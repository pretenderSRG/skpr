from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age > 18"))
    group_id = db.Column(db.Integer)


with app.app_context():
    db.create_all()

    users = [
            User(id=1, name="John", age=20, passport_number='123'),
            User(id=2, name="Kate", age=22, passport_number='456'),
            User(id=3, name="Arthur", age=23, passport_number='789'),
            User(id=4, name="Maxim", age=20, passport_number='012'),
            User(id=5, name="Lily", age=30, passport_number='345'),
            User(id=6, name="Mary", age=27, passport_number='678')
        ]
    db.session.add_all(users)
    db.session.commit()

    user = User.query.get(2)
    print(user.name)
    user.name = "Sub-Zero"
    db.session.add(user)
    db.session.commit()

    user = User.query.get(2)
    print(user.name)


if __name__ == '__main__':
    app.run()