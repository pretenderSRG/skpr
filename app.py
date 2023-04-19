from flask import Flask, render_template, request

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD=True, FLASK_DEBUG=True)


@app.route('/')
def handler():
    word = request.args.get('word')
    dictionary = {'cat': 'кіт', 'dog': 'пес', 'word': 'слово', 'eye': 'око'}
    translation = dictionary.get(word, 'word is not found')
    return render_template("form.html", word=word, translation=translation)


if __name__ == '__main__':
    app.run()