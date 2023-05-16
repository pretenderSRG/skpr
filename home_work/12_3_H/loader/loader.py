from flask import Blueprint, render_template, request
import logging
from functions import load_posts, upload_posts
from config import UPLOAD_FOLDER, POST_PATH


logging.basicConfig(encoding='utf-8', filename='login.log', filemode='w',level=logging.INFO)

loader_blueprint = Blueprint('loader', __name__, template_folder='templates', url_prefix='/post/', static_folder='static')


@loader_blueprint.route('/form/')
def form():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=['POST'])
def upload():
    try:
        file = request.files.get('picture')
        filename = file.filename
        content = request.values.get('content')
        posts = load_posts()
        posts.append({
            "pic": f"{UPLOAD_FOLDER}/{filename}",
            "content": content
        })
        if filename.split('.')[-1] not in ('png', 'jpg', 'jpeg'):
            logging.info('Файл не являється зображенням')
        upload_posts(posts)
        file.save(f'{UPLOAD_FOLDER}/{filename}')
    except FileNotFoundError as e:
        logging.error('Помилка при загрузці файлу')
        return "<h1>Файл не знайдений</h1>"
    else:
        return render_template('post_uploaded.html', pic=f'../../{UPLOAD_FOLDER}/{filename}', content=content)
