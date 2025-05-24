from flask import Flask, request, jsonify, send_from_directory
import os
from nlp.nlp import load_data, process_query
import pandas as pd

app = Flask(__name__, static_folder="../frontend")

# Load data and NLP setup
df = load_data()

# Serve the front-end
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# Serve other static files (CSS, JS)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Handle user inquiries
@app.route('/api/inquiry', methods=['POST'])
def handle_inquiry():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    # Process the query using the NLP logic
    try:
        answer = process_query(query, df)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Handle admin data updates
@app.route('/api/update', methods=['POST'])
def update_data():
    data = request.get_json()
    index = data.get('index')
    new_answer = data.get('answer')
    
    if index is None or new_answer is None:
        return jsonify({'error': 'Index and answer required'}), 400
    
    try:
        # Update the DataFrame and save to CSV
        global df
        df.at[int(index), 'Answer'] = new_answer
        df.to_csv("../database/data.csv", index=False)
        return jsonify({'message': 'Data updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)