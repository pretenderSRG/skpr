from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

db = SQLAlchemy(app)


#  create User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)


#  ----create Schema for User----
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()


#  ----make dump in dict----
# user = User(id=1, name="John", age=30)
# user_schema = UserSchema()
# result = user_schema.dump(user)
# print(type(result))
# print(result)
# print(result["name"])

#  ----make dump in string----
# user = User(id=1, name="John", age=30)
# user_schema = UserSchema()
# result = user_schema.dumps(user)
# print(type(result))
# print(result)

#  ----make dump list----
# u1 = User(id=1, name="Jhon", age=30)
# u2 = User(id=2, name="Kate", age=20)
# u3 = User(id=3, name="Mary", age=18)
# u4 = User(id=4, name="Max", age=41)
# user_schema = UserSchema(many=True)
# result1 = user_schema.dump([u1, u2, u3, u4])
# result2 = user_schema.dumps([u1, u2, u3, u4])
# print(result1)
# print(result2)

# ----make deserialize----
user_json = '{"name": "John", "age": 30}'
user_schema = UserSchema()

user_dict = user_schema.loads(user_json)
user = User(**user_dict)
print(user.age)
print(user.name)


if __name__ == '__main__':
    app.run(debug=True)
