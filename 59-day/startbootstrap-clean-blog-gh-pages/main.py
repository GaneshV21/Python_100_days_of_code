from flask import Flask,render_template
import requests
app = Flask(__name__)
api = "https://api.npoint.io/7446a0998c9172ddb49c"
response = requests.get(api).json()
@app.route('/')
def home():
    return render_template("index.html",data=response)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def post(id):
    for item in response:
        if item['id'] == id:
            return render_template("post.html",data=item)

if __name__ == "__main__":
    app.run(debug=True)