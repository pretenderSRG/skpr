from flask import Flask, request, render_template


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024*1024


@app.route('/', methods=["GET", "POST"])
def page_form():
    return render_template('file_form.html')


@app.route('/upload', methods=["POST"])
def page_upload():
    ALLOWED_EXTENSION = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    picture = request.files["picture"]
    file_name = picture.filename
    extension = file_name.split('.')[-1]
    if extension in ALLOWED_EXTENSION:
        picture.save(f"./uploads/{file_name}")
        return f"<h1>Загружений файл <{file_name}></h1><p><a href='/'>на головну</a></p>"
    else:
        return f"Ти файлів <{extension}> не підтримуєтсья"


# @app.route('/upload/<file>')
# def show_file(file):
#     picture = request.files["picture"]





@app.errorhandler(413)
def page_not_found(e):
    return f"<h1>Файл занадто великий</h1><p>пошукайте менший : (</p><p></p><a href='/'>на головну</a>"


if __name__ == "__main__":
    app.run()
