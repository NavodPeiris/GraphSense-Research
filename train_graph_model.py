import os
import csv
from typing import List
from collections import Counter
import joblib
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec
import duckdb
import umap
import umap.plot
from mpl_toolkits.mplot3d import Axes3D
from pecanpy import pecanpy
from gensim.models import Word2Vec
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import faiss
import multiprocessing
import gc

def is_comment_or_empty(line: str, in_block_comment: bool) -> (bool, bool):
    """Check if a line is a comment or part of a multi-line comment."""
    stripped = line.strip()

    # Handle block comments (triple quotes)
    if stripped.startswith('"""') or stripped.startswith("'''"):
        if (stripped.endswith('"""') or stripped.endswith("'''")) and (stripped != '"""' and stripped != "'''"):
            # If the line contains both start and end of block comment, treat it as a single-line comment
            return True, False
        elif in_block_comment:
            # If we are already inside a block comment, this ends it
            return True, False
        else:
            # If we are not inside a block comment, this starts it
            return True, True

    if stripped.endswith('"""') or stripped.endswith("'''"):
        return True, False

    # Handle single-line comments (#, //, C-style)
    if stripped.startswith("#") or stripped.startswith("//"):
        return True, False

    # Handle C-style block comments (/* ... */)
    if stripped.startswith("/*"):
        return True, True
    if stripped.endswith("*/"):
        return True, False
    # If inside a block comment, ignore all lines
    if in_block_comment:
        return True, in_block_comment

    return False, in_block_comment


def get_python_files_in_directory(directory_path: str) -> List[str]:
    """Get all Python files in a directory, including subdirectories."""
    python_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def process_file(input_file):
    pairs = []  # Local variable to store the pairs for this file
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file {input_file} does not exist.")

        with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        current_line = None
        next_line = None
        in_block_comment = False

        # Process each line
        for i in range(len(lines) - 1):
            # Check if the line is a comment or empty and if we are inside a block comment
            is_comment, in_block_comment = is_comment_or_empty(lines[i], in_block_comment)
            if not is_comment and not in_block_comment:
                if current_line == None or current_line.strip() == "":
                    current_line = lines[i].strip()  # Remove leading/trailing whitespace
                if current_line.strip() != "" and current_line != None:  # Only consider non-empty lines
                    next_line = lines[i + 1].strip()  # Remove leading/trailing whitespace
                    if (current_line.strip() != "" 
                        and current_line != None 
                        and next_line != None 
                        and not next_line.startswith("'''") 
                        and not next_line.endswith("'''") 
                        and not next_line.startswith('"""') 
                        and not next_line.endswith('"""') 
                        and not next_line.startswith("#")
                        and not next_line.startswith("//")
                        and not next_line.startswith("/*")
                        and not next_line.endswith("*/")
                    ):
                        if next_line.strip() != "":
                            pairs.append((current_line, next_line))
                        current_line = None
                        next_line = None
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")
    
    return pairs  # Return the pairs found in this file


def datagen_line(input_files: List[str], output_csv: str):
    """
    Generate a CSV dataset with columns `current_line`, `next_line`, and `occurrence_ct`.
    
    Args:
        input_files (List[str]): List of paths to the input Python files.
        output_csv (str): Path to the output CSV file.
    """
    all_pairs = []
    
    # Use ThreadPoolExecutor to divide the work among multiple threads
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_file, input_file): input_file for input_file in input_files}
        
        # Collect results as they complete
        for future in as_completed(futures):
            file_pairs = future.result()
            all_pairs.extend(file_pairs)

    # Count occurrences of each pair
    pair_counts = Counter(all_pairs)
    rows = [(current_line, next_line, count) for (current_line, next_line), count in pair_counts.items()]

    # Write to CSV
    with open(output_csv, "w", encoding="utf-8", newline="", errors="ignore") as csvfile:
        writer = csv.writer(csvfile, delimiter='‖')
        #writer.writerow(["current_line", "next_line", "occurrence_ct"])
        writer.writerows(rows)

    print(f"Dataset created at {output_csv} with {len(rows)} rows.")



def datagen(input_files: List[str], output_csv: str):
    """
    Generate a CSV dataset with columns `sentence`, `next_token`, and `occurrence_ct`.
    
    Args:
        input_files (List[str]): List of paths to the input Python files.
        output_csv (str): Path to the output CSV file.
    """
    pairs = []
    in_block_comment = False

    for input_file in input_files:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file {input_file} does not exist.")

        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Process each line
        for line in lines:
            # Check if the line is a comment or empty and if we are inside a block comment
            is_comment, in_block_comment = is_comment_or_empty(line, in_block_comment)
            if not is_comment and not in_block_comment:
                current_line = line.split()  # Remove leading/trailing whitespace
                for i in range(len(current_line)-1):
                    pairs.append((current_line[i], current_line[i+1]))

    # Count occurrences of each pair
    pair_counts = Counter(pairs)
    rows = [(current_word, next_word, count) for (current_word, next_word), count in pair_counts.items()]

    # Write to CSV
    with open(output_csv, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter='‖')
        #writer.writerow(["current_word", "next_word", "occurrence_ct"])
        writer.writerows(rows)

    print(f"Dataset created at {output_csv} with {len(rows)} rows.")


def shard_edg_file(file_path, max_edges=100000, delimiter="‖"):
    os.makedirs("shards", exist_ok=True)
    
    with open(file_path, 'r', encoding='utf-8') as infile:
        file_count = 0
        line_count = 0
        outfile = None
        
        for line in infile:
            if line_count % max_edges == 0:
                if outfile:
                    outfile.close()
                file_count += 1
                output_filename = f"shards/shard_{file_count}.edg"
                outfile = open(output_filename, 'w', encoding='utf-8') 
                print(f"Creating {output_filename}")
            
            outfile.write(line)
            line_count += 1
        
        if outfile:
            outfile.close()
    
    print(f"Sharding complete. {file_count} files created.")


def get_edg_files_in_directory(directory_path="shards") -> List[str]:
    """Get all Python files in a directory, including subdirectories."""
    edg_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".edg"):
                edg_files.append(os.path.join(root, file))
    return edg_files


def line_completion(directory_path: str):
    input_files = get_python_files_in_directory(directory_path)
    output_csv_path = "output_dataset.edg"
    datagen_line(input_files, output_csv_path)

    g = pecanpy.SparseOTF(p=1, q=0.5, workers=-1, verbose=True, extend=True)

    try:
        if os.path.exists("shards"):
            print(f"Deleting existing shards")
            # Remove the database directory (RocksDB stores files in a folder)
            os.remove("shards")
    except Exception as err:
        print("Permission Denied: please delete shards folder manually")
        sys.exit(1)

    shard_edg_file(output_csv_path)

    edg_files = get_edg_files_in_directory()

    edg_files = edg_files[:20]
    
    num_cores = multiprocessing.cpu_count()
    if num_cores > 1:
        worker_cores = num_cores - 1
    else:
        worker_cores = num_cores

    model = Word2Vec(
        vector_size=128, window=5, min_count=1, workers=worker_cores, sg=1, hs=1
    )

    first_file = True
    i = 0
    for edg_file in edg_files:
        # Load graph and simulate walks
        g.read_edg(edg_file, weighted=True, directed=False, delimiter="‖")
        i += 1
        print(f"sharded file: {i}")

        walks = g.simulate_walks(num_walks=10, walk_length=10)
        
        if first_file:
            # Build vocabulary from the first batch of walks
            model.build_vocab(walks)
            first_file = False
        else:
            # Update vocabulary incrementally
            model.build_vocab(walks, update=True)
        
        # Train the model
        model.train(walks, total_examples=len(walks), epochs=100)

    # Convert word vectors to float16 to reduce memory usage
    model.wv.vectors = model.wv.vectors.astype(np.float16)
    
    model.save("small_model/graph_embeddings.model")


def word_completion(directory_path: str):
    input_files = get_python_files_in_directory(directory_path)
    output_csv_path = "output_dataset.edg"
    datagen(input_files, output_csv_path)

    g = pecanpy.SparseOTF(p=1, q=0.5, workers=-1, verbose=True, extend=True)
    g.read_edg("output_dataset.edg", weighted=True, directed=False)
    
    walks = g.simulate_walks(num_walks=200, walk_length=20)

    model = Word2Vec(walks, hs=1, sg=1, vector_size=128, window=10, min_count=1, workers=4, epochs=1)
    
    print("Saving the model...")
    # Convert word vectors to float16 to reduce memory usage
    model.wv.vectors = model.wv.vectors.astype(np.float16)

    # Save the model with reduced precision
    model.save("graph_embeddings.model")


# Example usage
directory_path = "dataset/"  # Replace with your folder path
line_completion(directory_path)
