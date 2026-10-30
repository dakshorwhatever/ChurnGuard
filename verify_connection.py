import json
from openai import OpenAI

# Initialize the OpenAI client pointing to the Nebius endpoint
client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key="YOUR_NEBIUS_API_KEY" # <--- Paste your API key here
)

def verify_connection():
    # Using the standard Nemotron 70B model identifier 
    model_name = "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF" 
    print(f"Attempting to connect to Nebius API using model: {model_name}...")
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": "Hello, this is a connection test. Please reply with 'Connection successful'."}
            ],
            max_tokens=15
        )
        print("\nSUCCESS! The AI replied:", response.choices[0].message.content)
    except Exception as e:
        print("\nCONNECTION ERROR:")
        print(str(e))
        print("\nTroubleshooting Tips:")
        print("1. Did you replace 'YOUR_NEBIUS_API_KEY' with your actual key?")
        print("2. Is the model name correct in your Nebius Token Factory console?")

if __name__ == "__main__":
    verify_connection()
