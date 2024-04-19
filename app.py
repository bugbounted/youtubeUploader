from aiogram import executor
from flask import Flask, request, jsonify

import filters
import handlers
from loader import dp

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    executor.start_polling(dp)

    # Run the Flask app on port 8000
    app.run(host='127.0.0.1', port=8000)
