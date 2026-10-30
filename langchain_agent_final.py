import json
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

# 1. Initialize the LangChain LLM to point to Nebius
llm = ChatOpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key="v1.CmQKHHN0YXRpY2tleS1lMDBjcnYwdDlidDlnc3prYngSIXNlcnZpY2VhY2NvdW50LWUwMGNleDc3eDB0NHBkcGR4bjIMCNfCjdcGEKC32MwBOgwIzMWlogcQwKnlrgJAAloDZTAw.AAAAAAAAAAEuY7TutcKLKhdoJPtu3jISwZFRevwsPKH9SUxrGR5HYssuTX_byGwPaeSnW9IPl_1xbdWVIT_xIyq9auqjabkF", # <--- Paste your API key here again
    model="nvidia/Nemotron-3.5-Super-VL", 
    temperature=0.1
)

# 2. Define the Tools
@tool
def send_retention_email(user_name: str, issue: str) -> str:
    """Sends a personalized tutorial or retention email to a frustrated user."""
    print(f"\n[ACTION TAKEN] Sending email to {user_name} with a tutorial about {issue}.")
    return "Email sent successfully."

@tool
def offer_discount(user_name: str, discount_percent: int) -> str:
    """Offers a discount promo code to a fading user."""
    print(f"\n[ACTION TAKEN] Generating a {discount_percent}% off promo code for {user_name}.")
    return "Discount offered successfully."

tools = [send_retention_email, offer_discount]

# 3. Bind tools natively (Bypasses the buggy langchain.agents module!)
llm_with_tools = llm.bind_tools(tools)

if __name__ == "__main__":
    # Let's test it with User B's scenario
    user_scenario = """
    User Name: User B
    Status: Frustrated
    Churn Risk Score: 8/10
    Reason: The user is highly frustrated because they have 3 open support tickets regarding billing failures.
    """
    
    prompt = f"Here is the analysis of a user: {user_scenario}\nIf the churn risk is over 7, decide whether to send a helpful email or offer a discount to save them, and use the correct tool."
    
    print("Running Agentic Decision...")
    try:
        # Ask the AI to make a decision
        response = llm_with_tools.invoke(prompt)
        
        # Manually execute the tool it decided to use
        if response.tool_calls:
            for tool_call in response.tool_calls:
                print(f"\n[AI DECISION] The AI chose to use: {tool_call['name']}")
                if tool_call["name"] == "send_retention_email":
                    send_retention_email.invoke(tool_call["args"])
                elif tool_call["name"] == "offer_discount":
                    offer_discount.invoke(tool_call["args"])
        else:
            print("\n[AI DECISION] The AI responded without using a tool:", response.content)
            
    except Exception as e:
        print("\nError running the agent:", e)
