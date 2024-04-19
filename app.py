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

if __name__ == '__main__':
    # Run Flask app on port 8000
    app.run(port=8000, debug=True, threaded=True)

    # Start aiogram polling
    executor.start_polling(dp)
