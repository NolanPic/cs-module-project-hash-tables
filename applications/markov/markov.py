import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    

# TODO: analyze which words can follow other words

# hold the analyzed words
word_breakdown = {}
words = words.split()
print(len(words))

for i in range(len(words)):
    word = words[i]
    if word not in word_breakdown:
        # if the word is not in the dict yet, add it
        word_breakdown[word] = []
        
    # check to see if there is a word after this one
    if i + 1 != len(words):
        # there's a word--add it to this word's list
        following_word = words[i+1]
        word_breakdown[word].append(following_word)
        
    

# TODO: construct 5 random sentences
# Your code here



def get_rand_word(array):
    return random.choice(array)

if __name__ == "__main__":
    
    print(word_breakdown)

