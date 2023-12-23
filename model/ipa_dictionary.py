from copy import copy
from typing import List

from model.token import Symbol, Vowel, Consonant, Modifier, Diphthong


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


class Modifiers:
    a͡ = Modifier('͡', fix_type=Modifier.FixType.AFFRICATE)

    sup_1 = Modifier('¹', fix_type=Modifier.FixType.WORD_LEVEL_PRE)
    sup_2 = Modifier('²', fix_type=Modifier.FixType.WORD_LEVEL_PRE)

    ˈ = Modifier('ˈ', fix_type=Modifier.FixType.SYLLABLE_LEVEL_PRE)
    ˌ = Modifier('ˌ', fix_type=Modifier.FixType.SYLLABLE_LEVEL_PRE)
    period = Modifier('.', fix_type=Modifier.FixType.SYLLABLE_LEVEL_PRE)

    ʰ = Modifier('ʰ', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    ˢ = Modifier('ˢ', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    ʷ = Modifier('ʷ', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    ː = Modifier('ː', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    ˀ = Modifier('ˀ', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    â = Modifier('̂', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    ã = Modifier('̃', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    ä = Modifier('̈', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    å = Modifier('̊', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̚ = Modifier('̚', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̞ = Modifier('̞', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̟ = Modifier('̟', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̠ = Modifier('̠', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    ḁ = Modifier('̥', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̩ = Modifier('̩', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̪ = Modifier('̪', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̯ = Modifier('̯', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̹ = Modifier('̹', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a̽ = Modifier('̽', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)
    a͈ = Modifier('͈', fix_type=Modifier.FixType.SYMBOL_LEVEL_POST)

    all = [a͡, sup_1, sup_2, ˈ, ˌ, period, ʰ, ˢ, ʷ, ː, ˀ, â, ã, ä, å, a̚, a̞, a̟, a̠, ḁ, a̩, a̪, a̯, a̹, a̽, a͈]


_all_symbols: List[Vowel | Consonant | Modifier] = [*Vowels.all, *Consonants.all, *Modifiers.all]


def lookup(char: str):
    for s in _all_symbols:
        if s.char == char:
            return copy(s)
    return Symbol(char)


def get_ipa_tokenization(ipa):
    symbols = [lookup(c) for c in ipa]
    tokens = []

    for i, symbol in enumerate(symbols):
        if type(symbol) == Symbol:
            print(f'{symbol} unrecognized, skipping')
            continue

        elif len(tokens) > 0:
            prev_symbol = tokens[-1]

            if type(symbol) == Modifier:
                if symbol.fix_type == Modifier.FixType.WORD_LEVEL_PRE:
                    # TODO do this
                    print(f'{symbol} is a word-level modifier, which is not supported yet. Skipping')
                    continue
                if symbol.fix_type == Modifier.FixType.SYMBOL_LEVEL_POST:
                    prev_symbol.add_modifier(symbol)
                    continue
                if symbol.fix_type == Modifier.FixType.AFFRICATE:
                    # TODO do this
                    print(f'{symbol} is an affricate, which is not supported yet. Skipping')
                    continue

            if type(prev_symbol) == Vowel and type(symbol) == Vowel:
                tokens.remove(prev_symbol)
                d = Diphthong(prev_symbol, symbol)
                tokens.append(d)
                continue

        tokens.append(symbol)

    return tokens


def main():
    for x in 'ɮ':
        print(x)


if __name__ == '__main__':
    main()
