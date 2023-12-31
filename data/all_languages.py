from data.germanic._germanic import ALL_LANGS as GERMANIC
from data.romance._romance import ALL_LANGS as ROMANCE
from data.east_asian._east_asian import ALL_LANGS as EAST_ASIAN


def get_all_langs():
    return [
        *GERMANIC,
        *ROMANCE,
        *EAST_ASIAN,
    ]
