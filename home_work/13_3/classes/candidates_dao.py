import json
from classes.candidate import Candidate


class CandidateDAO:
    __PATH_TO_CANDIDATES = "candidates.json"

    def __init__(self):
        self.__candidates = self._load_data()

    @classmethod
    def _load_data(cls):
        try:
            candidates = []
            with open(cls.__PATH_TO_CANDIDATES, encoding="utf-8") as file:
                candidates_data = json.load(file)
                for candidate in candidates_data:
                    candidates.append(Candidate(
                        candidate['id'],
                        candidate['name'],
                        candidate['position'],
                        candidate['skills'],
                        candidate['picture']
                    ))
        except FileNotFoundError:
            candidates = []
        return candidates

    def get_all_candidates(self):
        return self.__candidates

    def get_by_skill(self, skill: str) -> list:
        skilled_candidates = []
        skill = skill.lower()
        for candidate in self.__candidates:
            candidate_skills = candidate.skills.lower().split(", ")
            if skill in candidate_skills:
                skilled_candidates.append(candidate)
        return skilled_candidates

    def get_by_id(self, uid):
        for candidate in self.__candidates:
            if candidate.id == uid:
                return candidate

