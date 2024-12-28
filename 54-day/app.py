from flask import Flask

app = Flask(__name__)
# print(__name__)

@app.route("/") # -- decorator

def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye!</p>"

if __name__ == '__main__':
    app.run()



