from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def get_json():
    data = {"name": "Alexs"}
    return jsonify(data)


if __name__ == "__main__":
    app.run()
# response = app.test_client().get('/')
# print(response.status_code)
# print(response.data)
