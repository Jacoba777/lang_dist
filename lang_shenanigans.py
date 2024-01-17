from data.all_languages import *

LANGS = get_all_langs()


def main():
    print(len(LANGS))
    langs_sorted = sorted(LANGS, key=lambda lang: lang.get_embarrassment_level())
    for lang in langs_sorted:
        print(f'{lang.name} - Embarrassment: {lang.get_embarrassment_level()}')


if __name__ == '__main__':
    main()
