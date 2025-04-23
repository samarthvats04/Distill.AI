# SUMMARYGenie

## Introduction

SUMMARYGenie is an AI-powered research and summarization tool that automatically retrieves information from the web and creates concise, informative summaries on any topic. This application combines powerful search capabilities with advanced language models to provide users with comprehensive answers to research queries through a clean, user-friendly interface.

The system uses Tavily's search API to gather relevant information from across the web, and then processes this data using Mistral AI to generate well-structured, detailed summaries - all accessible through a simple web interface.

## Features

- **Web-based Research**: Enter any query and get comprehensive answers based on up-to-date web information
- **AI-Powered Summarization**: Transforms raw search results into coherent, well-structured summaries
- **LangGraph Pipeline**: Modular architecture using LangGraph for orchestrating the research workflow
- **Elegant User Interface**: Clean, responsive design with modern gradient styling
- **Interactive Results**: Engaging typing animation for displaying results
- **Download Capability**: Save generated summaries as text files for later reference
- **Data logging**: Automatically saves search results and answers as JSON files

## Tech Stack

### Backend
- **Python 3.10 or above**: Core programming language
- **Flask**: Web framework for the application
- **LangGraph**: For orchestrating the research and summarization workflow
- **Tavily API**: For web search and data gathering
- **Mistral AI**: Using Mistral-7B-Instruct model for generating summaries
- **Together API**: Client for accessing Mistral AI models

### Frontend
- **HTML/CSS**: For the user interface
- **JavaScript**: For interactive elements and API communication
- **Modern UI**: Custom styling with gradients, animations, and responsive design

## Required Dependencies

```
flask
python-dotenv
tavily-python
langgraph
together
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/samarthvats04/SUMMARYGenie.git
   ```

2. Navigate to the project directory:
   ```
   cd SUMMARYGenie
   ```

3. Install the required dependencies:
   ```
   pip install flask python-dotenv tavily-python langgraph langchain-community together
   ```
   
4. Create a `.env` file in the root directory with your API keys:
   ```
   TAVILY_API_KEY=your_tavily_api_key_here
   TOGETHER_API_KEY=your_mistral_api_key_here
   ```

## How to Run

1. Open the root directory of the project in your preferred text editor or IDE (I used PyCharm):

2. Start the Flask application:
   Run this command in the terminal
   ```
   python app_flask.py
   ```

3. Navigate to the following port address:
   ```
   http://127.0.0.1:5000/
   ```
   this port address can be found in the terminal itself after running the app.<br>
   The application will run locally in your browser.
   
5. Enter your research query in the input field and click "Go" to generate a summary.

## Project Structure

```
SUMMARYGenie/
├── app_flask.py           # Flask web application
├── langgraph_pipeline.py  # LangGraph workflow definition
├── research_agent.py      # Tavily search integration
├── answer_drafter.py      # Mistral AI integration for summarization
├── templates/
│   └── index.html         # Web interface template
├── data/                  # Directory for storing search results and answers
└── .env                   # Environment variables (API keys)
```

## Usage Guide

1. Enter a specific research query in the search box (e.g., "Impact of AI on Education in 2024")
2. Click "Go" or press Enter to submit your query
3. Wait while the system gathers information and generates a summary
4. Review the generated summary, which will appear with a typing animation
5. Use the "Download as .txt" button to save the summary for later reference

## Getting API Keys

### Tavily API
1. Visit [Tavily AI](https://tavily.com/)
2. Sign up for an account
3. Navigate to the API section to obtain your API key

## App UI


### Mistral API (via Together)
1. Visit [Together AI](https://www.together.ai/)
2. Create an account
3. Navigate to the API section to get your API key for accessing Mistral models
