from transformers import AutoTokenizer, AutoModelWithLMHead
import psutil
import os
import time
import matplotlib.pyplot as plt

tokenizer = None
model = None

def infer_gpt_model():
    # Specify whether to use CPU
    use_cpu = True
    context = "def factorial(n):"
    lang = "python"  # can be java as well.

    # Move model to CPU if required
    if use_cpu:
        model.to("cpu")

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

    # Get the first line
    first_line = decoded.splitlines()[1]

# Lists to store memory usage and timestamps
memory_usage = []
timestamps = []
execution_times = []
execution_time = 0
consumed_memory = 0

if __name__ == "__main__":
    process = psutil.Process(os.getpid())
    before = process.memory_info().rss
    # Initialize tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")
    model = AutoModelWithLMHead.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")
    for i in range(10):
        # Start measuring time
        start_time = time.time()
        infer_gpt_model()
        # Calculate execution time
        exec_time = round(time.time() - start_time, 4)
        execution_time = execution_time + exec_time
        after = process.memory_info().rss
        mem = round((after - before) / 10**6, 4)
        consumed_memory = consumed_memory + mem

        timestamps.append(i + 1)  # Iteration number as timestamp
        memory_usage.append(mem)
        execution_times.append(exec_time)

    print(f"average memory usage: {round(consumed_memory/10, 4)} MB")
    print(f"average execution time: {round(execution_time/10, 4)} seconds")

    # Plot memory usage
    plt.figure(figsize=(8, 5))
    plt.plot(timestamps, memory_usage, marker='o', linestyle='-', color='b', label='Memory Usage (MB)')
    plt.xlabel("Iteration")
    plt.ylabel("Memory Used (MB)")
    plt.title("Memory Usage Over Iterations")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot execution time
    plt.figure(figsize=(8, 5))
    plt.plot(timestamps, execution_times, marker='o', linestyle='-', color='b', label='Execution Time (s)')
    plt.xlabel("Iteration")
    plt.ylabel("Execution Time (s)")
    plt.title("Execution Time Over Iterations")
    plt.legend()
    plt.grid(True)
    plt.show()