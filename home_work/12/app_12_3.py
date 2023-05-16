from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)


@app.route('/uploads/<path:path>')
def static_dir(path):
    return send_from_directory('uploads', path)


if __name__ == '__main__':
    app.run()
