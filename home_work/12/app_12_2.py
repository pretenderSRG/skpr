from flask import Flask, request, render_template


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024*1024


@app.route('/')
def page_form():
    return render_template('file_form.html')


@app.route('/upload', methods=['POST'])
def page_upload():
    ALLOWED_EXTENSION = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    picture = request.files.get('picture')
    filename = picture.filename
    extension = filename.split('.')[-1]
    if extension in ALLOWED_EXTENSION:
        picture.save(f"./uploads/{filename}")
        return f"<h1>Загружений файл <{filename}></h1><p><a href='/'>на головну</a></p>"
    else:
        return f"Ти файлів <{extension}> не підтримуєтсья"


@app.errorhandler(413)
def page_not_found(e):
    return f"<h1>Файл занадто великий</h1><p>пошукайте менший : (</p><p></p><a href='/'>на головну</a>"


if __name__ == "__main__":
    app.run()
