import psutil
from gensim.models import Word2Vec
import time

# Function to get current resource usage
def get_resource_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_usage = memory_info.rss / (1024 * 1024)  # Convert to MB
    return cpu_percent, memory_usage

def infer(line):

    # Load the saved Node2Vec model
    model = Word2Vec.load('graph_embeddings.model')

    # Find and print the most similar tokens
    for similar_line in model.wv.most_similar(line)[:1]:
        next_line = similar_line[0]
        print(next_line)
    
    return next_line

# Start measuring time
start_time = time.time()
print("started timing")

# Track initial resource usage
initial_cpu, initial_memory = get_resource_usage()


#line_completion()
pred_line = infer("def factorial(n):")

# Track resource usage after generation
final_cpu, final_memory = get_resource_usage()

# Calculate execution time
execution_time = time.time() - start_time

# Print the results
print(f"Generated Output: {pred_line}")
print(f"Execution Time: {execution_time:.4f} seconds")
print(f"CPU Usage: {final_cpu - initial_cpu}%")
print(f"Memory Usage: {(final_memory - initial_memory):.2f} MB")