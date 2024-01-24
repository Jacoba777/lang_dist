from typing import List

from data.germanic._germanic import ALL_LANGS as GERMANIC
from data.romance._romance import ALL_LANGS as ROMANCE
from data.baltic._baltic import ALL_LANGS as BALTIC
from data.slavic._slavic import ALL_LANGS as SLAVIC
from data.celtic._celtic import ALL_LANGS as CELTIC
from data.indo_aryan._indo_aryan import ALL_LANGS as INDO_ARYAN
from data.iranian._iranian import ALL_LANGS as IRANIAN
from data.dravidian._dravidian import ALL_LANGS as DRAVIDIAN
from data.uralic._uralic import ALL_LANGS as URALIC
from data.caucasian._caucasian import ALL_LANGS as CAUCASIAN
from data.indo_euro_other._indo_euro_other import ALL_LANGS as INDO_EURO_OTHER
from data.koreanic._koreanic import ALL_LANGS as KOREANIC
from data.chukotko_kamchatkan._chukotko_kamchatkan import ALL_LANGS as CHUKOTKO_KAMCHATKAN
from data.mongolic._mongolic import ALL_LANGS as MONGOLIC
from data.turkic._turkic import ALL_LANGS as TURKIC
from data.japonic._japonic import ALL_LANGS as JAPONIC
from data.tungusic._tungusic import TUNGUSIC
from data.austroasiatic._austroasiatic import AUSTROASIATIC
from data.isolates._isolates import ALL_LANGS as ISOLATES
from model.lang import Language

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
    *ISOLATES,
]

ALL_LANGS_W_DATA = [lang for lang in ALL_LANGS if lang.get_word_count() >= 10]
ALL_MODERN_LANGS_W_DATA = [lang for lang in ALL_LANGS_W_DATA if lang.extinct_year is None]

LANGS_TO_USE = [lang for lang in ALL_MODERN_LANGS_W_DATA if lang in [*AUSTROASIATIC]]
# LANGS_TO_USE = AUSTRO


def get_all_langs() -> List[Language]:
    return LANGS_TO_USE
