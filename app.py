from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load GPT-2 Small model
generator = pipeline('text-generation', model='gpt2')

# Define API route for chat
@app.route('/chat', methods=['POST'])
def chat():
    # Get the prompt from the request
    data = request.json
    prompt = data.get('prompt', '')

    # Generate response using GPT-2
    response = generator(prompt, max_length=50, num_return_sequences=1)

    # Return the generated text
    return jsonify({'response': response[0]['generated_text']})

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)