from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from sqlalchemy.orm import relationship
from data import users, orders, offers
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JSON_AS_ASCII"] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.String(50))
    email = db.Column(db.String(50))
    role = db.Column(db.String(50))
    phone = db.Column(db.String(50))


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(255))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    orders = relationship("Order")
    users = relationship("User")


def main():
    with app.app_context():
        db.create_all()
        insert_data()
        app.run(debug=True)


def insert_data():
    new_users = []

    for user in users:
        new_users.append(
            User(
                id=user['id'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                age=user['age'],
                email=user['email'],
                role=user['role'],
                phone=user['phone']
            )
        )

    new_orders = []

    for order in orders:
        new_orders.append(
            Order(
                id=order['id'],
                name=order['name'],
                description=order['description'],
                start_date=datetime.strptime(order['start_date'], "%m/%d/%Y"),
                end_date=datetime.strptime(order['end_date'], "%m/%d/%Y"),
                address=order['address'],
                price=order['price'],
                customer_id=order['customer_id'],
                executor_id=order['executor_id'],

            )
        )

    new_offers = []
    for offer in offers:
        new_offers.append(
            Offer(
                id=offer['id'],
                order_id=offer['order_id'],
                executor_id=offer['executor_id']
            )
        )

    with db.session.begin():
        db.session.add_all(new_orders)
        db.session.add_all(new_users)
        db.session.add_all(new_offers)


@app.route('/users', methods=['GET', 'POST'])
def users_index():
    if request.method == 'GET':
        all_users = []
        for user in db.session.query(User).all():
            all_users.append(
                {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'age': user.age,
                    'email': user.email,
                    'role': user.role,
                    'phone': user.phone
                }
            )
        return jsonify(all_users)

    elif request.method == 'POST':
        data = request.get_json()
        new_user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            age=data['age'],
            email=data['email'],
            role=data['role'],
            phone=data['phone']
        )
        with db.session.begin():
            db.session.add(new_user)


@app.route('/orders', methods=['GET', 'POST'])
def orders_index():
    if request.method == 'GET':
        data = []
        for order in db.session.query(Order).all():
            data.append(
                {
                    'id': order.id,
                    'name': order.name,
                    'description': order.description,
                    'start_date': order.start_date,
                    'end_date': order.end_date,
                    'address': order.address,
                    'price': order.price,
                    'customer_id': order.customer_id,
                    'executor_id': order.executor_id
                }
            )
        return jsonify(data)

    elif request.method == 'POST':
        data = request.get_json()
        new_order = Order(
            name=data['name'],
            description=data['description'],
            start_date=datetime.strptime(data['start_date'], "%m/%d/%Y"),
            end_date=datetime.strptime(data['end_date'], "%m/%d/%Y"),
            address=data['address'],
            price=data['price'],
            customer_id=data['customer_id'],
            executor_id=data['executor_id']
        )
        with db.session.begin():
            db.session.add(new_order)

if __name__ == '__main__':
    main()
