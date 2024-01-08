from model.lang import Language

FAMILY = 'baltic'

LATGALIAN = Language('latgalian', FAMILY, 200000, 0)
LATVIAN = Language('latvian', FAMILY, 1500000, 0)
LITHUANIAN = Language('lithuanian', FAMILY, 3000000, 0)
PRUSSIAN_OLD = Language('prussian_old', FAMILY, extinct_year=1700)
SAMOGITIAN = Language('samogitian', FAMILY, 500000, 0)


ALL_LANGS = [
    LATGALIAN,
    LATVIAN,
    LITHUANIAN,
    PRUSSIAN_OLD,
    SAMOGITIAN,
]

if __name__ == '__main__':
    print(LATGALIAN.get_word('they').ipa_tokenized)
