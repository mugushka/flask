from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def get_greeting():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 24:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

@app.route('/login')
def index():
    greeting = get_greeting()
    return render_template('login.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)