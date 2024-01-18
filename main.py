from math import inf

from data.all_languages import *
from model.difference_scores import DifferenceScores
from model.lang import Language
from model.lang_dist import LanguageDistances, calculate_word_dists
from model.node import Node


def get_words_by_similarity(lang_name_1: str, lang_name_2: str):
    langs = get_all_langs()
    l1 = next(lang for lang in langs if lang.name == lang_name_1)
    l2 = next(lang for lang in langs if lang.name == lang_name_2)
    word_dists = calculate_word_dists(l1, l2)
    word_dists.sort(key=lambda w: w[2])
    print(word_dists)


def show_relative_distance(lang_name: str, lang_name_1: str, lang_name_2: str):
    langs = get_all_langs()
    l = [lang for lang in langs if lang.name == lang_name][0]
    l1 = [lang for lang in langs if lang.name == lang_name_1][0]
    l2 = [lang for lang in langs if lang.name == lang_name_2][0]
    word_dists_1 = calculate_word_dists(l, l1)
    word_dists_2 = calculate_word_dists(l, l2)

    matches = []
    for word in word_dists_1:
        for word2 in word_dists_2:
            if word[0] == word2[0]:
                matches.append((word, word2))

    formatted_compare = [(w[0][0], w[0][1], w[1][1], w[0][2] - w[1][2]) for w in matches]
    formatted_compare.sort(key=lambda x: x[3])
    for w in formatted_compare:
        print(w)

    l_dists = [w[3] for w in formatted_compare]

    abs_diff = sum(l_dists) / len(l_dists)
    print("Average relative distance:", abs_diff)


def get_closest_langs(lang_name: str):
    langs = get_all_langs()
    compare_lang = [lang for lang in langs if lang.name == lang_name][0]
    lang_dists = LanguageDistances(langs)

    en_dists = [(lang_dists.get_dist(compare_lang, lang), lang.name) for lang in langs]
    en_dists.sort()

    for dist in en_dists:
        print(f"{dist[1]}: {(1-dist[0])*100:.1f}%")


def get_lang_dist_pairs():
    langs = [*DRAVIDIAN]
    # langs = get_all_langs()
    print(langs)
    lang_dists = LanguageDistances(langs).get_all_dists()
    lang_dists.sort()

    dist_scores = DifferenceScores()

    for (x, margin_of_error), langs in lang_dists:
        moe_min = max(x-margin_of_error, 0)
        moe_max = min(x+margin_of_error, 1)
        print(f"{langs}: {x*100:.1f}% ({moe_min*100:.1f}% - {moe_max*100:.1f}%)")
        dist_scores.set_score(langs[0].name, langs[1].name, x)
    dist_scores.save_as("lang_dist_scores.pickle")


def get_cluster_hierarchy():
    lang_dists = DifferenceScores.load_from_file("lang_dist_scores.pickle")
    langs = lang_dists.get_entity_names()

    root = [lang for lang in langs]

    while len(root) > 1:
        min_cost, min_l1, min_l2 = inf, None, None
        for i, l1 in enumerate(root):
            for l2 in root[i+1:]:
                potential_node = Node([l1, l2])
                cost = potential_node.compute_cost(lang_dists)
                if cost < min_cost:
                    min_cost, min_l1, min_l2 = cost, l1, l2
        print(f"Best pair to node: ({min_l1}, {min_l2}) | Cost: {min_cost}")
        root.remove(min_l1)
        root.remove(min_l2)
        root.append(Node([min_l1, min_l2]))
    root[0].pprint(lang_dists)


def get_cluster_hierarchy_v2():
    lang_dists = DifferenceScores.load_from_file("lang_dist_scores.pickle")
    langs = lang_dists.get_entity_names()

    root = []
    root.extend([lang for lang in langs])

    while len(root) > 1:
        min_cost, min_l1, min_l2 = inf, None, None
        for i, l1 in enumerate(root):
            for l2 in root[i+1:]:
                if type(l1) == str and type(l2) == str:

                    cost = Node([l1, l2]).compute_cost(lang_dists)
                else:
                    if type(l1) == Node:
                        cost = l1.compute_union_cost(lang_dists, l2)
                    else:
                        cost = l2.compute_union_cost(lang_dists, l1)

                if cost < min_cost:
                    min_cost, min_l1, min_l2 = cost, l1, l2
        print(f"Best pair to node: ({min_l1}, {min_l2}) | Cost: {min_cost}")
        root.remove(min_l1)
        root.remove(min_l2)
        root.append(Node([min_l1, min_l2]))
    root[0].pprint(lang_dists)


def func(langs_to_cluster: List[Language], lang_dists: LanguageDistances):
    max_dist = 0
    for i, lang1 in enumerate(langs_to_cluster):
        for lang2 in langs_to_cluster[i+1:]:
            max_dist = max(max_dist, lang_dists.get_dist(lang1, lang2))
    return max_dist


def func2():
    langs = get_all_langs()
    lang_dists = LanguageDistances(langs)

    res = []
    count = 0
    for i in range(0, 2**len(langs)):
        cluster_langs = [lang for j, lang in enumerate(langs) if i//(2**j) % 2 == 0]
        if len(cluster_langs) > 2:
            res.append((func(cluster_langs, lang_dists)/len(cluster_langs), cluster_langs))
            count += 1
    res.sort()
    for r in res:
        print(r)


def node_compare():
    lang_dists = DifferenceScores.load_from_file("lang_dist_scores.pickle")
    slavs = Node(['RUSYN', 'UKRAINIAN', 'RUSSIAN', 'BELARUSIAN', 'POLISH', 'LOWER SORBIAN', 'UPPER SORBIAN', 'CZECH', 'SLOVAK', 'SERBO-CROAT', 'SLOVENE', 'BULGARIAN', 'MACEDONIAN'])
    baltics = Node(['OLD PRUSSIAN', 'LITHUANIAN', 'LATVIAN', 'LATGALIAN'])

    n1 = Node([slavs, baltics])
    n2 = Node([baltics, 'GREEK'])

    print("N1 cost:", n1.compute_cost(lang_dists))
    print("N2 cost:", n2.compute_cost(lang_dists))


if __name__ == '__main__':
    # get_words_by_similarity("Italian", "English")
    # show_relative_distance('English', 'Dutch', 'WestFrisian')
    # get_closest_langs("Spanish")
    get_lang_dist_pairs()
    # get_cluster_hierarchy_v2()
    # node_compare()
