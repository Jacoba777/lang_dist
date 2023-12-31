from statistics import stdev, mean
from typing import Dict, List, Tuple

from data.swadesh import SWADESH_WORDS
from model.lang import Language
from model.word import word_distance


class LanguageDistances:
    def __init__(self, langs: List[Language]):
        self._dist: Dict[(Language, Language), (float, float)] = {}
        for i1, l1 in enumerate(langs):
            for l2 in langs[i1 + 1:]:
                dist, std = calculate_lang_dist(l1, l2)
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


def calculate_word_dists(lang1: Language, lang2: Language) -> List[Tuple[str, str, float]]:
    common_words = [(lang1.get_word(w), lang2.get_word(w)) for w in SWADESH_WORDS]
    common_words = [(w1, w2) for (w1, w2) in common_words if w1.ipa and w2.ipa]
    word_dists = [(w1, w2, word_distance(w1, w2)) for (w1, w2) in common_words]
    return word_dists


def calculate_lang_dist(lang1: Language, lang2: Language):
    dists = calculate_word_dists(lang1, lang2)
    if len(dists) == 0:
        return 1.0, 1.0
    dists = [d[2] for d in dists]

    return mean(dists), stdev(dists)
