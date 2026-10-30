import sys

print("--- PYTHON ENVIRONMENT DIAGNOSTIC ---")
print(f"1. Python Executable Being Used: {sys.executable}")
print(f"2. Python Version: {sys.version}")

print("\n3. Checking LangChain Installation:")
try:
    import langchain
    print(f"   SUCCESS: LangChain is installed (Version: {langchain.__version__})")
except ImportError:
    print("   ERROR: LangChain is NOT installed in this specific Python environment.")

try:
    import langchain_openai
    print(f"   SUCCESS: langchain_openai is installed")
except ImportError:
    print("   ERROR: langchain_openai is NOT installed in this specific Python environment.")

print("\n--- HOW TO FIX ---")
print("If you see errors above, it means your 'pip' and 'python' commands are disconnected.")
print("Run THIS exact command in your terminal to install the packages to the correct environment:")
print(f"\"{sys.executable}\" -m pip install -U langchain langchain-openai langchain-core")
