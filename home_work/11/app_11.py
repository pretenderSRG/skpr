from flask import Flask, render_template
from configurate import PATH_TO_CANDIDATE_DATA
from utils import load_candidates_from_json


app = Flask(__name__)
app.config.update(
    DEBUG=True
)

candidates = load_candidates_from_json(PATH_TO_CANDIDATE_DATA)


@app.route('/')
def main_page():
    candidate_str = '<h1>All candidates</h1>'
    for candidate in candidates:
        candidate_name = candidate.get('name')
        candidate_str += f"<p><a href='/candidate/{candidate_name}'>{candidate_name}</a></p>"
    return candidate_str


@app.route('/candidate/<x>')
def candidate_info(x):
    for candidate in candidates:
        if x in candidate.values():
            return render_template('single.html', candidate=candidate)


if __name__ == '__main__':
    app.run()
