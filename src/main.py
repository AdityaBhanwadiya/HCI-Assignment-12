import openai
import os
from config import Config
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Configure CORS to allow requests from the React frontend
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://localhost:3001", "http://192.168.0.14:3001"]}})

# Set up OpenAI client for Azure
# Initialize the Azure OpenAI client with API key, version, and endpoint from the configuration
openai.api_type = "azure"
openai.api_base = Config.AZURE_OPENAI_ENDPOINT
openai.api_version = Config.AZURE_OPENAI_API_VERSION
openai.api_key = Config.AZURE_OPENAI_API_KEY


# Function to generate a creative "Hello World" message
def generate_hello_world(name):
    try:
        response = openai.ChatCompletion.create(
        engine=Config.AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"Generate a unique 'Hello World' message in a fun way for {name}. Don't forget to include the name in the message."}
        ],
        temperature=0.7
    )


        # Extract and return the generated message from the response
        return response.choices[0].message.content 

    except Exception as e:
        # Handle exceptions and return the error message
        return f"Error: {str(e)}"

@app.route('/api/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', 'there')
    message = generate_hello_world(name)
    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
