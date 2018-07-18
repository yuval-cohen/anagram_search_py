#!/usr/bin/env python3
"""A program searches all anagrams of a word or phrase that its
words can be found in an input word-list UTF-8 text file.
The program prints all those anagrams to the standard output.

Example:
    phrase: real fun
    input file: .\word.list
    python anagram_search.py word.list real fun

Attributes:
    none
"""

import sys
from word_list import WordListSet as WordList, FindWord
from anagram import Anagram, NextAnagram

def create_word_list(file_name):
    """Creates WordList object from  input word-list text file.

    Args:
        file_name (str) - full path input word-list UTF-8 text file
            each word in single line.

    Returns:
         The created WordList object
    """
    print("creating word-list from "+str(file_name)+ " file... ")
    word_list = WordList("word.list")
    print("[DONE]")
    return word_list


def print_all_anagrams_in_word_list(phrase_str, word_list):
    """Prints all anagrams of a phrase that its words found in word list.

    Args:
        phrase_str (str) - phrase
        word_list (WordList) - WordList object already created

    Returns:
         none
    """
    phrase = Anagram(phrase_str)
    next_anagram = list()
    print("anagrams found:")
    while phrase.find_next_anagram() == NextAnagram.NEXT_FOUND:
        next_anagram = phrase.get_next_anagram()
        all_anagram_words_found = True
        for word in next_anagram:
            if word_list.find_word(word) != FindWord.WORD_FOUND:
                all_anagram_words_found = False
                break
        if all_anagram_words_found:
            print(next_anagram)


def main(phrase_str, file_name):
    """The main function of anagram_search program.

    Args:
        phrase_str (str) - phrase
            e.g.:
                'cat'
                'I'm okay'
                'funeral'
                'real fun'
                'you, me, her'
        file_name (str) - full path input word-list UTF-8 text file
            each word in single line.

        Returns:
            none
    """
    word_list = create_word_list(file_name)
    print_all_anagrams_in_word_list(phrase_str, word_list)


# examples for phrases: cat, I'm okay, funeral, real fun, 'you, me, her'
if __name__ == "__main__":
    file_name = sys.argv[1]
    phrase_str = " ".join(sys.argv[2:])
    print("phrase = " + phrase_str)
    main(phrase_str, file_name)
