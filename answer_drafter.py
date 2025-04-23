import os
import json
from dotenv import load_dotenv
from together import Client

# Load environment variables from .env file
load_dotenv()

# Initialize Mistral client
mistral_api_key = os.getenv("MISTRAL_API_KEY")
mistral_client = Client(api_key=mistral_api_key)

# Function to draft an answer using Mistral AI
def draft_answer(data, query):
    """
    This function drafts an answer using the raw data from Tavily.
    """
    context = "\n".join([item.get("content", "") for item in data if "content" in item])

    prompt = f"""You are a helpful research assistant.
    You are given the following context:\n{context}\n
    Based on this context, write a detailed and informative answer to the query:
    "{query}"\n
    Ensure that your answer is accurate and well-structured."""

    response = mistral_client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )

    # Save the generated answer as a JSON file
    filename = f"data/{query.replace(' ', '_')}_answer.json"
    with open(filename, 'w') as f:
        json.dump({"query": query, "answer": response.choices[0].message.content}, f, indent=4)

    return response.choices[0].message.content
