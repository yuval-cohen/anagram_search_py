"""This module contains Anagram class that generates
all possible anagrams of a word or phrase.

Attributes:
    none.
"""

import itertools

from enum import Enum

class NextAnagram(Enum):
    """Enum class for the return value of Anagram.find_next_anagram."""
    NO_PHRASE = 1
    PHRASE_TOO_LONG = 2
    NEXT_FOUND = 3
    END_OF_OUTPUT = 4


class Anagram:
    """A class for generating all possible anagrams of a word or phrase.

    E.g.:
    phrase: cat
    All anagrams generated:
        act
        ac t
        a ct
        a c t
        atc
        at c
        a tc
        a t c
        cat
        ca t
        c at
        c a t
        cta
        ct a
        c ta
        c t a
        tac
        ta c
        t ac
        t a c
        tca
        tc a
        t ca
        t c a

    Usage:
        anagram = Anagram("real fun")
        while anagram.find_next_anagram() == NextAnagram.NEXT_FOUND:
            next_anagram = anagram.get_next_anagram()
            ...

    Todo:
        Change to yield next anagram:
        anagram = Anagram("real fun")
        for next_anagram in anagram.get_next_anagram():
            ...

    Attributes:
        _phrase (str) - input phrase
        _root_anagram (str) - single word anagram of phrase
            e.g. if phrase = 'cat' all root anagrams are:
            'act', 'atc', 'cat', 'cta', 'tac' and 'tca'
        _multi_anagram (list) -  list of words as multi-word
            anagram of specific root anagram.
            E.g. root anagram = 'act'
            multi anagrams are: 'a ct', 'ac t' 'a c t' and 'act'
        _multi_anagram_index (int) - index of multi anagram of
            a root anagram.
        _max_phrase_len (int) - maximum phrase length.
    """

    def __init__(self, _phrase = ""):
        """Inits Anagram from an phrase str.

        Args:
            _phrase (str) - multi word phrase string
        """
        self._phrase = _phrase
        self._root_anagram = ""
        self._multi_anagram = []
        self._multi_anagram_index = None
        self._max_phrase_len  = 10


    def set_phrase(self, _phrase):
        """Sets (new) phrase to Anagram object.

        Args:
            _phrase (str) - multi word phrase string

        Returns:
            none
        """
        self._phrase = _phrase
        self._root_anagram = ""
        self._multi_anagram = []
        self._multi_anagram_index = None


    def find_next_anagram(self):
        """Finds the next anagram of the phrase.

        Args:
            none

        Returns:
            NextAnagram.NO_PHRASE - if no phrase
            NextAnagram.PHRASE_TOO_LONG - phrase too long
            NextAnagram.NEXT_FOUND - next anagram found
                (call get_next_anagram to retrieve it)
            NextAnagram.END_OF_OUTPUT - end of output
                (all anagrams found)
        """
        if self._phrase == "":
            return NextAnagram.NO_PHRASE

        if self._root_anagram == "":
            # removes punctuations space and transform to lowercase
            punct_table = str.maketrans("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\"", 32*" ")
            self._root_anagram = self._phrase.translate(punct_table)
            self._root_anagram = self._root_anagram.replace(" ", "")
            self._root_anagram = self._root_anagram.lower()
            if len(self._root_anagram) > self._max_phrase_len :
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
        """Gets next anagram of Anagram object
        following a call of find_next_anagram
        that returns NextAnagram.NEXT_FOUND

        Args:
            none

        Returns:
            _multi_anagram (list) -  multi-word anagram as list of (str) words.
        """
        return self._multi_anagram


    def _next_multi_anagram(self):
        # input: _root_anagram, _multi_anagram_index
        # output: _multi_anagram (list of words)
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
