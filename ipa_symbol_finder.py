from model.ipa_dictionary import lookup
from model.token import Symbol


def ipa_tokenizer(ipa: str):
    tokens = []
    for char in ipa:
        symbol = lookup(char)


def get_symbols():
    symbols = set()
    with open('ipa_symbol_mess', encoding='UTF-8') as f:
        txt = f.read()
    for s in txt:
        if s not in ['\t', '\n']:
            symbols.add(s)
    print(sorted(symbols))
    print(sorted([s for s in symbols if type(lookup(s)) == Symbol]))


def main():
    get_symbols()


if __name__ == '__main__':
    main()
