from flask import Flask, jsonify
from utils import search_by_id


app = Flask(__name__)


@app.route('/<int:itemid>')
def item_page(itemid):
    return jsonify(search_by_id(itemid))


if __name__ == '__main__':
    app.run(debug=True)