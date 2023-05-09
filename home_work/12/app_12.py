from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def form_page():
    return render_template('form.html')


@app.route('/add', methods=['POST'])
def add_page():
    task = request.form.get('task_name')
    return f"Ви добавили задачу - {task}"


@app.route('/filter')
def filter_page():
    from_value = request.args.get('from')
    to_value = request.args.get('to')
    return f"Шукаємо в фапазоні  від {from_value} до {to_value}"


@app.route('/test', methods=["GET", "POST"])
def test_page():
    name = request.values.get('name')
    return f"Ви ввели ім'я {name}"


if __name__ == '__main__':
    app.run()
