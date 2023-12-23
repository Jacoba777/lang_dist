from typing import List

from model.word import Word
from token_distance import token_distance

COST_INSERT = 1.0
COST_DELETE = 1.0
COST_REPLACE = 2.0


class _State:
    def __init__(self, path: List[Word], cost: float):
        self.path = path
        self.cost = cost

    def get_current_word(self):
        return self.path[-1]

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"<State {self.path} | {self.cost}>"


class _States:
    def __init__(self, states=None):
        self._states: List[_State] = states if states else []

    def add(self, state: _State):
        self._states.append(state)

    def remove(self, state: _State):
        self._states.remove(state)

    def is_empty(self):
        return len(self._states) == 0

    def get_cheapest(self):
        return min(self._states, key=lambda x: x.cost)

    def get_state(self, word: Word):
        state_matches = [s for s in self._states if s.get_current_word() == word]
        if len(state_matches) > 1:
            raise ValueError(f'Duplicate state detected for {word}')
        elif len(state_matches) == 0:
            return None
        else:
            return state_matches[0]

    def __repr__(self):
        return f'{self._states}'


def _make_replacement(state: _State, w_goal: Word):
    w_curr = state.get_current_word()
    if w_curr.starts_with(w_goal) or w_goal.starts_with(w_curr):
        return None

    for i, token in enumerate(w_curr):
        goal_token = w_goal.tokens[i]
        if token != goal_token:
            new_word = TokenizedWord(tokens=w_curr.tokens[:i] + [goal_token] + w_curr.tokens[i+1:])
            new_path = state.path + [new_word]
            replace_cost = token_distance(token, goal_token)
            return _State(new_path, state.cost + replace_cost)


def _make_insertion(state: _State, w_goal: Word):
    w_curr = state.get_current_word()
    if w_curr.starts_with(w_goal):
        return None

    for i, token in enumerate(w_goal):
        if i > len(w_curr)-1 or w_curr.tokens[i] != token:
            new_word = TokenizedWord(tokens=w_curr.tokens[:i] + [token] + w_curr.tokens[i:])
            new_path = state.path + [new_word]
            return _State(new_path, state.cost + COST_INSERT)


def _make_deletion(state: _State, w_goal: Word):
    w_curr = state.get_current_word()
    if w_goal.starts_with(w_curr):
        return None

    for i, token in enumerate(w_curr):
        if i > len(w_goal)-1 or w_goal.tokens[i] != token:
            new_word = Word(tokens=w_curr.tokens[:i] + w_curr.tokens[i+1:])
            new_path = state.path + [new_word]
            return _State(new_path, state.cost + COST_DELETE)


def _get_choice_states(state: _State, w: Word):
    replace = _make_replacement(state, w)
    insert = _make_insertion(state, w)
    delete = _make_deletion(state, w)

    states = [replace, insert, delete]
    return [s for s in states if s]


def weighted_lev(w1: Word, w2: Word, best: _State | None = None, debug=False):
    if w1 == w2:
        return 0.0

    initial_state = _State([w1], 0)
    states = _States([initial_state])

    while not states.is_empty() and (not best or states.get_cheapest() < best):
        cheapest = states.get_cheapest()
        new_states = _get_choice_states(cheapest, w2)

        if debug:
            print(f'new_states from {cheapest}: {new_states}')

        for state in new_states:
            existing_state = states.get_state(state.get_current_word())
            if state.get_current_word() == w2 and (not best or best > state):
                best = state
            elif existing_state and existing_state.cost > state.cost:
                states.remove(existing_state)
                states.add(state)
            elif not existing_state:
                states.add(state)
        states.remove(cheapest)

    normalized_cost = best.cost / max(len(w1), len(w2))

    if debug:
        print('best path:', best)
        print(f'{normalized_cost=}')

    return normalized_cost


if __name__ == '__main__':
    w1 = Word(ipa='aɪ')
    w2 = Word(ipa='ˈi.o')
    weighted_lev(w1, w2, debug=True)
