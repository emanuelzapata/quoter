#imports
from flask import Flask, jsonify, request, Response
from dotenv import load_dotenv
import json
import secrets

load_dotenv()

quotes = json.load(open("quotes.json"))

app = Flask(__name__)

@app.get('/ping')
def ping():
    return Response(status=200)

@app.post('/quote')
def quote():
    return json.dumps(secrets.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)