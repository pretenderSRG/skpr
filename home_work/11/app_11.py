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
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<x>')
def candidate_info(x):
    for candidate in candidates:
        if x in candidate.values():
            return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidate(candidate_name):
    candidates_list = []
    for candidate in candidates:
        search_candidate = candidate.get("name")
        if search_candidate.split()[0] == candidate_name:
            candidates_list.append(search_candidate)

    return render_template('search.html', count=len(candidates_list), candidates=candidates_list)


@app.route('/skill/<skill_name>')
def skills(skill_name):
    candidates_with_skill = []
    for candidate in candidates:
        skills = candidate.get("skills").lower().split(', ')
        if skill_name.lower() in skills:
            candidates_with_skill.append(candidate.get('name'))
    return render_template('skill.html', count=len(candidates_with_skill), candidates=candidates_with_skill, skill=skill_name)


if __name__ == '__main__':
    app.run()
