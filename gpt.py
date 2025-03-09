from transformers import AutoTokenizer, AutoModelWithLMHead

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")
model = AutoModelWithLMHead.from_pretrained("congcongwang/gpt2_medium_fine_tuned_coder")

def infer_gpt_model(context):
    # Specify whether to use CPU
    use_cpu = True
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
    return first_line

res = infer_gpt_model("dsdsd")

# Print the results
print(f"Generated Output: {res}")
