from typing import Set, TypeVar


class Token:
    def __eq__(self, other):
        return False


class Symbol(Token):
    def __init__(self, char):
        self.char = char
        self._modifiers: Set[Modifier] = set()

    def __repr__(self):
        return self.char

    def __eq__(self, other):
        if not hasattr(other, "char") or not hasattr(other, "modifiers"):
            return other == self
        return self.char == other.char and self._modifiers - other._modifiers == set()

    def add_modifier(self, modifier):
        self._modifiers.add(modifier)
        self.char = self.char + modifier.char


class Vowel(Symbol):
    class Frontage:
        FRONT = 0
        NEAR_FRONT = 1
        CENTRAL = 2
        NEAR_BACK = 3
        BACK = 4

    class Openness:
        CLOSED = 0
        NEAR_CLOSED = 1
        CLOSED_MID = 2
        MID = 3
        OPEN_MID = 4
        NEAR_OPEN = 5
        OPEN = 6

    def __init__(self, char, frontage: int, openness: int, rounded: bool, f1: int = 0, f2: int = 0, approx1=None, approx2=None):
        super().__init__(char)
        self.frontage = frontage
        self.openness = openness
        self.rounded = rounded
        if f1 and f2:
            self.f1 = f1
            self.f2 = f2
        else:
            self.f1 = (approx1.f1 + approx2.f1)/2
            self.f2 = (approx1.f2 + approx2.f2)/2


class Consonant(Symbol):
    class Manner:
        PLOSIVE = 0
        NASAL = 1
        TRILL = 2
        TAP = 3
        FRICATIVE = 4
        LAT_FRICATIVE = 5
        APPROX = 6
        LAT_APPROX = 7
        CLICK = 8
        IMPLOSIVE = 9

    class Place:
        BILABIAL = 0
        LABIODENTAL = 1
        DENTAL = 2
        ALVEOLAR = 3
        POST_ALVEOLAR = 4
        RETROFLEX = 5
        PALATAL = 6
        VELAR = 7
        UVULAR = 8
        PHARYNGEAL = 9
        GLOTTAL = 10

    def __init__(self, char, manner: int, place: int, voiced: bool):
        super().__init__(char)
        self.manner = manner
        self.place = place
        self.voiced = voiced


class Modifier(Symbol):
    class FixType:
        WORD_LEVEL_PRE = 0
        SYLLABLE_LEVEL_PRE = 1
        SYMBOL_LEVEL_POST = 2
        AFFRICATE = 3

    def __init__(self, char, fix_type: int):
        super().__init__(char)
        self.fix_type = fix_type

    def __hash__(self):
        return self.fix_type * hash(self.char)


class Diphthong(Token):
    def __init__(self, v1: Vowel, v2: Vowel):
        self.v1 = v1
        self.v2 = v2

    def __repr__(self):
        return f'{self.v1}{self.v2}'

    def __eq__(self, other):
        if type(other) != Diphthong:
            return False
        return self.v1 == other.v1 and self.v2 == other.v2


Vowellike = TypeVar('Vowellike', Vowel, Diphthong)
AnyIPAToken = TypeVar('AnyIPAToken', Vowel, Diphthong, Consonant)
