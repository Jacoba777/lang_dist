from typing import List

from model.phone import get_phone_by_symbol, Phone, get_phone_distance
from model.state import get_phone_list_dist


class Syllable:
    def __init__(self, onset: List[Phone] = None, nucleus: List[Phone] = None, coda: List[Phone] = None):
        self.onset = onset
        self.nucleus = nucleus
        self.coda = coda

    def __repr__(self):
        return f'<Syllable "{self.onset}{self.nucleus}{self.coda}">'


def create_syllables_from_phones(phones: List[Phone]):
    syllables, consonants = [], []
    curr_syllable = Syllable()
    for phone in phones:
        if phone.is_vowel():
            if not curr_syllable.nucleus:
                curr_syllable.onset = consonants
                consonants = []
                curr_syllable.nucleus = [phone]
            elif not consonants:
                curr_syllable.nucleus.append(phone)
            else:
                prev_syllable, curr_syllable = curr_syllable, Syllable(nucleus=[phone])
                _split_consonants(prev_syllable, curr_syllable, consonants)
                syllables.append(prev_syllable)
                consonants = []
        else:
            consonants.append(phone)
    curr_syllable.coda = consonants
    syllables.append(curr_syllable)
    return syllables


# TEMPORARY function. The raw string should be processed in a new class to account for non-phone ipa symbols and modifiers, like . or '
def create_syllables_from_ipa_string(ipa: str):
    if not ipa:
        return None
    phones = [get_phone_by_symbol(s) for s in ipa]
    phones = [p for p in phones if p is not None]
    return create_syllables_from_phones(phones)


def _split_consonants(s1: Syllable, s2: Syllable, consonants: List[Phone]):
    i = len(consonants) // 2
    s1.coda, s2.onset = consonants[:i], consonants[i:]


def syllable_distance(s1: Syllable, s2: Syllable, debug=False):
    dist_onset = get_phone_list_dist(s1.onset, s2.onset, debug=debug)
    dist_nucleus = get_phone_list_dist(s1.nucleus, s2.nucleus, debug=debug)
    dist_coda = get_phone_list_dist(s1.coda, s2.coda, debug=debug)
    if debug:
        print(f'{dist_onset=},{dist_nucleus=},{dist_coda=}')
    return (dist_onset + dist_nucleus + dist_coda) / 3


def main():
    # w = Word(ipa='blɑɒːr')
    w1 = create_syllables_from_ipa_string('ɹɒɹ')
    w2 = create_syllables_from_ipa_string('fip')

    print(w1, w2, syllable_distance(w1[0], w2[0]))


if __name__ == '__main__':
    main()
