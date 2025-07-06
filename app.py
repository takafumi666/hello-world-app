from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1><p>AWS EC2で動作中です！</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
