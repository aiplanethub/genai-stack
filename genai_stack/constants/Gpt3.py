import openai

# Set your OpenAI API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

# Define a prompt
prompt = "Translate the following English text to French: 'Hello, how are you?'"

# Use the GPT-3 model to generate text
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50  # Adjust as needed
)

# Extract and print the generated text
generated_text = response.choices[0].text
print(generated_text)
