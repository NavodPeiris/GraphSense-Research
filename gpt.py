import time
import psutil
from transformers import AutoTokenizer, AutoModelWithLMHead

# Function to get current resource usage
def get_resource_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_usage = memory_info.rss / (1024 * 1024)  # Convert to MB
    return cpu_percent, memory_usage


# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")
model = AutoModelWithLMHead.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")

# Specify whether to use CPU
use_cpu = True
context = "def factorial(n):"
lang = "python"  # can be java as well.

# Move model to CPU if required
if use_cpu:
    model.to("cpu")

# Start measuring time
start_time = time.time()
print("started timing")

# Track initial resource usage
initial_cpu, initial_memory = get_resource_usage()

# Prepare input
input_ids = tokenizer.encode("<python> " + context,
                             return_tensors='pt') if lang == "python" else tokenizer.encode(
    "<java> " + context, return_tensors='pt')

# Generate output
outputs = model.generate(input_ids=input_ids.to("cpu") if use_cpu else input_ids,
                         max_length=128,
                         temperature=0.7,
                         num_return_sequences=1)

# Decode the output
decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Track resource usage after generation
final_cpu, final_memory = get_resource_usage()

# Calculate execution time
execution_time = time.time() - start_time

# Get the first line
first_line = decoded.splitlines()[1]

# Print the results
print(f"Generated Output: {first_line}")
print(f"Execution Time: {execution_time:.4f} seconds")
print(f"CPU Usage: {final_cpu - initial_cpu}%")
print(f"Memory Usage: {(final_memory - initial_memory):.2f} MB")
