from flask import Flask, request, jsonify
from flask_cors import CORS
import Action

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    try:
        with open('index.html', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "HTML file not found. Make sure index.html is in the same folder as app.py"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message', '')
        
        # Use your existing Action function
        response = Action.Action(message)
        
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting MITS Academy Chatbot Server...")
    print("Open your browser to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)