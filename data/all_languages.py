from data.germanic._germanic import ALL_LANGS as GERMANIC
from data.romance._romance import ALL_LANGS as ROMANCE


def get_all_langs():
    return [
        *GERMANIC,
        *ROMANCE,
    ]
