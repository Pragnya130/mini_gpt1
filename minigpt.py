from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

output = generator("AI is", max_length=30)

print(output[0]["generated_text"])