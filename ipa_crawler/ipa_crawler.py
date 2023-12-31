import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://en.wiktionary.org/wiki'
LANG = 'Ukrainian'
WORD = '我'


def get_word_ipa(word: str, lang: str):
    url = f'{BASE_URL}/{word}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    lang_header = soup.find("span", class_="mw-headline", id=lang)

    if lang_header is None:
        return f'[ERROR] Could not find word "{word}" in lang "{lang}"'

    curr_element = lang_header
    while curr_element:
        curr_element = curr_element.find_next()

        if curr_element is None or curr_element.name == 'h2':
            return f'[ERROR] Missing IPA section for word "{word}" in lang "{lang}"'

        if curr_element.name == 'span' and curr_element.get('class') and 'IPA' in curr_element.get('class'):
            return curr_element.text


def debug_get_word_ipa(word: str, lang: str):
    res = get_word_ipa(word, lang)
    print(res)
    if res.startswith('[ERROR]'):
        return ''

    return res.strip('/[]\\')


def convert_input_words_to_ipa():
    with open('ipa_crawler/input.txt', encoding='UTF-8') as f:
        words = f.read().split('\n')

    ipas = [debug_get_word_ipa(w, LANG) for w in words]
    print(ipas)

    with open('ipa_crawler/output.txt', 'w', encoding='UTF-8') as f:
        for ipa in ipas:
            f.write(ipa)
            f.write('\n')


def main():
    convert_input_words_to_ipa()
    # word = get_word_ipa(WORD, LANG)
    # print(word)


if __name__ == '__main__':
    main()
