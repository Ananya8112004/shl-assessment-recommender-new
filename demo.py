import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="AIzaSyDjmEWQaMi1d-kFwzMdjy-E7MUh1KyoY-c")

# Update to the new model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Generate content
response = model.generate_content("Tell me a joke.")
print(response.text)
