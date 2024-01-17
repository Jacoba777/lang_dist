from data.germanic._germanic import ALL_LANGS as GERMANIC
from data.romance._romance import ALL_LANGS as ROMANCE
from data.baltic._baltic import ALL_LANGS as BALTIC
from data.slavic._slavic import ALL_LANGS as SLAVIC
from data.celtic._celtic import ALL_LANGS as CELTIC
from data.east_asian._east_asian import ALL_LANGS as EAST_ASIAN
from data.indo_euro_other._indo_euro_other import ALL_LANGS as INDO_EURO_OTHER

classifier = {
    'identical': (0, 1),
    'dialects': (1, 10),
    'sister': (10, 28),
    'very related': (28, 39),
    'familial': (39, 55),
    'distant': (55, 63),
    'unrelated': (63, 75),
    'likely nodata': (75, 100)
}


def get_all_langs():
    return [
        *GERMANIC,
        *ROMANCE,
        *BALTIC,
        *SLAVIC,
        *CELTIC,
        *EAST_ASIAN,
        *INDO_EURO_OTHER,
    ]
