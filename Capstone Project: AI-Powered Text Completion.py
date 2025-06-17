# ai_text_completion_app.py - version Hugging Face

from transformers import pipeline, set_seed
import os

# Load text-generation pipeline
# You can choose from various models like "gpt2", "distilgpt2", or others hosted on Hugging Face
text_generator = pipeline("text-generation", model="gpt2")
set_seed(42)  # Optional: for reproducible outputs

# Function to generate text from prompt
def generate_text(prompt, temperature=0.7, max_tokens=150):
    try:
        outputs = text_generator(
            prompt,
            max_length=max_tokens + len(prompt.split()),
            do_sample=True,
            temperature=temperature,
            top_k=50,
            top_p=0.95,
            num_return_sequences=1
        )
        return outputs[0]["generated_text"].strip()
    except Exception as e:
        return f"Generation Error: {e}"

def main():
    print("Welcome to the Hugging Face Text Completion App!")
    print("Type 'exit' to quit the app.")

    while True:
        prompt = input("\nEnter your prompt: ")
        if prompt.lower() == 'exit':
            break
        if not prompt.strip():
            print("Prompt cannot be empty.")
            continue

        try:
            temp = float(input("Set temperature (0.0–1.0, default=0.7): ") or 0.7)
            max_toks = int(input("Set max tokens (e.g., 150): ") or 150)
        except ValueError:
            print("Invalid input. Using default parameters.")
            temp = 0.7
            max_toks = 150

        output = generate_text(prompt, temperature=temp, max_tokens=max_toks)
        print(f"\nAI Response:\n{output}")

if __name__ == "__main__":
    main()
