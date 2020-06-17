import random
import re

# for matching a star word
start_word_match = re.compile("[A-Z]")
#for matching a stop word
stop_word_match = re.compile("([A-Za-z']+)[.!?]")

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    

# TODO: analyze which words can follow other words

# hold the analyzed words
word_breakdown = {}
words = words.split()

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


def generate_sentence(word_breakdown):
    sentence = ''
    # Choose a starting word
    # Keep track of a current word
    # While the current word is not a stop
    # word, keep on going
    # If the current word is a stop word, return
    
    # get the word breakdown as a list of the keys
    word_keys = list(word_breakdown.keys())
    
    start_word = choose_start_word(word_keys)
    # start the current word off at the start word
    current_word = start_word
    # keep track of whether we are inside a quote or not
    in_quote = True if "\"" in current_word else False
    # while the current word is not a stop word and we are not 
    # in the middle of a quote,
    while stop_word_match.search(current_word) is None or in_quote:
        sentence += current_word + ' '
        current_word = choose_next_word(word_breakdown[current_word])
        
        # check to see if this word began a quote
        if "\"" in current_word:
            in_quote = not in_quote # set it to the opposite of itself
    
    # finally, add the last word--this is the stop word
    sentence += current_word
    return sentence
    


def choose_start_word(words):
    rand_word = ""
    
    # while the random word chosen does not match the rules
    # for a starting word,
    while start_word_match.search(rand_word) is None:
        # keep getting a new random word
        rand_word = random.choice(words)
    return rand_word
        
def choose_next_word(array):
    return random.choice(array)

if __name__ == "__main__":
    
    for i in range(5):
        print('\n')
        print(generate_sentence(word_breakdown))
        print('\n')