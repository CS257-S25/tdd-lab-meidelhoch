import sys

'''
A file for the production code
'''


def reverse_word(word):
    '''
    A function that reverses a word.
    '''
    reversed_word = ""
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word


def reverse_all_words(words):
    words_array = words.split(" ")
    reversed_words = [reverse_word(word) for word in words_array]
    return " ".join(reversed_words)


def main():
    '''
    A function that reverses all words in a string from command line input.
    '''
    if len(sys.argv) > 1:
        words = sys.argv[1]
        reversed_words = reverse_all_words(words)
        print(reversed_words)
    else:
        print("Please provide a string to reverse.")
