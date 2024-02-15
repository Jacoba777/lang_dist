from typing import List

from data.afroasiatic import AFROASIATIC
from data.algic import ALGIC
from data.constructed import CONSTRUCTED, ESPERANTO
from data.creoles import CREOLES
from data.dene_yeniseian import DENE_YENISEIAN
from data.hmong_mein import HMONG_MEIN
from data.hokan import HOKAN
from data.iroquoian import IROQUOIAN
from data.khoisan import KHOISAN
from data.kra_dai import KRA_DAI
from data.mayan import MAYAN
from data.muskogean import MUSKOGEAN
from data.new_world_other import NEW_WORLD_OTHER
from data.niger_congo import NIGER_CONGO
from data.oto_manguean import OTO_MANGUEAN
from data.sino_tibetan import SINO_TIBETAN
from data.siouan import SIOUAN
from data.tupian import TUPIAN
from data.uto_aztecan import UTO_AZTECAN
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
    *BALTIC,
    *CELTIC,
    *GERMANIC,
    *INDO_ARYAN,
    *IRANIAN,
    *ROMANCE,
    *SLAVIC,
    *INDO_EURO_OTHER,
]

ASIAN = [
    *AUSTROASIATIC,
    *CHUKOTKO_KAMCHATKAN,
    *DRAVIDIAN,
    *HMONG_MEIN,
    *JAPONIC,
    *KOREANIC,
    *KRA_DAI,
    *MONGOLIC,
    *SINO_TIBETAN,
    *TUNGUSIC,
    *TURKIC,
]

NEW_WORLD = [
    *ALGIC,
    *DENE_YENISEIAN,
    *HOKAN,
    *IROQUOIAN,
    *SIOUAN,
    *MAYAN,
    *MUSKOGEAN,
    *NEW_WORLD_OTHER,
    *OTO_MANGUEAN,
    *TUPIAN,
    *UTO_AZTECAN,
]

AFRICAN = [
    *KHOISAN,
    *NIGER_CONGO,
]

ALL_LANGS: List[Language] = [
    *ASIAN,
    *INDO_EUROPEAN,
    *NEW_WORLD,
    *AFROASIATIC,
    *AUSTRONESIAN,
    *AFRICAN,
    *CAUCASIAN,
    *URALIC,
    *ISOLATES,
    *CREOLES,
    *CONSTRUCTED,
]

LANGS_SUFFICIENT_DATA = [lang for lang in ALL_LANGS if lang.get_word_count() >= 10]
LANGS_MODERN_LANGS = [lang for lang in ALL_LANGS if lang.extinct_year is None]
LANGS_WIDELY_SPOKEN = [lang for lang in ALL_LANGS if lang.total_speakers >= 1000000]

# LANGS_TO_USE = [lang for lang in ALL_MODERN_LANGS_W_DATA if lang in [*CONSTRUCTED, *CREOLES, *INDO_EUROPEAN]]
LANGS_TO_USE = [lang for lang in ALL_LANGS if lang in LANGS_WIDELY_SPOKEN and lang in LANGS_SUFFICIENT_DATA or lang in [ESPERANTO]]
# LANGS_TO_USE = [lang for lang in ALL_LANGS if lang.name in ['english_us', 'german', 'dutch', 'danish', 'swedish', 'norwegian_bokmal', 'west_frisian', 'mandarin_standard', 'luxembourgish', 'icelandic', 'zeelandic', 'faroese']]


def get_all_langs() -> List[Language]:
    return LANGS_TO_USE
