import json


__data = []


def load_candidates_from_json(path: str) -> list:
    global __data
    with open(path, encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    # повертає одного кандидати по ID
    for candidate in __data:
        if candidate_id == candidate.get('id'):
            return candidate
    return {"not_found": "candidate not found"}


def get_candidates_by_name(candidate_name):
    # Повертає кандидата по імені
    return [candidate for candidate in __data if candidate_name.lower() in candidate.get("name").lower()]


def get_candidates_by_skill(skill_name):
    # Повертає кандидатів по навику
    candidates_with_skill = []
    for candidate in __data:
        skills = candidate.get("skills").lower().split(', ')
        if skill_name.lower() in skills:
            candidates_with_skill.append(candidate)
    return candidates_with_skill



