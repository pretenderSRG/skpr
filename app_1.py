from flask import Flask


app = Flask(__name__)


@app.route('/users/<int:uid>')
def profile(uid):
    print(type(uid))
    return f"<h1>Profile {uid}</h1>"


@app.route('/catalog/items/<itemid>')
def product(itemid):
    return f"<h1>Product {itemid}</h1>"


app.run()