from flask import Flask
import json


def load_data_from_json(filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    return data


def add_candidate(can):
    return f"<Ім'я кандидата - {can.get('name')}\
    <br>Посада кандидата - {can.get('position')}\
    <br>Список навиків: {can.get('skills')}"


app = Flask(__name__)

candidates = load_data_from_json("candidates.json")


@app.route('/')
def index():
    str_candidates = "<pre><br>"
    for candidate in candidates:
        str_candidates += add_candidate(candidate)
    str_candidates += "</pre>"
    return str_candidates


@app.route('/skills/<x>')
def candidate(x):
    str_candidate = "</pre>\n"
    for candidate in candidates:
        candidates_list = candidate.get("skills").lower().split(", ")
        if x.lower() in candidates_list:
            str_candidate += add_candidate(candidate) + "<br>"
    str_candidate +="</pre>"
    return str_candidate


@app.route('/candidate/<int:x>')
def skills(x):
    str_candidate = "</pre>\n"
    for candidate in candidates:
        if candidate.get("id") == x:
            str_candidate +=f"<img src=\"{candidate.get('picture')}\"><br>" + add_candidate(candidate)
            break
    str_candidate += "</pre>"
    return str_candidate


if __name__ == "__main__":
    app.run()

