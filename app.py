import streamlit as st
import json
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

# ---- 1. DEFINE LANGCHAIN TOOLS ----
@tool
def send_retention_email(user_name: str, issue: str) -> str:
    """Sends a personalized tutorial or retention email to a frustrated user."""
    return f"Email sent to {user_name} regarding {issue}."

@tool
def offer_discount(user_name: str, discount_percent: int) -> str:
    """Offers a discount promo code to a fading user."""
    return f"Offered a {discount_percent}% discount to {user_name}."

# ---- 2. AI LOGIC ----
def analyze_and_act(user_scenario, api_key):
    llm = ChatOpenAI(
        base_url="https://api.studio.nebius.ai/v1/",
        api_key=api_key,
        model="nvidia/Nemotron-3.5-Super-VL", 
        temperature=0.1
    )
    tools = [send_retention_email, offer_discount]
    llm_with_tools = llm.bind_tools(tools)
    
    prompt = f"Here is the analysis of a user: {user_scenario}\nIf the churn risk is over 7, decide whether to send a helpful email or offer a discount to save them, and use the correct tool."
    return llm_with_tools.invoke(prompt)

# ---- 3. STREAMLIT UI ----
st.set_page_config(page_title="ChurnGuard UI", layout="wide")
st.title("🛡️ ChurnGuard: Autonomous Retention Agent")
st.write("Welcome to the Day 3 Demo! Monitor your users and let the AI take action.")

api_key = st.text_input("Enter Nebius API Key to run demo:", type="password")

# Hardcoded mock database for the UI demo
users = [
    {"name": "User A", "status": "Happy", "churn_score": "2/10", "reason": "Uses all features daily."},
    {"name": "User B", "status": "Frustrated", "churn_score": "8/10", "reason": "3 open support tickets regarding billing failures."},
    {"name": "User C", "status": "Fading", "churn_score": "6/10", "reason": "Login frequency dropped to weekly."}
]

st.divider()

# Create 3 columns for our 3 users
cols = st.columns(3)

for idx, user in enumerate(users):
    with cols[idx]:
        st.subheader(user['name'])
        st.write(f"**Status:** {user['status']}")
        st.write(f"**Churn Risk:** {user['churn_score']}")
        st.caption(f"**Context:** {user['reason']}")
        
        if st.button(f"Run AI Agent", key=user['name']):
            if not api_key:
                st.error("Please paste your API key at the top first!")
            else:
                with st.spinner("AI is thinking..."):
                    scenario = f"User Name: {user['name']}\nStatus: {user['status']}\nChurn Risk Score: {user['churn_score']}\nReason: {user['reason']}"
                    try:
                        response = analyze_and_act(scenario, api_key)
                        
                        if response.tool_calls:
                            for tool_call in response.tool_calls:
                                st.success(f"🤖 **ACTION TAKEN**")
                                st.info(f"Tool used: `{tool_call['name']}`\n\nDetails: {tool_call['args']}")
                        else:
                            st.info(f"🤖 **NO ACTION NEEDED**\n\nAI says: {response.content}")
                    except Exception as e:
                        st.error(f"Connection Error: {e}")
