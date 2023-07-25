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


#  create table 'user'
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.String(50))
    email = db.Column(db.String(50))
    role = db.Column(db.String(50))
    phone = db.Column(db.String(50))


#  create table 'order'
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


#  create table 'offer'
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


#  add data to db from file
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
        if isinstance(data, list):
            for user in data:
                new_user = User(
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    age=user['age'],
                    email=user['email'],
                    role=user['role'],
                    phone=user['phone']
                )
                db.session.add(new_user)
        else:
            new_user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                age=data['age'],
                email=data['email'],
                role=data['role'],
                phone=data['phone']
            )
            db.session.add(new_user)
        db.session.commit()

        return "All users was adding", 200


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user_id_page(uid):
    if request.method == "GET":
        user = db.session.query(User).get(uid)
        if user is None:
            return "User not found", 404
        else:
            user_json = {

                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'age': user.age,
                'email': user.email,
                'role': user.role,
                'phone': user.phone
            }
            return jsonify(user_json), 200

    elif request.method == "PUT":

        input_user = request.get_json()
        user = db.session.query(User).get(uid)
        if user is None:
            return "User not exist, try again"
        user.id = input_user['id']
        user.first_name = input_user['first_name']
        user.last_name = input_user['last_name']
        user.age = input_user['age']
        user.email = input_user['email']
        user.role = input_user['role']
        user.role = input_user['role']
        user.phone = input_user['phone']

        with db.session.begin():
            db.session.add(user)
        return "User data was changed", 200

    elif request.method == "DELETE":
        user = db.session.query(User).get(uid)
        db.session.delete(user)
        db.session.commit()
        return "User was deleted", 200


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
        if isinstance(data, list):
            for order in data:
                new_order = Order(
                    name=order['name'],
                    description=order['description'],
                    start_date=datetime.strptime(order['start_date'], "%m/%d/%Y"),
                    end_date=datetime.strptime(order['end_date'], "%m/%d/%Y"),
                    address=order['address'],
                    price=order['price'],
                    customer_id=order['customer_id'],
                    executor_id=order['executor_id']
                )
                db.session.add(new_order)
                db.session.commit()
            return "All orders was added", 200
        else:
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
            db.session.add(new_order)
            db.session.commit()
        return "Order was added", 200


@app.route('/orders/<int:oid>', methods=['GET', 'PUT', 'DELETE'])
def order_id_page(oid):
    if request.method == 'GET':
        order = db.session.query(Order).get(oid)
        if order is None:
            return f"Order not found", 201
        else:
            order_json = {
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
            return jsonify(order_json)

    elif request.method == 'PUT':
        input_order = request.get_json()
        order = db.session.query(Order).get(oid)
        if order is None:
            return "Order not exist, try again"

        order.id = input_order['id']
        order.name = input_order['name']
        order.description = input_order['description']
        order.start_date = datetime.strptime(input_order['start_date'], "%m/%d/%Y")
        order.end_date = datetime.strptime(input_order['end_date'], "%m/%d/%Y")
        order.address = input_order['address']
        order.price = input_order['price']
        order.customer_id = input_order['customer_id']
        order.executor_id = input_order['executor_id']

        db.session.add(order)
        db.session.commit()
        return "Order data was updated", 200

    elif request.method == 'DELETE':
        order = db.session.query(Order).get(oid)
        db.session.delete(order)
        db.session.commit()

        return "Order was deleted", 200


@app.route('/offers', methods=['GET', 'POST'])
def offers_index():
    if request.method == 'GET':
        all_offers = []
        for offer in db.session.query(Offer).all():
            all_offers.append({
                'id': offer.id,
                'order_id': offer.order_id,
                'executor_id': offer.executor_id
            })
        return jsonify(all_offers)

    elif request.method == "POST":
        data = request.get_json()
        if isinstance(data, list):
            for offer in data:
                new_offer = Offer(
                    order_id=offer["order_id"],
                    executor_id=offer["executor_id"]
                )
                db.session.add(new_offer)
            db.session.commit()
            return "All offers was added", 200
        else:
            new_offer = Offer(
                order_id=data["order_id"],
                executor_id=data["executor_id"]
            )
            db.session.add(new_offer)
            db.session.commit()
            return "Offer will added", 200


@app.route("/offers/<int:oid>", methods=["GET", "PUT", "DELETE"])
def offer_id_page(oid):
    if request.method == "GET":
        offer = db.session.query(Offer).get(oid)
        if offer is None:
            return "Offer not exist"
        else:
            offer_json = {
                'id': offer.id,
                'order_id': offer.order_id,
                'executor_id': offer.executor_id
            }
        return jsonify(offer_json)

    elif request.method == "PUT":
        input_data = request.get_json()
        offer = db.session.query(Offer).get(oid)
        if offer is None:
            return "Offer not exist, try again", 404

        offer.id = input_data["id"]
        offer.order_id = input_data["order_id"]
        offer.executor_id = input_data["executor_id"]

        db.session.add(offer)
        db.session.commit()
        return 'Offer was updated', 200

    elif request.method == "DELETE":
        offer = db.session.query(Offer).get(oid)
        db.session.delete(offer)
        db.session.commit()

        return "Offer was deleted", 200



@app.errorhandler(404)
def page_not_found(e):
    return f"Not Found {e}", 404


if __name__ == '__main__':
    main()
