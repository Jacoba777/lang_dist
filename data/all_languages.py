from data.germanic._germanic import ALL_LANGS as GERMANIC
from data.romance._romance import ALL_LANGS as ROMANCE
from data.baltic._baltic import ALL_LANGS as BALTIC
from data.slavic._slavic import ALL_LANGS as SLAVIC
from data.east_asian._east_asian import ALL_LANGS as EAST_ASIAN
from data.indo_euro_other._indo_euro_other import ALL_LANGS as INDO_EURO_OTHER


def get_all_langs():
    return [
        *GERMANIC,
        *ROMANCE,
        *BALTIC,
        *SLAVIC,
        *EAST_ASIAN,
        *INDO_EURO_OTHER,
    ]
