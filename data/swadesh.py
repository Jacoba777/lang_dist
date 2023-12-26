from config import ROOT


def _get_swadesh_words():
    with open(f'{ROOT}/data/swadesh.txt', encoding='UTF-8') as f:
        return f.read().split('\n')


SWADESH_WORDS = _get_swadesh_words()
