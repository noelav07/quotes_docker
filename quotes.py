from flask import Flask, render_template
import random

app = Flask(__name__)
app.template_folder = 'templates'

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future depends on what you do today. - Mahatma Gandhi",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Anger is a sign of weakness -Noel "
]

@app.route('/')
def index():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
