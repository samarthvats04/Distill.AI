from flask import Flask, render_template, request, jsonify, send_file
from langgraph_pipeline import graph  # Assuming you have the langgraph pipeline set up already

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_query', methods=['POST'])
def submit_query():
    query = request.form['query']
    if not query.strip():
        return jsonify({"error": "Please enter a valid query!"}), 400

    # Running the graph to get the result
    result = graph.run(query)
    return jsonify({"result": result, "query": query})

@app.route('/download/<query>', methods=['GET'])
def download(query):
    result = graph.run(query)
    response = jsonify(result)
    response.headers["Content-Disposition"] = f"attachment; filename=ai_research_answer.txt"
    response.mimetype = "text/plain"
    return response

if __name__ == "__main__":
    app.run(debug=True)
