import json


def load_candidates_from_json(path: str) -> list:
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    # повертає одного кандидати по ID
    pass


def get_candidates_by_name(candidate_name):
    # Повертає кандидата по імені
    pass


def get_candidates_by_skill(skil_name):
    # Повертає кандидатів по навику
    pass


