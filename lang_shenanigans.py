from data.all_languages import ALL_LANGS, LANGS_TO_USE


def list_by_native_speakers():
    langs_sorted = sorted(LANGS_TO_USE, key=lambda lang: lang.native_speakers)
    for lang in langs_sorted:
        print(f'{lang.name} - Speakers: {lang.native_speakers}')


def main():

    langs_sorted = sorted(ALL_LANGS, key=lambda lang: lang.get_embarrassment_level())
    for lang in langs_sorted:
        print(f'{lang.name} - Embarrassment: {lang.get_embarrassment_level()} - words: {lang.get_word_count()}')
    print('-----\n', len(ALL_LANGS), 'languages and dialects total')
    print(len([l for l in ALL_LANGS if l.get_word_count() >= 10]), 'languages with acceptable data')


if __name__ == '__main__':
    # main()
    list_by_native_speakers()
