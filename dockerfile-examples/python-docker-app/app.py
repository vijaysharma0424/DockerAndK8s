from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello,Logiclabs students.. Welcome to  Docker, Today is Feb 6th!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
