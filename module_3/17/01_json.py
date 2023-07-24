import datetime
import decimal
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)

a1 = "hello world"
b1 = {"key": "value"}
c1 = [1, 2, 3]
# print(json.dumps(a1))
# print(json.dumps(b1))
# print(json.dumps(c1))

a1_json = json.dumps(a1)
b1_json = json.dumps(b1)
c1_json = json.dumps(c1)

print(json.loads(a1_json))
print(json.loads(b1_json)["key"])
print(json.loads(c1_json)[1])


a2 = datetime.datetime.now()
b2 = decimal.Decimal("3")
# print(json.dumps(a2))
# print(json.dumps(b2))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)


pedro = User(id=1, name="Pedro", age=40)
# json.dumps(pedro)




if __name__ == "__main__":
    app.run()
