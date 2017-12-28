from flask import Flask
app = Flask(__name__)

@app.route("/api/v1/info")
def hello():
    return "Hello Cloud-Native-Python World!"

@app.route("/api/v1/info/subworld")
def helloSubworld():
    return "Hello Lower Cloud-Native-Python World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
