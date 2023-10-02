from copy import copy
from typing import List


class Token:
    def __eq__(self, other):
        return False


class Symbol(Token):
    def __init__(self, char):
        self.char = char
        self.modifiers = set()

    def __repr__(self):
        return self.char

    def __eq__(self, other):
        if not hasattr(other, "char") or not hasattr(other, "modifiers"):
            return other == self
        return self.char == other.char and self.modifiers - other.modifiers == set()


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


class Vowels:
    i = Vowel('i', Vowel.Frontage.FRONT, Vowel.Openness.CLOSED, rounded=False, f1=240, f2=2400)
    y = Vowel('y', Vowel.Frontage.FRONT, Vowel.Openness.CLOSED, rounded=True, f1=235, f2=2100)
    e = Vowel('e', Vowel.Frontage.FRONT, Vowel.Openness.CLOSED_MID, rounded=False, f1=390, f2=2300)
    ø = Vowel('ø', Vowel.Frontage.FRONT, Vowel.Openness.CLOSED_MID, rounded=True, f1=370, f2=1900)
    ɛ = Vowel('ɛ', Vowel.Frontage.FRONT, Vowel.Openness.OPEN_MID, rounded=False, f1=610, f2=1900)
    ε = Vowel('ε', Vowel.Frontage.FRONT, Vowel.Openness.OPEN_MID, rounded=False, f1=610, f2=1900)  # ε and ɛ are interchangeable in IPA
    œ = Vowel('œ', Vowel.Frontage.FRONT, Vowel.Openness.OPEN_MID, rounded=True, f1=585, f2=1710)
    æ = Vowel('æ', Vowel.Frontage.FRONT, Vowel.Openness.NEAR_OPEN, rounded=False, f1=(730), f2=(1760))
    a = Vowel('a', Vowel.Frontage.FRONT, Vowel.Openness.OPEN, rounded=False, f1=850, f2=1610)
    ɶ = Vowel('ɶ', Vowel.Frontage.FRONT, Vowel.Openness.OPEN, rounded=True, f1=820, f2=1530)

    ɯ = Vowel('ɯ', Vowel.Frontage.BACK, Vowel.Openness.CLOSED, rounded=False, f1=300, f2=1390)
    u = Vowel('u', Vowel.Frontage.BACK, Vowel.Openness.CLOSED, rounded=True, f1=250, f2=595)
    ɤ = Vowel('ɤ', Vowel.Frontage.BACK, Vowel.Openness.CLOSED_MID, rounded=False, f1=460, f2=1310)
    o = Vowel('o', Vowel.Frontage.BACK, Vowel.Openness.CLOSED_MID, rounded=True, f1=360, f2=640)
    ʌ = Vowel('ʌ', Vowel.Frontage.BACK, Vowel.Openness.OPEN_MID, rounded=False, f1=600, f2=1170)
    ɔ = Vowel('ɔ', Vowel.Frontage.BACK, Vowel.Openness.OPEN_MID, rounded=True, f1=500, f2=700)
    ɑ = Vowel('ɑ', Vowel.Frontage.BACK, Vowel.Openness.OPEN, rounded=False, f1=750, f2=940)
    ɒ = Vowel('ɒ', Vowel.Frontage.BACK, Vowel.Openness.OPEN, rounded=True, f1=700, f2=760)

    ɨ = Vowel('ɨ', Vowel.Frontage.CENTRAL, Vowel.Openness.CLOSED, rounded=False, approx1=i, approx2=ɯ)
    ʉ = Vowel('ʉ', Vowel.Frontage.CENTRAL, Vowel.Openness.CLOSED, rounded=True, approx1=y, approx2=u)
    ɘ = Vowel('ɘ', Vowel.Frontage.CENTRAL, Vowel.Openness.CLOSED_MID, rounded=False, approx1=e, approx2=ɤ)
    ɵ = Vowel('ɵ', Vowel.Frontage.CENTRAL, Vowel.Openness.CLOSED_MID, rounded=True, approx1=ø, approx2=o)
    ɜ = Vowel('ɜ', Vowel.Frontage.CENTRAL, Vowel.Openness.OPEN_MID, rounded=False, approx1=ɛ, approx2=ʌ)
    ɞ = Vowel('ɞ', Vowel.Frontage.CENTRAL, Vowel.Openness.OPEN_MID, rounded=True, approx1=œ, approx2=ɔ)
    ɐ = Vowel('ɐ', Vowel.Frontage.CENTRAL, Vowel.Openness.NEAR_OPEN, rounded=False, approx1=æ, approx2=ʌ)
    ä = Vowel('ä', Vowel.Frontage.CENTRAL, Vowel.Openness.OPEN, rounded=False, approx1=a, approx2=ɑ)

    ɪ = Vowel('ɪ', Vowel.Frontage.NEAR_FRONT, Vowel.Openness.NEAR_CLOSED, rounded=False, approx1=i, approx2=ɘ)
    ʏ = Vowel('ʏ', Vowel.Frontage.NEAR_FRONT, Vowel.Openness.NEAR_CLOSED, rounded=True, approx1=y, approx2=ɵ)

    ə = Vowel('ə', Vowel.Frontage.CENTRAL, Vowel.Openness.MID, rounded=False, approx1=ɘ, approx2=ɜ)
    ʊ = Vowel('ʊ', Vowel.Frontage.NEAR_BACK, Vowel.Openness.NEAR_CLOSED, rounded=True, approx1=ɵ, approx2=u)

    # temp nasals
    ã = Vowel('ã', Vowel.Frontage.FRONT, Vowel.Openness.OPEN, rounded=False, f1=850, f2=1610)
    ẽ = Vowel('ẽ', Vowel.Frontage.FRONT, Vowel.Openness.CLOSED_MID, rounded=False, f1=390, f2=2300)
    ĩ = Vowel('ĩ', Vowel.Frontage.FRONT, Vowel.Openness.CLOSED, rounded=False, f1=240, f2=2400)
    õ = Vowel('õ', Vowel.Frontage.BACK, Vowel.Openness.CLOSED_MID, rounded=True, f1=360, f2=640)
    ũ = Vowel('ũ', Vowel.Frontage.BACK, Vowel.Openness.CLOSED, rounded=True, f1=250, f2=595)

    # Circum
    ê = Vowel('ê', Vowel.Frontage.FRONT, Vowel.Openness.CLOSED_MID, rounded=False, f1=390, f2=2300)

    all = [i, y, e, ø, ɛ, ε, œ, æ, a, ɶ, ɪ, ʏ, ɨ, ʉ, ɘ, ɵ, ə, ɜ, ɞ, ɐ, ä, ʊ, ɯ, u, ɤ, o, ʌ, ɔ, ɑ, ɒ, ã, ẽ, ĩ, õ, ũ, ê]


class Consonants:
    p = Consonant('p', Consonant.Manner.PLOSIVE, Consonant.Place.BILABIAL, voiced=False)
    b = Consonant('b', Consonant.Manner.PLOSIVE, Consonant.Place.BILABIAL, voiced=True)
    t = Consonant('t', Consonant.Manner.PLOSIVE, Consonant.Place.ALVEOLAR, voiced=False)
    d = Consonant('d', Consonant.Manner.PLOSIVE, Consonant.Place.ALVEOLAR, voiced=True)
    ʈ = Consonant('ʈ', Consonant.Manner.PLOSIVE, Consonant.Place.RETROFLEX, voiced=False)
    ɖ = Consonant('ɖ', Consonant.Manner.PLOSIVE, Consonant.Place.RETROFLEX, voiced=True)
    c = Consonant('c', Consonant.Manner.PLOSIVE, Consonant.Place.PALATAL, voiced=False)
    ɟ = Consonant('ɟ', Consonant.Manner.PLOSIVE, Consonant.Place.PALATAL, voiced=True)
    k = Consonant('k', Consonant.Manner.PLOSIVE, Consonant.Place.VELAR, voiced=False)
    ɡ = Consonant('ɡ', Consonant.Manner.PLOSIVE, Consonant.Place.VELAR, voiced=True)
    g = Consonant('g', Consonant.Manner.PLOSIVE, Consonant.Place.VELAR, voiced=True)  # g,ɡ interchangeable
    q = Consonant('q', Consonant.Manner.PLOSIVE, Consonant.Place.UVULAR, voiced=False)
    ɢ = Consonant('ɢ', Consonant.Manner.PLOSIVE, Consonant.Place.UVULAR, voiced=True)
    ʔ = Consonant('ʔ', Consonant.Manner.PLOSIVE, Consonant.Place.GLOTTAL, voiced=False)

    m = Consonant('m', Consonant.Manner.NASAL, Consonant.Place.BILABIAL, voiced=True)
    ɱ = Consonant('ɱ', Consonant.Manner.NASAL, Consonant.Place.LABIODENTAL, voiced=True)
    n = Consonant('n', Consonant.Manner.NASAL, Consonant.Place.ALVEOLAR, voiced=True)
    ɳ = Consonant('ɳ', Consonant.Manner.NASAL, Consonant.Place.RETROFLEX, voiced=True)
    ɲ = Consonant('ɲ', Consonant.Manner.NASAL, Consonant.Place.PALATAL, voiced=True)
    ŋ = Consonant('ŋ', Consonant.Manner.NASAL, Consonant.Place.VELAR, voiced=True)
    ɴ = Consonant('ɴ', Consonant.Manner.NASAL, Consonant.Place.UVULAR, voiced=True)

    ʙ = Consonant('ʙ', Consonant.Manner.TRILL, Consonant.Place.BILABIAL, voiced=True)
    r = Consonant('r', Consonant.Manner.TRILL, Consonant.Place.ALVEOLAR, voiced=True)
    ʀ = Consonant('ʀ', Consonant.Manner.TRILL, Consonant.Place.UVULAR, voiced=True)
    ʜ = Consonant('ʜ', Consonant.Manner.TRILL, Consonant.Place.PHARYNGEAL, voiced=False)

    ⱱ = Consonant('ⱱ', Consonant.Manner.TAP, Consonant.Place.LABIODENTAL, voiced=True)
    ɾ = Consonant('ɾ', Consonant.Manner.TAP, Consonant.Place.ALVEOLAR, voiced=True)
    ɽ = Consonant('ɽ', Consonant.Manner.TAP, Consonant.Place.RETROFLEX, voiced=True)

    ɸ = Consonant('ɸ', Consonant.Manner.FRICATIVE, Consonant.Place.BILABIAL, voiced=False)
    β = Consonant('β', Consonant.Manner.FRICATIVE, Consonant.Place.BILABIAL, voiced=True)
    f = Consonant('f', Consonant.Manner.FRICATIVE, Consonant.Place.LABIODENTAL, voiced=False)
    v = Consonant('v', Consonant.Manner.FRICATIVE, Consonant.Place.LABIODENTAL, voiced=True)
    θ = Consonant('θ', Consonant.Manner.FRICATIVE, Consonant.Place.DENTAL, voiced=False)
    ð = Consonant('ð', Consonant.Manner.FRICATIVE, Consonant.Place.DENTAL, voiced=True)
    s = Consonant('s', Consonant.Manner.FRICATIVE, Consonant.Place.ALVEOLAR, voiced=False)
    z = Consonant('z', Consonant.Manner.FRICATIVE, Consonant.Place.ALVEOLAR, voiced=True)
    ʃ = Consonant('ʃ', Consonant.Manner.FRICATIVE, Consonant.Place.POST_ALVEOLAR, voiced=False)
    ʒ = Consonant('ʒ', Consonant.Manner.FRICATIVE, Consonant.Place.POST_ALVEOLAR, voiced=True)
    ʂ = Consonant('ʂ', Consonant.Manner.FRICATIVE, Consonant.Place.RETROFLEX, voiced=False)
    ʐ = Consonant('ʐ', Consonant.Manner.FRICATIVE, Consonant.Place.RETROFLEX, voiced=True)
    ç = Consonant('ç', Consonant.Manner.FRICATIVE, Consonant.Place.PALATAL, voiced=False)
    ʝ = Consonant('ʝ', Consonant.Manner.FRICATIVE, Consonant.Place.PALATAL, voiced=True)
    x = Consonant('x', Consonant.Manner.FRICATIVE, Consonant.Place.VELAR, voiced=False)
    ɣ = Consonant('ɣ', Consonant.Manner.FRICATIVE, Consonant.Place.VELAR, voiced=True)
    χ = Consonant('χ', Consonant.Manner.FRICATIVE, Consonant.Place.UVULAR, voiced=False)
    ʁ = Consonant('ʁ', Consonant.Manner.FRICATIVE, Consonant.Place.UVULAR, voiced=True)
    ħ = Consonant('ħ', Consonant.Manner.FRICATIVE, Consonant.Place.PHARYNGEAL, voiced=False)
    ʕ = Consonant('ʕ', Consonant.Manner.FRICATIVE, Consonant.Place.PHARYNGEAL, voiced=True)
    h = Consonant('h', Consonant.Manner.FRICATIVE, Consonant.Place.GLOTTAL, voiced=False)
    ɦ = Consonant('ɦ', Consonant.Manner.FRICATIVE, Consonant.Place.GLOTTAL, voiced=True)

    ɬ = Consonant('ɬ', Consonant.Manner.LAT_FRICATIVE, Consonant.Place.ALVEOLAR, voiced=False)
    ɮ = Consonant('ɮ', Consonant.Manner.LAT_FRICATIVE, Consonant.Place.ALVEOLAR, voiced=True)

    ʋ = Consonant('ʋ', Consonant.Manner.APPROX, Consonant.Place.LABIODENTAL, voiced=True)
    ɹ = Consonant('ɹ', Consonant.Manner.APPROX, Consonant.Place.ALVEOLAR, voiced=True)
    ɻ = Consonant('ɻ', Consonant.Manner.APPROX, Consonant.Place.RETROFLEX, voiced=True)
    j = Consonant('j', Consonant.Manner.APPROX, Consonant.Place.PALATAL, voiced=True)
    ɰ = Consonant('ɰ', Consonant.Manner.APPROX, Consonant.Place.VELAR, voiced=True)

    l = Consonant('l', Consonant.Manner.LAT_APPROX, Consonant.Place.ALVEOLAR, voiced=True)
    ɭ = Consonant('ɭ', Consonant.Manner.LAT_APPROX, Consonant.Place.RETROFLEX, voiced=True)
    ʎ = Consonant('ʎ', Consonant.Manner.LAT_APPROX, Consonant.Place.PALATAL, voiced=True)
    ʟ = Consonant('ʟ', Consonant.Manner.LAT_APPROX, Consonant.Place.VELAR, voiced=True)

    # Co-articulated, so properties are approximated
    w = Consonant('w', Consonant.Manner.APPROX, Consonant.Place.BILABIAL, voiced=True)
    ʍ = Consonant('ʍ', Consonant.Manner.FRICATIVE, Consonant.Place.VELAR, voiced=False)  # This is a copy of x, could not find a better way to repr this sound
    ɥ = Consonant('ɥ', Consonant.Manner.APPROX, Consonant.Place.PALATAL, voiced=True)
    ʢ = Consonant('ʢ', Consonant.Manner.FRICATIVE, Consonant.Place.PHARYNGEAL, voiced=True)
    ʡ = Consonant('ʡ', Consonant.Manner.PLOSIVE, Consonant.Place.PHARYNGEAL, voiced=False)
    ɕ = Consonant('ɕ', Consonant.Manner.FRICATIVE, Consonant.Place.POST_ALVEOLAR, voiced=False)
    ʑ = Consonant('ʑ', Consonant.Manner.FRICATIVE, Consonant.Place.POST_ALVEOLAR, voiced=True)

    ɫ = Consonant('ɫ', Consonant.Manner.LAT_APPROX, Consonant.Place.POST_ALVEOLAR, voiced=True)

    ʧ = Consonant('ʧ', Consonant.Manner.FRICATIVE, Consonant.Place.POST_ALVEOLAR, voiced=False)  # TODO Replace with new affricate type
    ɧ = Consonant('ɧ', Consonant.Manner.FRICATIVE, Consonant.Place.VELAR, voiced=False)

    all = [p, b, t, d, ʈ, ɖ, c, ɟ, k, ɡ, g, q, ɢ, ʔ, m, ɱ, n, ɳ, ɲ, ŋ, ɴ, ʙ, r, ʀ, ʜ, ⱱ, ɾ, ɽ, ɸ, β, f, v, θ, ð, s, z, ʃ, ʒ, ʂ, ʐ, ç, ʝ, x, ɣ, χ, ʁ, ħ, ʕ, h, ɦ, ɬ, ɮ,
           ʋ, ɹ, ɻ, j, ɰ, l, ɭ, ʎ, ʟ, w, ʍ, ɥ, ʢ, ʡ, ɕ, ʑ, ʧ, ɧ, ɫ]


_all_symbols: List[Vowel | Consonant] = [*Vowels.all, *Consonants.all]


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


def lookup(char: str):
    for s in _all_symbols:
        if s.char == char:
            return copy(s)
    return Symbol(char)


def main():
    for x in 'ɮ':
        print(x)


if __name__ == '__main__':
    main()
