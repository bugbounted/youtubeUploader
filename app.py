from threading import Thread
from flask import Flask

# Import your aiogram related code
from aiogram import executor
import filters
import handlers
from loader import dp

# Create a Flask app
app = Flask(__name__)

# Define a route for your index page
@app.route('/')
def index():
    return 'Hello, World! This is your index page.'

def run_flask():
    # Run Flask app on port 8000
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    # Start a thread to run Flask app
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    # Start aiogram polling
    executor.start_polling(dp)
