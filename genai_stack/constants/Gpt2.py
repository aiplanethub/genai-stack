import openai

# Set your OpenAI API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

# Prompt for text generation
prompt = "Once upon a time"

# Generate text with GPT-2
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50  # Adjust the number of tokens as needed
)

# Extract and print the generated text
generated_text = response.choices[0].text
print(generated_text)
