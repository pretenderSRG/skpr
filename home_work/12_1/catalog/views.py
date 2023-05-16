from flask import Blueprint, render_template


catalog_blueprint = Blueprint('catalog', __name__, template_folder='templates')


@catalog_blueprint.route('/')
def catalog_page():
    return render_template('main.html')


@catalog_blueprint.route('/<cat>')
def category_page(cat):
    return render_template('category.html', category=cat)


@catalog_blueprint.route('/<cat>/<int:item>')
def item_page(item, cat):
    return render_template('item.html', category=cat, item=item)

