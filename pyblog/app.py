from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Mehedi',
        'title': 'Beautiful nodejs',
        'content': 'Node is really awesome for making application and rest api',
        'date_posted': 'June 20, 2019'
    },
    {
        'author': 'Masum',
        'title': 'Beautiful python',
        'content': 'Python is really awesome for making application and rest api',
        'date_posted': 'June 21, 2019'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == '__main__':
    app.run(debug=True)
