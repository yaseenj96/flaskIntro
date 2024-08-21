
from flask import Flask

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

##Logging Decorator exercise - using *args
def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


app = Flask(__name__)
@app.route("/") ## Python decorator - Wraps another function
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1> '
            '<p>This is a paragraph</p>'
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHNod2hnd3BqemNjOThpeHh2a2FxdndmZnV3cjN4cG41NTc1Y21uNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1BXa2alBjrCXC/giphy.webp" width=200>')

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"

## Serve up app and run within PyCharm - Check that this is the current file where
## it is being run
if __name__ == "__main__":
    app.run(debug=True)


## Need to export FLASK_APP=hello.py
## Then: flask run