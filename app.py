from flask import Flask
import parser

app = Flask(__name__)

@app.route('/')
def index():
    parser.main()
    return 'parser.py запущен!'

if __name__ == '__main__':
    app.run()
