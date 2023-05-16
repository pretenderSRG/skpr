from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint
from config import UPLOAD_FOLDER


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route(f"/{UPLOAD_FOLDER}/<path:path>")
def static_dir(path):
    return send_from_directory(UPLOAD_FOLDER, path)


app.run(debug=True)

