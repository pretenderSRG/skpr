import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    __tamlename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


with app.app_context():
    db.drop_all()
    db.create_all()

    user_john = User(id=1, name="John", age=30)
    user_kate = User(id=2, name="Kate", age=32)
    db.session.add(user_kate)
    db.session.add(user_john)

    db.session.commit()


@app.route("/users/first")
def get_first_user():
    user = User.query.first()
    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })


@app.route("/users/count")
def get_count():
    user_count = User.query.count()

    return json.dumps(user_count)


@app.route("/users")
def get_users():
    users_list = User.query.all()
    user_response = []

    for user in users_list:
        user_response.append({
            "id": user.id,
            "name": user.name,
            "age": user.age})

    return json.dumps(user_response)


@app.route("/users/<int:sid>")
def get_user(sid: int):
    user = User.query.get(sid)
    if user is None:
        return "User not found"

    return json.dumps({
        "id": user.id,
        "name": user.name,
        "age": user.age,
    })


@app.route("/users/add/<name>/<int:age>")
def add_user(name: str, age: int):
    try:
        with app.app_context():
            user = User(name=name, age=age)
            db.session.add(user)
            db.session.commit()

        return "User added to base"
    except Exception as e:
        return f"{e} - Somethings wrong ("


if __name__ == "__main__":
    app.run(debug=True)
