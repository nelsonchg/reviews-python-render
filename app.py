from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привет! Python-проект работает на Render."

@app.route('/reviews')
def get_reviews():
    try:
        with open('reviews.json', 'r', encoding='utf-8') as f:
            import json
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/html')
def get_html():
    return send_file("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)