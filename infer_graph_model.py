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

def infer(prev_line, line):

    # Load the saved Node2Vec model
    model = Word2Vec.load('graph_embeddings.model')

    correct_next_line = None
    max_sandwitch_prob = 0

    # Get the top most similar lines to the input line
    similar_lines = model.wv.most_similar(line)
    
    # Initialize the result list with the first line
    top_similar = [similar_lines[0][0]]
    
    # Compare each subsequent line's similarity with the first line's similarity
    for i in range(1, len(similar_lines)):
        # Check the difference in similarity with the previous highest score
        similarity_diff = similar_lines[0][1] - similar_lines[i][1]
        
        # If the difference exceeds the threshold, stop adding more results
        if similarity_diff > 0.2:
            break
        top_similar.append(similar_lines[i][0])
    
    print("top similar lines: ", top_similar)
    for top_next_line in top_similar:
        sandwitch_probs = dict(model.predict_output_word([prev_line, top_next_line]))
        sandwitch_prob = sandwitch_probs.get(line, 0)
        if(sandwitch_prob > max_sandwitch_prob):
            correct_next_line = top_next_line

    return correct_next_line
        

# Start measuring time
start_time = time.time()
print("started timing")

# Track initial resource usage
initial_cpu, initial_memory = get_resource_usage()


#line_completion()
pred_line = infer('if n % divisor == 0:', 'ans.append(divisor)')

# Track resource usage after generation
final_cpu, final_memory = get_resource_usage()

# Calculate execution time
execution_time = time.time() - start_time

# Print the results
print(f"Generated Output: {pred_line}")
print(f"Execution Time: {execution_time:.4f} seconds")
print(f"CPU Usage: {final_cpu - initial_cpu}%")
print(f"Memory Usage: {(final_memory - initial_memory):.2f} MB")