from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age > 18"))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")


with app.app_context():
    db.create_all()

group_01 = Group(id=1, name="Group #1")
group_02 = Group(id=2, name="Group #2")

user_01 = User(id=1, name="John", age=20, passport_number='123', group=group_01)
user_02 = User(id=2, name="Kate", age=22, passport_number='456', group=group_02)
user_03 = User(id=3, name="Arthur", age=23, passport_number='789', group=group_01)
user_04 = User(id=4, name="Maxim", age=20, passport_number='012', group=group_01)
user_05 = User(id=5, name="Lily", age=30, passport_number='345', group=group_02)
user_06 = User(id=6, name="Mary", age=27, passport_number='678', group=group_02)


with db.session.begin():
    try:
        db.session.add(user_01)
        db.session.add(user_02)

        nested = db.session.begin_nested()

        try:
            db.session.add(user_03)
            db.session.add(user_04)
            # raise Exception("Database error")
        except Exception as e:
            print(f"Error {e}")
            nested.rollback()
        # raise Exception("Main database error")
    except Exception as e:
        print(f"Error {e}")
        db.session.rollback()

print(User.query.all())

if __name__ == "__main__":
    app.run()

