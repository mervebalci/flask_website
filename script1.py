from flask import Flask

app=Flask(__name__)

@app.route('/')
# This / means the home page

def home():
    return "Website content goes here!"

if __name__ == "__main__":
    app.run(debug=True)
