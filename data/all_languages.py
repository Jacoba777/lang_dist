from typing import List
from model.lang import Language

from data.austroasiatic import AUSTROASIATIC
from data.austronesian import AUSTRONESIAN
from data.baltic import BALTIC
from data.caucasian import CAUCASIAN
from data.celtic import CELTIC
from data.chukotko_kamchatkan import CHUKOTKO_KAMCHATKAN
from data.dravidian import DRAVIDIAN
from data.germanic import GERMANIC
from data.indo_aryan import INDO_ARYAN
from data.indo_euro_other import INDO_EURO_OTHER
from data.iranian import IRANIAN
from data.isolates import ISOLATES
from data.japonic import JAPONIC
from data.koreanic import KOREANIC
from data.mongolic import MONGOLIC
from data.romance import ROMANCE
from data.slavic import SLAVIC
from data.tungusic import TUNGUSIC
from data.turkic import TURKIC
from data.uralic import URALIC

classifier = {
    'identical': (0, 1),
    'dialects': (1, 10),
    'sister - highly mutually intelligible': (10, 28),
    'very related - partially intelligible': (28, 39),
    'familial': (39, 55),
    'distantly related': (55, 63),
    'unrelated': (63, 75),
    'likely nodata': (75, 100)
}

INDO_EUROPEAN = [
    *GERMANIC,
    *ROMANCE,
    *BALTIC,
    *SLAVIC,
    *CELTIC,
    *INDO_ARYAN,
    *IRANIAN,
    *INDO_EURO_OTHER,
]

ALL_LANGS: List[Language] = [
    *INDO_EUROPEAN,
    *CAUCASIAN,
    *DRAVIDIAN,
    *URALIC,
    *CHUKOTKO_KAMCHATKAN,
    *MONGOLIC,
    *TURKIC,
    *JAPONIC,
    *KOREANIC,
    *TUNGUSIC,
    *AUSTROASIATIC,
    *AUSTRONESIAN,
    *ISOLATES,
]

ALL_LANGS_W_DATA = [lang for lang in ALL_LANGS if lang.get_word_count() >= 10]
ALL_MODERN_LANGS_W_DATA = [lang for lang in ALL_LANGS_W_DATA if lang.extinct_year is None]

# LANGS_TO_USE = [lang for lang in ALL_MODERN_LANGS_W_DATA if lang in [*AUSTRONESIAN]]
LANGS_TO_USE = ALL_MODERN_LANGS_W_DATA


def get_all_langs() -> List[Language]:
    return LANGS_TO_USE
