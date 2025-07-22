from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    print("Starting test Flask app...")
    app.run(debug=True)