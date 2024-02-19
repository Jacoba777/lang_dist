from typing import List

from old_world import *
from new_world import *

from constructed import *
from creoles import *
from isolates import *

ALL_LANGS: List[Language] = [
    *NEW_WORLD,
    *OLD_WORLD,
    *ISOLATES,
    *CREOLES,
    *CONSTRUCTED,
]

LANGS_SUFFICIENT_DATA = [lang for lang in ALL_LANGS if lang.get_word_count() >= 10]
LANGS_MODERN_LANGS = [lang for lang in ALL_LANGS if lang.extinct_year is None]
LANGS_WIDELY_SPOKEN = [lang for lang in ALL_LANGS if lang.total_speakers >= 1000000]

LANGS_TO_USE = [lang for lang in ALL_LANGS if lang in [*GERMANIC] and lang]


def get_all_langs() -> List[Language]:
    return LANGS_TO_USE
