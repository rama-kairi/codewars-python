# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

import string


# With for loop
def highest_scoring_word(words: str) -> str:
    words = words.split(" ")
    words_scores = []
    for word in words:
        score = sum(string.ascii_lowercase.index(letter) + 1 for letter in word)
        words_scores.append((word, score))
    words_scores.sort(key=lambda x: x[1], reverse=True)
    return words_scores[0][0]


# With List Comprehension
def highest_scoring_word_lc(words: str) -> str:
    words = words.split(" ")
    words_scores = [
        (word, sum(string.ascii_lowercase.index(letter) + 1 for letter in word)) for word in words
    ]
    words_scores.sort(key=lambda x: x[1], reverse=True)
    return words_scores[0][0]


# One line Solution
def highest_scoring_word_oneliner(words: str) -> str:
    return max(
        words.split(" "),
        key=lambda x: sum(string.ascii_lowercase.index(letter) + 1 for letter in x),
    )


# Tests
print(highest_scoring_word("what time are we climbing up the volcano"))
print(highest_scoring_word_lc("what time are we climbing up the volcano"))
print(highest_scoring_word_oneliner("what time are we climbing up the volcano"))
