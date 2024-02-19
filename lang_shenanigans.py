from typing import List, Tuple

from data.all_languages import ALL_LANGS
from data.lang_swadesh_lists import LANGS_TO_USE
from data.germanic import ENGLISH_US
from model.lang import Language
from model.lang_dist import calculate_lang_dist


def list_by_native_speakers(langs: List[Language]):
    return sorted(langs, key=lambda lang: lang.native_speakers, reverse=True)


def list_by_lowest_embarrassment(langs: List[Language]):
    return sorted(langs, key=lambda lang: lang.get_embarrassment_level())


def list_by_plot_order(langs: List[Language]):
    return sorted(langs, key=lambda lang: lang.native_speakers * (lang.get_word_count()/207), reverse=True)


def transform_distance_to_graph_diameter(distance: float) -> int:
    # return int((2**(distance*10) - 1) * 5)
    return int(distance * 100 * 20)


def get_nearest_two_with_distance():
    langs = list_by_plot_order(LANGS_TO_USE)
    langs_done: List[Language] = []

    for lang in langs:
        dists: List[Tuple[Language, float, float]] = [(l2, *calculate_lang_dist(lang, l2)) for l2 in langs_done if lang != l2]
        dists.sort(key=lambda x: x[1])
        for i in range(min(len(dists), 2)):
            lang_near, dist, moe = dists[i]
            print(f'{lang}->{lang_near} = {transform_distance_to_graph_diameter(dist)} ({dist:.4f} += {moe:.4f})')
        langs_done.append(lang)


def get_fixed_lang_dist():
    lang_fixed = ENGLISH_US

    langs = list_by_plot_order(LANGS_TO_USE)
    langs_done: List[Language] = []

    for lang in langs:
        dists: List[Tuple[Language, float, float]] = [(l2, *calculate_lang_dist(lang, l2)) for l2 in langs_done if l2 not in [lang_fixed, lang]]
        dists.sort(key=lambda x: x[1])

        dist_fixed = calculate_lang_dist(lang, lang_fixed)
        dist, moe = dist_fixed
        print(f'{lang}->{lang_fixed} = {transform_distance_to_graph_diameter(dist)} ({dist:.4f} +/- {moe:.4f})')

        for i in range(min(len(dists), 1)):
            lang_near, dist, moe = dists[i]
            print(f'{lang}->{lang_near} = {transform_distance_to_graph_diameter(dist)} ({dist:.4f} +/- {moe:.4f})')
        langs_done.append(lang)


def main():
    langs_sorted = list_by_lowest_embarrassment()
    for lang in langs_sorted:
        print(f'{lang.name} - Embarrassment: {lang.get_embarrassment_level()} - words: {lang.get_word_count()}')
    print('-----\n', len(ALL_LANGS), 'languages and dialects total')
    print(len([l for l in ALL_LANGS if l.get_word_count() >= 10]), 'languages with acceptable data')


if __name__ == '__main__':
    # main()
    get_fixed_lang_dist()
