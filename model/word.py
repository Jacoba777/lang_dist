from typing import List

from model.ipa_dictionary import Vowel, Symbol, lookup, Diphthong, Token


class TokenizedWord:
    def __init__(self, ipa: str = '', tokens: List[Token] | None = None):
        self.tokens = self._get_ipa_tokenization(ipa) if not tokens else tokens

    def __iter__(self):
        return self.tokens.__iter__()

    def __len__(self):
        return len(self.tokens)

    def __repr__(self):
        s = ''
        for token in self.tokens:
            s += token.__repr__()
        return s

    def __eq__(self, other):
        if len(self.tokens) != len(other.tokens):
            return False
        for i, token in enumerate(self.tokens):
            if token != other.tokens[i]:
                return False
        return True

    def starts_with(self, tokens):
        if len(tokens) > len(self.tokens):
            return False
        for i, token in enumerate(tokens):
            if self.tokens[i] != token:
                return False
        return True

    @staticmethod
    def _get_ipa_tokenization(ipa):
        symbols = [lookup(c) for c in ipa]
        tokens = []

        for i, symbol in enumerate(symbols):
            if type(symbol) == Symbol:
                print(f'{symbol} unrecognized, skipping')
                continue

            elif len(tokens) > 0:
                prev_symbol = tokens[-1]

                if type(prev_symbol) == Vowel and type(symbol) == Vowel:
                    tokens.remove(prev_symbol)
                    d = Diphthong(prev_symbol, symbol)
                    tokens.append(d)
                    continue

            tokens.append(symbol)

        return tokens


# still need to add word to weighted lev 2 and refactor to use this instead of strings
class Word:
    def __init__(self, spelling: str = '', ipa: str = ''):
        self.spelling = spelling
        self.ipa = ipa
        self.ipa_tokenized: TokenizedWord = TokenizedWord(self.ipa)


def main():
    w = TokenizedWord('faʊ̯l')
    w2 = TokenizedWord('faʊ̯')

    print(w.starts_with(w2))


if __name__ == '__main__':
    main()
