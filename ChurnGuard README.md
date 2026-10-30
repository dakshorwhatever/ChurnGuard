# 🛡️ ChurnGuard: Autonomous SaaS Retention Agent

**ChurnGuard** is an active AI agent that predicts when a SaaS user will cancel and takes immediate, personalized action to save them. Built for the Devpost Hackathon.

## ⚠️ Problem & Solution

Passive dashboards detect churn too late, and traditional ML only predicts it without intervening. ChurnGuard acts as an autonomous Customer Success Manager. It monitors user activity, uses advanced AI reasoning to diagnose churn risk, and triggers real-world actions (like tutorial emails or targeted discounts) to retain users *before* they leave.

## ⚙️ Architecture

1. **Data Ingestion:** Simulates pulling user activity (logins, tickets) from a mock database (`mock_database.json`).  
2. **Analysis:** Feeds data to **NVIDIA Nemotron 70B** via the **Nebius Token Factory API**. The model scores churn risk (1-10) and diagnoses specific pain points.  
3. **Action:** Using **LangChain**, if risk \> 7, the agent autonomously selects a tool (e.g., `send_retention_email`, `offer_discount`) to resolve the issue.  
4. **UI:** A clean **Streamlit** dashboard allows managers to audit decisions.

## 🛠️ Tech Stack

* **AI Model:** NVIDIA Llama-3.1-Nemotron-70B-Instruct-HF  
* **Cloud Infrastructure:** Nebius AI Cloud (Token Factory)  
* **Framework & UI:** LangChain, Streamlit (Python 3\)

## 🚀 Quick Start

**1\. Prerequisites:** Python 3.8+ and a valid [Nebius API Key](https://nebius.ai/).

**2\. Install:**

```sh
git clone https://github.com/YOUR_USERNAME/ChurnGuard.git
cd ChurnGuard
python -m pip install -U streamlit langchain langchain-openai langchain-core openai
```

**3\. Run:** Ensure `mock_database.json` is present in the root folder, then launch the app:

```sh
python -m streamlit run app.py
```

**4\. Use:** Paste your Nebius API Key into the dashboard and click **"Run AI Agent"** to watch the Nemotron model autonomously trigger retention tools\!

*License: MIT*