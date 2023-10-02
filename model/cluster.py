from typing import List

from difference_scores import DifferenceScores


class Cluster:
    entities: List[str]

    def __init__(self, entities: List[str] = None):
        if not entities:
            entities = []

        entities.sort()
        self.entities = entities

    def __len__(self):
        return len(self.entities)

    def __iter__(self):
        return self.entities.__iter__()

    def __getitem__(self, item):
        return self.entities[item]

    def __repr__(self):
        return self.entities.__str__()

    def __lt__(self, other):
        return self.entities < other.entities

    def add_entity(self, entity: str):
        self.entities.append(entity)
        self.entities.sort()

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def compute_cost(self, difference_scores: DifferenceScores):
        if len(self.entities) <= 1:
            return 0

        cost, num_scores = 0.0, len(self.entities)
        for i1, e1 in enumerate(self.entities):
            rem_entities = self.entities[i1+1:]
            for e2 in rem_entities:
                cost += difference_scores.get_score(e1, e2)
                num_scores += 1

        cost /= len(self.entities)
        return cost

    def sort(self):
        self.entities.sort()
