from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def main_page():
    title = app.config.get('PROJECT_NAME')
    description = app.config.get('PROJECT_DESCRIPTION')
    return f"<h1>{title} ....{description}</h1>"


if __name__ == '__main__':
    app.run()