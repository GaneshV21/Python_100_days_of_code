from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
blogs = Post()
@app.route('/blog')
def blog():

    return render_template("index.html", data=blogs.get_data())

@app.route('/blog/<int:num>')
def read_blog(num):
    blogs.num = num
    print(blogs.get_exact_data())
    return render_template("post.html",data = blogs.get_exact_data())


if __name__ == "__main__":
    app.run(debug=True)
