from data.all_languages import *

LANGS = get_all_langs()


def main():
    print(len(LANGS), 'languages total')
    print(len([l for l in LANGS if l.get_word_count() >= 10]), 'languages with acceptable data')

    langs_sorted = sorted(LANGS, key=lambda lang: lang.get_embarrassment_level())
    for lang in langs_sorted:
        print(f'{lang.name} - Embarrassment: {lang.get_embarrassment_level()} - words: {lang.get_word_count()}')


if __name__ == '__main__':
    main()
