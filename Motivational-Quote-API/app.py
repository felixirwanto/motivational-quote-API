from flask import Flask, request, jsonify
from flasgger import Swagger
import openai

app = Flask(__name__)

# Initialize Swagger UI
swagger = Swagger(app)

# OpenAI API key (replace with your key)
openai.api_key = "Insert OpenAI Secret Key Here"

@app.route('/api/motivational-quote', methods=['POST'])
def generate_quote():
    """
    Generate a Motivational Quote
    ---
    tags:
      - Motivational Quotes
    parameters:
      - name: body
        in: body
        required: false
        schema:
          type: object
          properties:
            prompt:
              type: string
              description: "Optional custom prompt"
              example: "Give me a motivational quote today"
    responses:
      200:
        description: A motivational quote
        schema:
          type: object
          properties:
            quote:
              type: string
              description: The motivational quote
      500:
        description: Error message
    """
    data = request.get_json()
    prompt = data.get("prompt", "Give me a short motivational quote.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        quote = response['choices'][0]['message']['content'].strip()
        return jsonify({"quote": quote})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
