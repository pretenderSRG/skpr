from flask import Flask, jsonify
from utils.utils import Car


app = Flask(__name__)
car = Car('cars_1.db')


@app.route('/car/<model>')
def main_page(model):
    find_model = car.find_by_model(model.lower())
    return jsonify(find_model)


@app.route('/car/<int:start>/to/<int:finish>')
def range_page(start, finish):
    result = car.find_range(start, finish)
    return jsonify(result)


if __name__ == '__main__':
    app.run()