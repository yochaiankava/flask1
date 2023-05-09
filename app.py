from flask import Flask
from news import news_pb
from sport import sport_pb

app = Flask(__name__)
app.register_blueprint(news_pb)
app.register_blueprint(sport_pb)

@app.route("/")
def hello_world():
    print("hello")
    # return "<p>Hello, World!</p>"
    return "<p>Hello, World!</p><button>Press</button>"

if __name__ == '__main__':
    app.run(debug=True, port=9000)
