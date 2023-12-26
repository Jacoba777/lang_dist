from model.phone import Phone, get_phone_by_symbol


def get_phones_in_use():
    symbols = set()
    with open('ipa_symbol_mess', encoding='UTF-8') as f:
        txt = f.read()
    for s in txt:
        if s not in ['\t', '\n']:
            symbols.add(s)
    print(sorted(symbols))
    print(sorted([s for s in symbols if type(get_phone_by_symbol(s)) == Phone]))


def main():
    get_phones_in_use()


if __name__ == '__main__':
    main()
