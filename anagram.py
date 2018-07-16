

from enum import Enum

class NextAnagram(Enum):
    NO_PHRASE = 1
    PHRASE_TOO_LONG = 2
    NEXT_FOUND = 3
    END_OF_OUTPUT = 4


import itertools

class Anagram:

    def __init__(self, _phrase = ""):
        self._phrase = _phrase
        self._root_anagram = ""
        self._multi_anagram = []
        self._multi_anagram_index = None
        self._max_anagram_len = 10


    def reset_phrase(self, _phrase):
        self._phrase = _phrase
        self._root_anagram = ""
        self._multi_anagram = []
        self._multi_anagram_index = None


    def find_next_anagram(self):
        if self._phrase == "":
            return NextAnagram.NO_PHRASE

        if self._root_anagram == "":
            # removes punctuations space and transform to lowercase
            punct_table = str.maketrans("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\"", 32*" ")
            self._root_anagram = self._phrase.translate(punct_table)
            self._root_anagram = self._root_anagram.replace(" ", "")
            self._root_anagram = self._root_anagram.lower()
            if len(self._root_anagram) > self._max_anagram_len:
                return NextAnagram.PHRASE_TOO_LONG

            # create initial root anagram */
            self._root_anagram = "".join(sorted(self._root_anagram))
            self._multi_anagram_index = 0
            self._permutations = itertools.permutations(self._root_anagram)
            self._permutations.__next__()
        elif self._multi_anagram_index == (pow(2, len(self._root_anagram) - 1)):
            try:
                next_permutation = self._permutations.__next__()
                self._root_anagram = "".join(next_permutation)
                self._multi_anagram_index = 0
            except StopIteration:
                return NextAnagram.END_OF_OUTPUT

        self._next_multi_anagram()

        return NextAnagram.NEXT_FOUND


    def get_next_anagram(self):
        return self._multi_anagram


    def _next_multi_anagram(self):
        # input: _root_anagram, _multi_anagram_index
        # output: _multi_anagram with all words
        self._multi_anagram = list()

        if self._multi_anagram_index == 0:
            self._multi_anagram.append(self._root_anagram)
        else:
            multi_anagram_index_bit = 1
            start = 0
            end = 0
            while multi_anagram_index_bit < pow(2, len(self._root_anagram)):
                if self._multi_anagram_index & multi_anagram_index_bit:
                    self._multi_anagram.append(self._root_anagram[start:end+1])
                    start = end + 1
                multi_anagram_index_bit <<= 1
                end += 1
            self._multi_anagram.append(self._root_anagram[start:end])
        self._multi_anagram_index += 1
