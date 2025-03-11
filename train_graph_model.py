import os
import csv
from typing import List
from collections import Counter
from pecanpy import pecanpy
from gensim.models import Word2Vec
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import faiss
import multiprocessing
import gc
from sklearn.decomposition import PCA
import pickle
from light_embed import TextEmbedding
import sys
from rocksdbpy import Option
import rocksdbpy
import struct

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


def get_code_files_in_directory(directory_path, extension):
    """Get all Python files in a directory, including subdirectories."""
    python_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(extension):
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


# Function to delete the RocksDB database if it exists
def delete_db_if_exists(db_path):
    if os.path.exists(db_path):
        print(f"Deleting existing database at {db_path}")
        # Remove the database directory (RocksDB stores files in a folder)
        os.remove(db_path)


def faiss_rocksdb_dump(model):
    os.makedirs("artifacts", exist_ok=True)

    try:
        # Delete the existing databases if they exist
        delete_db_if_exists("artifacts/line_to_idx.db")
        delete_db_if_exists("artifacts/idx_to_line.db")
    except Exception as err:
        print("Permission Denied: please delete folders artifacts/line_to_idx.db and artifacts/idx_to_line.db manually")
        sys.exit(1)

    txt_embed_model = TextEmbedding('onnx-models/all-MiniLM-L6-v2-onnx')  # embed text for OOV handling

    # Load the full vectors
    line_vectors = model.wv.vectors

    # Get total vocabulary size
    total_lines = len(line_vectors)

    print(f"Total code lines in vocabulary: {total_lines}")

    # Select the top N most frequent lines
    top_n = 1000000
    top_lines = model.wv.index_to_key[:top_n]

    # Create a list of vectors for FAISS
    vectors = []
    opts = Option()
    opts.create_if_missing(True)

    line_to_idx = rocksdbpy.open('artifacts/line_to_idx.db', opts)
    idx_to_line = rocksdbpy.open('artifacts/idx_to_line.db', opts)

    idx = 0
    for line in top_lines:
        vector = line_vectors[model.wv.key_to_index[line]]
        line_to_idx.set(line.encode(), struct.pack("i", idx))
        idx_to_line.set(struct.pack("i", idx), line.encode())
        vectors.append(vector)
        idx += 1

    # Convert the list of vectors into a NumPy array
    vectors_for_faiss = np.array(vectors, dtype=np.float16)

    print(vectors_for_faiss.shape)

    # Create a FAISS index (for example, using L2 distance)
    index = faiss.IndexFlatL2(vectors_for_faiss.shape[1])  # Using L2 distance
    index = faiss.IndexScalarQuantizer(vectors_for_faiss.shape[1], faiss.ScalarQuantizer.QT_fp16)

    # Add vectors to the FAISS index
    index.add(vectors_for_faiss)

    # Save the FAISS index
    faiss.write_index(index, 'artifacts/faiss_index.bin')

    # generate text embeddings for OOV handling
    txt_embeddings = txt_embed_model.encode(top_lines)

    if txt_embeddings.shape[0] > vectors_for_faiss.shape[1]:
        # Reduce the dimensionality to 128 dimensions using PCA
        pca = PCA(n_components=vectors_for_faiss.shape[1])
        reduced_txt_embeddings = pca.fit_transform(txt_embeddings)
        # Save the PCA model for dimensionality reduction
        with open('artifacts/pca_model.pkl', 'wb') as file:
            pickle.dump(pca, file)
        txt_embeddings_for_faiss = reduced_txt_embeddings.astype(np.float16)
    else:
        txt_embeddings_for_faiss = txt_embeddings.astype(np.float16)

    print(txt_embeddings_for_faiss.shape)

    # Create a FAISS index for txt embeddings
    txt_embed_index = faiss.IndexFlatL2(txt_embeddings_for_faiss.shape[1])  # Using L2 distance
    txt_embed_index = faiss.IndexScalarQuantizer(txt_embeddings_for_faiss.shape[1], faiss.ScalarQuantizer.QT_fp16)

    # Add vectors to the FAISS index
    txt_embed_index.add(txt_embeddings_for_faiss)

    # Save the FAISS index
    faiss.write_index(txt_embed_index, 'artifacts/faiss_txt_embed_index.bin')

    print("FAISS index and RocksDB stores saved successfully!")


def get_edg_files_in_directory(directory_path="shards") -> List[str]:
    """Get all Python files in a directory, including subdirectories."""
    edg_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".edg"):
                edg_files.append(os.path.join(root, file))
    return edg_files


def line_completion(directory_path: str, language: str):
    """
    Train next line suggestion model
    
    Args:
        directory_path (str): path to root folder of code repo or code folder
        language (str): Python/C++/Java/Scala/JavaScript/TypeScript/Dart/Rust/C#/Go
    """
    extensions = {
        "Python": ".py",
        "C++": ".cpp",
        "Java": ".java",
        "Scala": ".scala",
        "JavaScript": ".js",
        "TypeScript": ".ts",
        "Dart": ".dart",
        "Rust": ".rs",
        "C#": ".cs",
        "Go": ".go"
    }
    input_files = get_code_files_in_directory(directory_path, extensions[language])
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
    
    faiss_rocksdb_dump(model)


# Example usage
directory_path = "test/"  # Replace with your folder path
line_completion(directory_path, "Python")
