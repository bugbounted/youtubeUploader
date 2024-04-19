from flask import Flask, render_template
from threading import Thread
from aiogram import executor
import filters
import handlers
from loader import dp

app = Flask(__name__)

# Define your Flask route for the index page
@app.route('/')
def index():
    return render_template('index.html')  # Replace 'index.html' with your actual HTML file

def run_flask():
    app.run(port=8000)  # Run Flask on port 8000

if __name__ == '__main__':
    # Start aiogram polling
    executor.start_polling(dp, skip_updates=True)
    
    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
