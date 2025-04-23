import os
import json
from tavily import TavilyClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Tavily client
tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=tavily_api_key)

# Function to gather raw data using Tavily
def gather_data(query, num_results=10):
    """
    This function fetches data from Tavily API based on the query.
    """
    results = tavily_client.search(query, num_results=num_results)
    print(f"API returned {len(results)} results")

    # Save raw data to a json file in the data subfolder
    if not os.path.exists("data"):
        os.makedirs("data")  # Create the data folder if it doesn't exist

    # Save raw results in a JSON file
    filename = f"data/{query.replace(' ', '_')}_results.json"
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)

    return results
