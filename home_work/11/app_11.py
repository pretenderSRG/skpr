from flask import Flask, render_template
import logging
from configurate import PATH_TO_CANDIDATE_DATA
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)
logging.basicConfig(filename="basic.log")
app.config.update(
    DEBUG=True
)

candidates = load_candidates_from_json(PATH_TO_CANDIDATE_DATA)


@app.route('/')
def main_page():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def candidate_info(x):
    return render_template('single.html', candidate=get_candidate(x))


@app.route('/search/<candidate_name>')
def search_candidate(candidate_name):
    candidates_list = get_candidates_by_name(candidate_name)
    return render_template('search.html', count=len(candidates_list), candidates=candidates_list)


@app.route('/skill/<skill_name>')
def skills(skill_name):
    candidates_with_skill = get_candidates_by_skill(skill_name)
    return render_template('skill.html', count=len(candidates_with_skill), candidates=candidates_with_skill, skill=skill_name)


if __name__ == '__main__':
    app.run()
