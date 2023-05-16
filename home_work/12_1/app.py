from flask import Flask, request, render_template
from catalog.views import catalog_blueprint
from profile.views import profile_blueprint


app = Flask(__name__)

app.register_blueprint(catalog_blueprint, url_prefix='/catalog')
app.register_blueprint(profile_blueprint)


if __name__ == '__main__':
    app.run()
