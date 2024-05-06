from flask import Flask, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI;
import os

app = Flask(__name__)

load_dotenv()

open_api_key = os.getenv('OPENAI_SECRET_KEY')

# Set your OpenAI API Key here (better to use environment variables in production)
openai.api_key = open_api_key

@app.route('/generate-text', methods=['POST'])
def generate_text():
    try:
        data = request.json
        prompt = data.get('prompt')
        max_tokens = data.get('max_tokens', 100)

        # Call to OpenAI API
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Or any other model
            prompt=prompt,
            max_tokens=max_tokens
        )
        # Extract the generated text
        text = response.choices[0].text.strip()
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

