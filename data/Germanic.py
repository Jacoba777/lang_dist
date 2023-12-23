from model.lang import Language

FAMILY = 'germanic'

ENGLISH = Language('english', FAMILY, 372900000, 1080000000)
GERMAN = Language('german', FAMILY, 95000000, 83000000)
GOTHIC = Language('gothic', FAMILY, 0, 0)


if __name__ == '__main__':
    print(GERMAN.get_word('to sleep').ipa)
