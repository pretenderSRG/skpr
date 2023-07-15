from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, desc, func
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
    # users = relationship("User", back_populates="group", overlaps="group")


def create_db():
    with app.app_context():
        db.create_all()


def add_users():
    group_01 = Group(id=1, name="Group #1")
    group_02 = Group(id=2, name="Group #2")

    users = [
        User(id=1, name="John", age=20, passport_number='123', group=group_01),
        User(id=2, name="Kate", age=22, passport_number='456', group=group_02),
        User(id=3, name="Arthur", age=23, passport_number='789', group=group_01),
        User(id=4, name="Maxim", age=20, passport_number='012', group=group_01),
        User(id=5, name="Lily", age=30, passport_number='345', group=group_02),
        User(id=6, name="Mary", age=27, passport_number='678', group=group_02)
    ]

    with app.app_context():
        db.session.add_all(users)
        db.session.commit()


def get_queries():
    with app.app_context():

        # SQL -> WHERE
        query1 = db.session.query(User).filter(User.name == "Mary")
        print(f"Запит {query1}")
        print(f"Результат {query1.first().name}")
        print(f"Результат 2 {query1.one()}")
        print("-------------")

        # SQL -> WHERE AND
        query2 = db.session.query(User).filter(User.id <= 5, User.age > 20)
        print(f"Запит {query2}")
        print(f"Результат {query2.all()}")
        print("-------------")

        # SQL -> LIKE
        query3 = db.session.query(User).filter(User.name.like("M%"))
        print(f"Запит {query3}")
        print(f"Результат {query3.all()}")
        print("-------------")

        # SQL -> WHERE OR
        query4 = db.session.query(User).filter(or_(User.id <= 5, User.age > 20))
        print(f"Запит {query4}")
        print(f"Результат {query4.all()}")
        print("-------------")

        # SQL -> IS NULL
        query5 = db.session.query(User).filter(User.name == None)
        print(f"Запит {query5}")
        print(f"Результат {query5.all()}")
        print("-------------")

        # SQL -> IN
        query6 = db.session.query(User).filter(User.id.in_([2, 5]))
        print(f"Запит {query6}")
        print(f"Результат {query6.all()}")
        print("-------------")

        # SQL -> BETWEEN
        query7 = db.session.query(User).filter(User.id.between(2, 5))
        print(f"Запит {query7}")
        print(f"Результат {query7.all()}")
        print("-------------")

        # SQL -> LIMIT
        query8 = db.session.query(User).limit(2)
        print(f"Запит {query8}")
        print(f"Результат {query8.all()}")
        print("-------------")

        # SQL -> LIMIT OFFSET
        query9 = db.session.query(User).limit(2).offset(2)
        print(f"Запит {query9}")
        print(f"Результат {query9.all()}")
        print("-------------")

        # SQL -> ORDER BY DESC
        query10 = db.session.query(User).order_by(desc(User.id))
        print(f"Запит {query10}")
        print(f"Результат {query10.all()}")
        print("-------------")

        # SQL -> JOIN
        query11 = db.session.query(User.name, Group.name).join(Group)
        print(f"Запит {query11}")
        print(f"Результат {query11.all()}")
        print("-------------")

        # SQL -> GROUP BY (scalar)
        query12 = db.session.query(func.count(User.id)).join(Group).filter(Group.id == 1).group_by(Group.id)
        print(f"Запит {query12}")
        print(f"Результат {query12.scalar()}")
        print("-------------")


if __name__ == "__main__":
    create_db()
    add_users()
    get_queries()
