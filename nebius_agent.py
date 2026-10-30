import json
from openai import OpenAI

# Initialize the OpenAI client pointing to the Nebius endpoint
client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key="v1.CmQKHHN0YXRpY2tleS1lMDBjcnYwdDlidDlnc3prYngSIXNlcnZpY2VhY2NvdW50LWUwMGNleDc3eDB0NHBkcGR4bjIMCNfCjdcGEKC32MwBOgwIzMWlogcQwKnlrgJAAloDZTAw.AAAAAAAAAAEuY7TutcKLKhdoJPtu3jISwZFRevwsPKH9SUxrGR5HYssuTX_byGwPaeSnW9IPl_1xbdWVIT_xIyq9auqjabkF" # <--- Paste your API key here
)

def get_churn_risk(user_data):
    # This is the prompt asking the AI to analyze the user
    system_prompt = "You are a behavioral analyst for a SaaS company. Rate the user's churn risk from 1-10 and explain why in one sentence."
    
    # We convert the user's data dictionary back to a string so the AI can read it
    user_string = json.dumps(user_data)
    
    try:
        response = client.chat.completions.create(
            model="nvidia/Nemotron-3.5-Super-VL", # Example model, replace with Nemotron if available on Nebius
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is the user data: {user_string}"}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to API: {e}"

if __name__ == "__main__":
    # Let's test it with User B from your mock database
    user_b_mock_data = {
        "id": "user_b",
        "name": "User B",
        "status": "Frustrated",
        "login_frequency": "rare",
        "features_used": ["dashboard"],
        "support_tickets": [
            {"issue": "billing discrepancy", "status": "open"},
            {"issue": "billing failed", "status": "closed"},
            {"issue": "invoice request", "status": "open"}
        ],
        "days_since_last_login": 5
    }

    print("Analyzing User B...")
    result = get_churn_risk(user_b_mock_data)
    print(f"AI Decision: {result}")
