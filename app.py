from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return '<h1 style="text-align:center">Hello, World!</h1>'\
#            '<p>This is a paragraphph</p>' \
#             '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWRiM3kzYnB1OGIyY3RtMXkxd2h4NG54NzZndmlnZzVxYXF2NjRwYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YRVP7mapl24G6RNkwJ/giphy.gif" width=200px>'

# @app.route("/username/<name>")
# def greet(name):
#     return  f"Hello there, {name}"

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye!"



if __name__ == "__main__":
    app.run(debug=True)

