from enum import Enum


class Place(Enum):
    N0_BILABIAL = '0_BILABIAL'
    N1_LABIODENTAL = '1_LABIODENTAL'
    N2_DENTAL = '2_DENTAL'
    N3_ALVEOLAR = '3_ALVEOLAR'
    N4_POST_ALVEOLAR = '4_POST_ALVEOLAR'
    N5_ALVEOLO_PALATAL = '5_ALVEOLO_PALATAL'
    N6_RETROFLEX = '6_RETROFLEX'
    N7_PALATAL = '7_PALATAL'
    N8_VELAR = '8_VELAR'
    N9_UVULAR = '9_UVULAR'
    NA_PHARYNGEAL = 'A_PHARYNGEAL'
    NB_GLOTTAL = 'B_GLOTTAL'
    NC_VOWEL = 'C_VOWEL'


class Manner(Enum):
    N0_CLICK = '0_CLICK'
    N1_IMPLOSIVE = '1_IMPLOSIVE'
    N2_PLOSIVE = '2_PLOSIVE'
    N3_AFFRICATE = '3_AFFRICATE'
    N4_FRICATIVE = '4_FRICATIVE'
    N5_NASAL = '5_NASAL'
    N6_VOWEL = '6_VOWEL'
    N7_SEMIVOWEL = '7_SEMIVOWEL'
    N8_APPROX = '8_APPROX'
    N9_TAP = '9_TAP'
    NA_TRILL = 'A_TRILL'
    NB_EJECTIVE = 'B_EJECTIVE'


class Frontage(Enum):
    N0_FRONT = '0_FRONT'
    N1_NEAR_FRONT = '1_NEAR_FRONT'
    N2_CENTRAL = '2_CENTRAL'
    N3_NEAR_BACK = '3_NEAR_BACK'
    N4_BACK = '4_BACK'
    N5_CONSONANT = '5_CONSONANT'


class Openness(Enum):
    N0_CLOSED = '0_CLOSED'
    N1_NEAR_CLOSED = '1_NEAR_CLOSED'
    N2_CLOSED_MID = '2_CLOSED_MID'
    N3_MID = '3_MID'
    N4_OPEN_MID = '4_OPEN_MID'
    N5_NEAR_OPEN = '5_NEAR_OPEN'
    N6_OPEN = '6_OPEN'
    N7_CONSONANT = '7_CONSONANT'


class Phone:
    def __init__(self,
                 symbol: str,
                 manner: str,
                 place: str,
                 frontage: str,
                 openness: str,
                 voiced: bool,
                 rounded=False,
                 rhotic=False,
                 lateral=False,
                 strident=False,
                 sibilant=False,
                 f1: int | None = None,
                 f2: int | None = None,):
        self.symbol = symbol
        self.manner = Manner(manner)
        self.place = Place(place)
        self.frontage = Frontage(frontage)
        self.openness = Openness(openness)
        self.voiced = voiced in ['TRUE', True]
        self.rounded = rounded in ['TRUE', True]
        self.rhotic = rhotic in ['TRUE', True]
        self.lateral = lateral in ['TRUE', True]
        self.strident = strident in ['TRUE', True]
        self.sibilant = sibilant in ['TRUE', True]
        self.f1 = int(f1) if f1 not in ['FALSE', None] else None
        self.f2 = int(f2) if f2 not in ['FALSE', None] else None

    def __repr__(self):
        return f'{self.symbol}'

    def is_vowel(self):
        return self.manner == Manner.N6_VOWEL

    def is_consonant(self):
        return not self.is_vowel

    def is_obstruent(self):
        return self.manner in [
            Manner.N0_CLICK,
            Manner.N1_IMPLOSIVE,
            Manner.N2_PLOSIVE,
            Manner.N3_AFFRICATE,
            Manner.N4_FRICATIVE,
            Manner.NB_EJECTIVE,
        ]

    def is_occlusive(self):
        return self.manner in [
            Manner.N0_CLICK,
            Manner.N1_IMPLOSIVE,
            Manner.N2_PLOSIVE,
            Manner.N3_AFFRICATE,
            Manner.N5_NASAL,
            Manner.NB_EJECTIVE,
        ]

    def is_vibrant(self):
        return self.manner in [
            Manner.N9_TAP,
            Manner.NA_TRILL,
        ]

    def is_vowellike(self):
        return self.manner in [
            Manner.N6_VOWEL,
            Manner.N7_SEMIVOWEL,
        ]

    def is_vocoid(self):
        return self.manner == Manner.N8_APPROX or self.is_vowellike()

    def is_liquid(self):
        return self.rhotic or self.lateral

    def is_labial(self):
        return self.rounded or self.place in [
            Place.N0_BILABIAL,
            Place.N1_LABIODENTAL,
        ]

    def is_coronal(self):
        return self.place in [
            Place.N2_DENTAL,
            Place.N3_ALVEOLAR,
            Place.N4_POST_ALVEOLAR,
            Place.N6_RETROFLEX,
            Place.N7_PALATAL,
        ]

    def is_dorsal(self):
        return self.place in [
            Place.N8_VELAR,
            Place.N9_UVULAR,
            Place.NA_PHARYNGEAL,
        ]

    def is_lingual(self):
        return self.is_dorsal() or self.is_coronal()


def _read_phones_from_file():
    with open('../data/ipa/phones.txt', encoding='UTF-8') as f:
        phones_raw = f.read().split('\n')[1:]
    return [Phone(*pd.split('\t')) for pd in phones_raw]


PHONES = _read_phones_from_file()
VOWELS = [p for p in PHONES if p.is_vowel()]

_f1s = [v.f1 for v in VOWELS if type(v.f1) == int]
_f2s = [v.f2 for v in VOWELS if type(v.f2) == int]
F1_MIN, F1_MAX = min(_f1s), max(_f1s)
F2_MIN, F2_MAX = min(_f2s), max(_f2s)


def _get_phone_manner_distance(p1: Phone, p2: Phone):
    if p1.manner == p2.manner:
        return 0.0
    if p1.is_vowellike() and p2.is_vowellike():
        return 1 / 8
    if p1.is_vocoid() and p2.is_vocoid() or p1.is_vibrant() and p2.is_vibrant():
        return 1 / 4
    if p1.is_obstruent() == p2.is_obstruent():
        return 1 / 2
    return 1.0


def _get_phone_place_distance(p1: Phone, p2: Phone):
    if p1.place == p2.place:
        return 0.0
    if p1.is_coronal() and p2.is_coronal() or p1.is_dorsal() and p2.is_dorsal():
        return 1/4
    if p1.is_labial() == p1.is_labial() and p1.is_lingual() == p2.is_lingual():
        return 1/2
    return 1.0


def _get_vowel_formant_distance(v1: Phone, v2: Phone):
    v1_f1_norm = (F1_MAX - v1.f1)/(F1_MAX - F1_MIN)
    v1_f2_norm = (F2_MAX - v1.f2)/(F2_MAX - F2_MIN)
    v2_f1_norm = (F1_MAX - v2.f1) / (F1_MAX - F1_MIN)
    v2_f2_norm = (F2_MAX - v2.f2) / (F2_MAX - F2_MIN)

    f1_dst = (v1_f1_norm - v2_f1_norm)**2
    f2_dist = (v1_f2_norm - v2_f2_norm)**2
    dist = (f1_dst + f2_dist)**0.5
    dist_norm = dist / 1.1768543475538389  # this is the max distance between 2 vowel formants using this approach (i, ɒ). This makes this distance range from (0,1)
    return dist_norm


def get_phone_distance(p1: Phone, p2: Phone):
    def _apply_factor(weight: float, cond: bool | float):
        nonlocal total
        nonlocal dist

        # if p1 == get_by_symbol('j') or p2 == get_by_symbol('j'):
        #     print(cond, dist, total)

        total += weight
        if type(cond) == float:
            dist += weight * cond
        else:
            dist += weight if cond else 0

    dist, total = 0.0, 0.0

    if p1.is_vowel() and p2.is_vowel():
        _apply_factor(1.0, _get_vowel_formant_distance(p1, p2))
    elif p1.is_vowellike() and p2.is_vowellike():
        _apply_factor(1.0, p1.rounded != p2.rounded)
        _apply_factor(5.0, _get_phone_manner_distance(p1, p2))

        _apply_factor(1.0, _get_phone_place_distance(p1, p2))
        _apply_factor(5.0, _get_vowel_formant_distance(p1, p2))
    else:
        _apply_factor(0.25, p1.rhotic != p2.rhotic)
        _apply_factor(0.25, p1.lateral != p2.lateral)
        _apply_factor(0.5, p1.is_liquid() != p2.is_liquid())
        # _apply_factor(1.0, p1.is_occlusive() != p2.is_occlusive())
        _apply_factor(1.0, p1.voiced != p2.voiced)
        _apply_factor(4, _get_phone_manner_distance(p1, p2))

        _apply_factor(2, _get_phone_place_distance(p1, p2))

    return dist / total


def get_phone_by_symbol(symbol: str):
    match = [p for p in PHONES if p.symbol == symbol]
    return match[0] if len(match) else None


if __name__ == '__main__':
    x = get_phone_by_symbol('f')
    dists = [(p, get_phone_distance(x, p)) for p in PHONES]
    dists.sort(key=lambda d: d[1])
    print(dists)
