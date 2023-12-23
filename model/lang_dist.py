from statistics import stdev, mean
from typing import Dict, List, Tuple
from model.lang import Language
from model.word import Word

from weighted_lev_v2 import weighted_lev


class LanguageDistances:
    def __init__(self, langs: List[Language]):
        self._dist: Dict[(Language, Language), (float, float)] = {}

        en = langs[0]
        for i1, l1 in enumerate(langs):
            for l2 in langs[i1 + 1:]:
                dist, std = calculate_lang_dist(l1, l2, en)
                self.set_dist(l1, l2, dist, std)

    def set_dist(self, lang1: Language, lang2: Language, dist: float, std: float):
        if lang1 > lang2:
            lang1, lang2 = lang2, lang1
        self._dist[(lang1, lang2)] = (dist, std)

    def get_dist(self, lang1: Language, lang2: Language):
        if lang1 == lang2:
            return 0.0, 0.0
        if lang1 > lang2:
            lang1, lang2 = lang2, lang1
        return self._dist[(lang1, lang2)]

    def get_all_dists(self):
        return [(v, k) for (k, v) in self._dist.items()]


def calculate_word_dists(lang1: Language, lang2: Language, en: Language) -> List[Tuple[str, str, float]]:
    common_words = [(lang1.get_word(word), lang2.get_word(word)) for word in en.get_all_words() if lang1.get_word(word) != '' and lang2.get_word(word) != '']
    word_dists = [(w1, w2, weighted_lev(Word(w1), Word(w2))) for (w1, w2) in common_words]
    return word_dists


def calculate_lang_dist(lang1: Language, lang2: Language, en: Language):
    word_dists = calculate_word_dists(lang1, lang2, en)
    dists = [w[2] for w in word_dists]
    if len(dists) == 0:
        return 1.0, 1.0

    return mean(dists), stdev(dists)
