Anagram Search:

A program in python that print anagrams of a given phrase found in a word list file (such as .\word.list).

Anagram is produced by rearranging the letters of a word or a phrase to produce another word or phrase, e.g.:
"funeral" and "real fun"

The program expects the phrase as a parameter to Anagram and prints the results to the standard output. 
To run simply type:
python anagram_search.py <word-list-file> <phrase-str>
e.g.
python anagram_search.py word.list real fun

Comments:
(1) in word_search.py:
    You can choose to import WordList class from either WordListTree or from WordListSet:
    either:
    from word_list import WordListTree as WordList
    or
    from word_list import WordListSet as WordList
