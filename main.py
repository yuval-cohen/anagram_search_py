
from word_list import WordListSet as WordList
from word_list import FindWordRC
from anagram import Anagram, NextAnagramRC

print("reading word-list file... ")
word_list = WordList("word.list")
print("DONE")
#phrase_str = "cat"
#phrase_str = "I'm okay"
#phrase_str = "real fun"
phrase_str = "funeral"
#phrase_str = "you, me, her"
phrase = Anagram(phrase_str)
print("phrase = " + phrase_str)
print("anagrams found:")
next_anagram = list()
while phrase.find_next_anagram() == NextAnagramRC.NEXT_FOUND:
    next_anagram = phrase.get_next_anagram()

    all_anagram_words_found = True
    for word in next_anagram:
        if word_list.find_word(word) != FindWordRC.WORD_FOUND:
            all_anagram_words_found = False
            break
    if all_anagram_words_found:
        print(next_anagram)
