from flask import Flask

app = Flask(__name__)

@app.route("/") # -- decorator

def hello_world():
    return "<p>Hello,World!</p>"

#Differnet routes using the app.route decorator

@app.route("/bye")
def bye():
    return "<p>Bye!</p>"

# creating variable paths and converting the path to a apecified data type

# @app.route("/username/<name>/1")  # - hello Ganesh12!
# @app.route("/username/<path:name>")  # - hello ganesh/112!
@app.route("/username/<name>/<int:num>") # - hello ganesh12 you are 21 years old!

def greet(name,num):
    return f"hello {name + '12'} you are {num} years old!"

@app.route('/render')
def render_html():
    return '<h1 style = "text-align:center"> hello </h1>'\
            '<p>This is Paragraph</p>'\
            '<img src="data:image/jpeg;base64,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" width= 200>'



#decorator task:
def make_bold(function):
    def wrapper1(name):
        return f'<b>{function(name)}</b>'
    return wrapper1

def make_emphasis(function):
    def wrapper2(name):
        return f'<em>{function(name)}</em>'
    return wrapper2

def make_underlined(function):
    def wrapper3(name):
        return f'<u>{function(name)}</u>'
    return wrapper3




@app.route('/user_bold/<name>')
@make_bold
def greets_bold(name):
    return f"hello {name}"


@app.route('/user_emphasis/<name>')
@make_emphasis
def greets_emphasis(name):
    return f"hello {name}"

@app.route('/user_underlined/<name>')
@make_underlined
def greets_underlined(name):
    return f"hello {name}"



# Advanced Python Decorator Functions
class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post")

new_user = User("Ganesh")
create_blog_post(new_user)


if __name__ == '__main__':
    # run the app in debug mode to auto-reload
    app.run(debug=True)




