from typing import List

from model.ipa_dictionary import lookup

COST_INSERT = 1.0
COST_DELETE = 1.0
COST_REPLACE = 1.0


class _State:
    def __init__(self, path: List[str], cost: float):
        self.path = path
        self.cost = cost

    def word(self):
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

    def get_state(self, word: str):
        state_matches = [s for s in self._states if s.word() == word]
        if len(state_matches) > 1:
            raise ValueError(f'Duplicate state detected for {word}')
        elif len(state_matches) == 0:
            return None
        else:
            return state_matches[0]

    def __repr__(self):
        return f'{self._states}'


def _make_replacement(state: _State, goal_word: str):
    word = state.word()
    if state.word == goal_word or word.startswith(goal_word) or goal_word.startswith(word):
        return None
    for i in range(len(goal_word)):
        letter = lookup(word[i])
        new_letter = lookup(goal_word[i])
        if letter.char != new_letter.char:
            replace_cost = letter.distance(new_letter) * COST_REPLACE
            new_word = word[:i] + goal_word[i] + word[i+1:]
            new_path = state.path.copy()
            new_path.append(new_word)
            return _State(new_path, state.cost + replace_cost)


def _make_insertion(state: _State, goal_word: str):
    word = state.word()
    if word == goal_word or word.startswith(goal_word):
        return None
    for i in range(len(goal_word)):
        if len(word) < i+1 or word[i] != goal_word[i]:
            new_word = word[:i] + goal_word[i] + word[i:]
            new_path = state.path.copy()
            new_path.append(new_word)
            return _State(new_path, state.cost + COST_INSERT)


def _make_deletion(state: _State, goal_word: str):
    word = state.word()
    if word == goal_word or goal_word.startswith(word):
        return None
    for i in range(len(word)):
        if len(goal_word) < i+1 or word[i] != goal_word[i]:
            new_word = word[:i] + word[i+1:]
            new_path = state.path.copy()
            new_path.append(new_word)
            return _State(new_path, state.cost + COST_DELETE)


def _get_choice_states(state: _State, goal_word: str):
    replace = _make_replacement(state, goal_word)
    insert = _make_insertion(state, goal_word)
    delete = _make_deletion(state, goal_word)

    states = [replace, insert, delete]
    return [s for s in states if s]


def _weighted_lev_path(goal_word: str, states: _States, best: _State | None = None, debug=False):
    while not states.is_empty() and (not best or states.get_cheapest() < best):
        cheapest = states.get_cheapest()
        new_states = _get_choice_states(cheapest, goal_word)

        for state in new_states:
            existing_state = states.get_state(state.word())
            if state.word() == goal_word and (not best or best > state):
                best = state
            elif existing_state and existing_state.cost > state.cost:
                states.remove(existing_state)
                states.add(state)
            elif not existing_state:
                states.add(state)
        states.remove(cheapest)
    return best


def weighted_lev(word: str, goal_word: str):
    if word == goal_word:
        return 0.0

    initial_state = _State([word], 0)
    states = _States([initial_state])
    return _weighted_lev_path(goal_word, states).cost / max(len(word), len(goal_word))


def debug_weighted_lev(word: str, goal_word: str):
    if word == goal_word:
        return 0.0

    initial_state = _State([word], 0)
    states = _States([initial_state])
    return _weighted_lev_path(goal_word, states)


if __name__ == '__main__':
    print(debug_weighted_lev("ai", "je"))
