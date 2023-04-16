from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'A SaaS leszállt!'


if __name__ == '__main__':
    app.run(debug=True)
