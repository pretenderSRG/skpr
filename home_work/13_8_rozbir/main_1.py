from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def page_index():
    return "It work"


@app.route('/posts')
def page_posts_show():
    return "I show all posts"


@app.route('/posts', methods=["POST"])
def page_posts_create():
    return "I create post"


@app.route('/post/1', methods=["GET"])
def page_post_get():
    return "I show one post"


@app.route('/post/1', methods=["PATCH"])
def page_post_patch():
    return "I refresh one post"


@app.route('/post/1', methods=["DELETE"])
def page_post_delete():
    return "I delete the post"


@app.route('/form', methods=['GET', 'POST'])
def page_form():
    if request.method == 'POST':
        var_name = request.values.get("name1")
        return f"Form get variable {var_name}"
    else:
        return "<form action='/form', method='post'>" \
               "<input type='text' name='name1'>" \
               "<input type='submit'>" \
               "</form>"


if __name__ == "__main__":
    app.run()