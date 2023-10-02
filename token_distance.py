from model.ipa_dictionary import Consonant, Vowel, Diphthong, Vowels

DIST_SAME_SYMBOL_TYPE_MULTIPLIER = 1


def _dist_default():
    return 1.0


def _dist_vowels_old(t1: Vowel, t2: Vowel):
    f1 = 0.40 * abs(t1.frontage - t2.frontage) / 4
    f2 = 0.40 * abs(t1.openness - t2.openness) / 6
    f3 = 0.20 * (0 if t1.rounded == t2.rounded else 1)
    return (f1 + f2 + f3) * DIST_SAME_SYMBOL_TYPE_MULTIPLIER


def _dist_vowels(t1: Vowel, t2: Vowel):
    f1_dist = ((t1.f1-t2.f1) / (Vowels.y.f1 - Vowels.a.f1))**2
    f2_dist = ((t1.f2-t2.f2) / (Vowels.u.f2 - Vowels.i.f2))**2

    formant_dist = (f1_dist + f2_dist)**0.5 / 1.1768543475538389

    f1 = 0.80 * formant_dist
    f2 = 0.20 * (0 if t1.rounded == t2.rounded else 1)
    return (f1 + f2) * DIST_SAME_SYMBOL_TYPE_MULTIPLIER


def _dist_consonants(t1: Consonant, t2: Consonant):
    f1 = 0.40 * (0 if t1.manner == t2.manner else 1)
    f2 = 0.40 * abs(t1.place - t2.place) / 6
    f3 = 0.20 * (0 if t1.voiced == t2.voiced else 1)
    return (f1 + f2 + f3) * DIST_SAME_SYMBOL_TYPE_MULTIPLIER


def _dist_diphthongs(t1: Diphthong, t2: Diphthong):
    return _dist_vowels(t1.v1, t2.v1) + _dist_vowels(t1.v2, t2.v2)


def _dist_diphthong_vowel(t1: Diphthong, t2: Vowel):
    return _dist_vowels(t1.v1, t2) + _dist_vowels(t1.v2, t2)


def token_distance(t1, t2):
    if type(t1) == Vowel and type(t2) == Vowel:
        return _dist_vowels(t1, t2)

    if type(t1) == Consonant and type(t2) == Consonant:
        return _dist_consonants(t1, t2)

    if type(t1) == Diphthong and type(t2) == Diphthong:
        return _dist_diphthongs(t1, t2)

    if type(t1) == Diphthong and type(t2) == Vowel:
        return _dist_diphthong_vowel(t1, t2)
    if type(t1) == Vowel and type(t2) == Diphthong:
        return _dist_diphthong_vowel(t2, t1)

    return _dist_default()


def temp_test_vowel_dists():

    vowels = Vowels.all


    vowel_pairs = []
    for i1, v1 in enumerate(vowels):
        vowel_pairs_partial = [(v1, v2, token_distance(v1, v2)) for i2, v2 in enumerate(vowels[i1+1:])]
        vowel_pairs.extend(vowel_pairs_partial)

    vowel_pairs.sort(key=lambda x: x[2])

    print(vowel_pairs)

    vowels.sort(key=lambda v: v.f1)
    print(vowels)
    vowels.sort(key=lambda v: v.f2)
    print(vowels)


def test_dists():
    new_vowel = Vowel('x', Vowel.Frontage.NEAR_BACK, Vowel.Openness.NEAR_OPEN, rounded=True)
    diph = Diphthong(Vowels.a, Vowels.i)

    print(token_distance(diph, new_vowel))


def main():
    temp_test_vowel_dists()


if __name__ == '__main__':
    main()
