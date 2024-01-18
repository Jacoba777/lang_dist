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
from data.east_asian._east_asian import ALL_LANGS as EAST_ASIAN
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


def get_all_langs() -> List[Language]:
    return [
        *GERMANIC,
        *ROMANCE,
        *BALTIC,
        *SLAVIC,
        *CELTIC,
        *EAST_ASIAN,
        *INDO_ARYAN,
        *IRANIAN,
        *CAUCASIAN,
        *DRAVIDIAN,
        *URALIC,
        *INDO_EURO_OTHER,
        *ISOLATES,
    ]
