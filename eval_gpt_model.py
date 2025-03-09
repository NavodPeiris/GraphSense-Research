
from transformers import AutoTokenizer, AutoModelWithLMHead
import torch
import re

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")
model = AutoModelWithLMHead.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")

def infer_gpt_model(context, num_return_sequences=10):
    lang = "python"  # can be java as well.

    # Check if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Move model to GPU
    model.to(device)

    # Prepare input
    input_ids = tokenizer.encode("<python> " + context,
                                return_tensors='pt') if lang == "python" else tokenizer.encode(
        "<java> " + context, return_tensors='pt')

    # Generate output
    outputs = model.generate(input_ids=input_ids.to(device),
                            max_length=128,
                            temperature=0.7,
                            num_return_sequences=num_return_sequences,
                            do_sample = True
                            )

    # Decode all the generated outputs
    decoded_outputs = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

    print(decoded_outputs)
    print("\n\n")
    
    return decoded_outputs

test_lines = []
correct_next_lines = []

edg_file_path = "output_dataset.edg"

# Read the .edg file and parse the values
with open(edg_file_path, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("‖")  # Split using the delimiter
        if len(parts) >= 2:
            test_lines.append(parts[0])  # Current line
            correct_next_lines.append(parts[1])  # Next line

print(f"Loaded {len(test_lines)} test lines and {len(correct_next_lines)} correct next lines.")

top1_score = 0
top3_score = 0
top10_score = 0

test_lines = test_lines[1:11]
correct_next_lines = correct_next_lines[1:11]
hits = []

for i in range(len(test_lines)):
    similar_blocks = infer_gpt_model(test_lines[i])
    correct_next_line = correct_next_lines[i]
    for j in range(len(similar_blocks)):
        if(correct_next_line in similar_blocks[j]):
            hits.append(test_lines[i])
            if j == 0:  # Top 1
                top1_score += 1
                top3_score += 1
                top10_score += 1
            elif j <= 2:  # Top 3
                top3_score += 1
                top10_score += 1
            elif j <= 9:  # Top 10
                top10_score += 1
            break
        

print("top-1 accuracy = ", top1_score / len(test_lines))
print("top-3 accuracy = ", top3_score / len(test_lines))
print("top-10 accuracy = ", top10_score / len(test_lines))

missed = []
for line in test_lines:
    if line not in hits:
        missed.append(line)
print("missed: ", missed)

'''
res = infer_gpt_model("if pattern in all_patterns:")
print(res)
'''