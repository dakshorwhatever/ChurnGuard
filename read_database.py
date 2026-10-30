import json

def read_and_print_mock_db():
    try:
        # Open and read the JSON file
        with open('mock_database.json', 'r') as file:
            data = json.load(file)
            
        # Print the parsed JSON data nicely formatted
        print("--- Mock Database Contents ---")
        print(json.dumps(data, indent=4))
        
    except FileNotFoundError:
        print("Error: 'mock_database.json' not found. Please ensure the file is in the same directory as this script.")

if __name__ == "__main__":
    read_and_print_mock_db()
