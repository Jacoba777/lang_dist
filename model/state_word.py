from typing import List

from model.state import State, _lists_start_same, COST_INSERT, COST_DELETE, _States, _starts_with
from model.syllable import Syllable, syllable_distance


class SyllableListState(State):

    def __repr__(self):
        return f"<SyllableListState {self.path} | {self.cost}>"

    def get_replacement(self, goal: List[Syllable]):
        curr: List[Syllable] = self.get_current_value()
        if _lists_start_same(curr, goal):
            return None

        for i, syllable_curr in enumerate(curr):
            syllable_goal = goal[i]
            if syllable_curr != syllable_goal:
                new_list = curr[:i] + [syllable_goal] + curr[i+1:]
                new_path = self.path + [new_list]
                replace_cost = syllable_distance(syllable_curr, syllable_goal)
                return SyllableListState(new_path, self.cost + replace_cost)

    def get_insertion(self, goal: List[Syllable]):
        curr: List[Syllable] = self.get_current_value()
        if _starts_with(curr, goal):
            return None

        for i, syllable_goal in enumerate(goal):
            if i > len(curr) - 1 or curr[i] != syllable_goal:
                new_list = curr[:i] + [syllable_goal] + curr[i:]
                new_path = self.path + [new_list]
                return SyllableListState(new_path, self.cost + COST_INSERT)

    def get_deletion(self, goal: List[Syllable]):
        curr: List[Syllable] = self.get_current_value()
        if _starts_with(goal, curr):
            return None

        for i, syllable_curr in enumerate(curr):
            if i > len(goal) - 1 or goal[i] != syllable_curr:
                new_list = curr[:i] + curr[i+1:]
                new_path = self.path + [new_list]
                return SyllableListState(new_path, self.cost + COST_DELETE)

    def get_choice_states(self, goal: List[Syllable]):
        replace = self.get_replacement(goal)
        insert = self.get_insertion(goal)
        delete = self.get_deletion(goal)

        states = [replace, insert, delete]
        return [s for s in states if s]


def get_syllable_list_dist(start: List[Syllable], goal: List[Syllable], best: SyllableListState | None = None, debug=False):
    if start == goal:
        return 0.0

    initial_state = SyllableListState([start], 0)
    states = _States([initial_state])

    while not states.is_empty() and (not best or states.get_cheapest() < best):
        cheapest: SyllableListState = states.get_cheapest()
        new_states = cheapest.get_choice_states(goal)

        if debug:
            print(f'new_states from {cheapest}: {new_states}')

        for state in new_states:
            existing_state = states.get_state(state.get_current_value())
            if state.get_current_value() == goal and (not best or best > state):
                best = state
            elif existing_state and existing_state.cost > state.cost:
                states.remove(existing_state)
                states.add(state)
            elif not existing_state:
                states.add(state)
        states.remove(cheapest)

    normalized_cost = best.cost / max(len(start), len(goal))

    if debug:
        print('best path:', best)
        print(f'{normalized_cost=}')

    return normalized_cost
