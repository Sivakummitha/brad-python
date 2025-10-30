#" Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow"
def sort_hyphen_words():
    word_sequence = input("Enter a hyphen-separated sequence of words: ")
    words = word_sequence.split('-')
    words.sort()
    sorted_sequence = '-'.join(words)
    print("Sorted sequence:", sorted_sequence)
sort_hyphen_words()
