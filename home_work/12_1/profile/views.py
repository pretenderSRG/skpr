from flask import Blueprint

profile_blueprint = Blueprint('profile', __name__)


@profile_blueprint.route('/profile/<int:user_id>')
def profile_page(user_id):
    return f"<h1>Я сторінка <mark>{user_id}</mark></h1>"
