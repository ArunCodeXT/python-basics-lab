text = "python for data science"
words = text.split()   # split into list of words
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("Longest word:", longest_word)
