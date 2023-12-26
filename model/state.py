from typing import List

from model.phone import Phone, get_phone_distance

COST_INSERT = 1.0
COST_DELETE = 1.0
COST_REPLACE = 2.0


class State:
    def __init__(self, path: List, cost: float):
        self.path = path
        self.cost = cost

    def get_current_value(self):
        return self.path[-1]

    def get_choice_states(self, goal) -> List:
        pass

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"<State {self.path} | {self.cost}>"


class _States:
    def __init__(self, states=None):
        self._states = states if states else []

    def add(self, state):
        self._states.append(state)

    def remove(self, state):
        self._states.remove(state)

    def is_empty(self):
        return len(self._states) == 0

    def get_cheapest(self):
        return min(self._states, key=lambda x: x.cost)

    def get_state(self, current_value):
        state_matches = [s for s in self._states if s.get_current_value() == current_value]
        if len(state_matches) > 1:
            raise ValueError(f'Duplicate state detected for {current_value}')
        elif len(state_matches) == 0:
            return None
        else:
            return state_matches[0]

    def __repr__(self):
        return f'{self._states}'


class PhoneListState(State):

    def __repr__(self):
        return f"<PhoneListState {self.path} | {self.cost}>"

    def get_replacement(self, goal: List[Phone]):
        curr: List[Phone] = self.get_current_value()
        if _lists_start_same(curr, goal):
            return None

        for i, phone_curr in enumerate(curr):
            phone_goal = goal[i]
            if phone_curr != phone_goal:
                new_phone_list = curr[:i] + [phone_goal] + curr[i+1:]
                new_path = self.path + [new_phone_list]
                replace_cost = get_phone_distance(phone_curr, phone_goal)
                return PhoneListState(new_path, self.cost + replace_cost)

    def get_insertion(self, goal: List[Phone]):
        curr: List[Phone] = self.get_current_value()
        if _starts_with(curr, goal):
            return None

        for i, phone_goal in enumerate(goal):
            if i > len(curr) - 1 or curr[i] != phone_goal:
                new_phone_list = curr[:i] + [phone_goal] + curr[i:]
                new_path = self.path + [new_phone_list]
                return PhoneListState(new_path, self.cost + COST_INSERT)

    def get_deletion(self, goal: List[Phone]):
        curr: List[Phone] = self.get_current_value()
        if _starts_with(goal, curr):
            return None

        for i, phone_curr in enumerate(curr):
            if i > len(goal) - 1 or goal[i] != phone_curr:
                new_phone_list = curr[:i] + curr[i+1:]
                new_path = self.path + [new_phone_list]
                return PhoneListState(new_path, self.cost + COST_DELETE)

    def get_choice_states(self, goal: List[Phone]):
        replace = self.get_replacement(goal)
        insert = self.get_insertion(goal)
        delete = self.get_deletion(goal)

        states = [replace, insert, delete]
        return [s for s in states if s]


def _lists_start_same(l1: List, l2: List):
    if len(l1) < len(l2):
        l1, l2 = l2, l1
    shorter_len = len(l2)
    return l1[:shorter_len] == l2


def _starts_with(list: List, prefix: List):
    return prefix == list[:len(prefix)]


def get_phone_list_dist(start: List[Phone], goal: List[Phone], best: PhoneListState | None = None, debug=False):
    if start == goal:
        return 0.0

    initial_state = PhoneListState([start], 0)
    states = _States([initial_state])

    while not states.is_empty() and (not best or states.get_cheapest() < best):
        cheapest: PhoneListState = states.get_cheapest()
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
