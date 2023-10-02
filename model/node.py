from __future__ import annotations

from typing import List
from model.difference_scores import DifferenceScores


class Node:
    def __init__(self, entities: List[str | Node] = None):
        if not entities:
            entities = []
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

    def add_entity(self, entity: str | Node):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def get_flat_entities(self) -> List[str]:
        flattened_entities = [e for e in self.entities if type(e) == str]
        for e in self.entities:
            if type(e) == Node:
                flattened_entities.extend(e.get_flat_entities())
        return flattened_entities

    def compute_cost_max_only(self, difference_scores: DifferenceScores, print_most_cost=False):
        flat_entities = self.get_flat_entities()
        if len(flat_entities) <= 1:
            return 0

        max_cost = 0.0
        max_e1, max_e2 = None, None
        for i1, e1 in enumerate(flat_entities):
            rem_entities = flat_entities[i1+1:]
            for e2 in rem_entities:
                cost = difference_scores.get_score(e1, e2)
                if cost > max_cost:
                    max_e1, max_e2 = e1, e2
                    max_cost = cost
        if print_most_cost:
            print(f"Most different pair: ({max_e1}, {max_e2}); cost={max_cost}")
        return max_cost

    def compute_union_cost(self, difference_scores: DifferenceScores, other: str | Node):
        cost = 0.0

        if type(other) == Node:
            for e in self.entities:
                cost += other.compute_union_cost(difference_scores, e)
        else:
            for e in self.entities:
                if type(e) == Node:
                    cost += e.compute_union_cost(difference_scores, other)
                else:
                    cost += difference_scores.get_score(e, other)

        return cost / len(self.entities)

    def compute_cost(self, difference_scores: DifferenceScores):
        cost = 0.0
        pairs = 0
        for i1, e1 in enumerate(self.entities):
            for e2 in self.entities[i1+1:]:
                pairs += 1
                if type(e1) == Node:
                    cost += e1.compute_union_cost(difference_scores, e2)
                elif type(e2) == Node:
                    cost += e2.compute_union_cost(difference_scores, e1)
                else:
                    cost += difference_scores.get_score(e1, e2)
        return cost / pairs

    def pprint(self, lang_dists: DifferenceScores, indents=0):
        cost = self.compute_cost(lang_dists)
        print("\t" * (indents-1) + f"[NODE {(1-cost)*100:.1f}% ({2744*(1-cost):.0f}px)]")
        for e in self.entities:
            if type(e) == str:
                print("\t"*indents + e)
            else:
                e.pprint(lang_dists, indents=indents+1)
