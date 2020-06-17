# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Go through each character in the text and count how many times
# it is used in the document.
# When done counting, order the the list from highest usage to lowest
# Compare to the order in the readme

# I need to be able to go through each character in the text and do something like:
# encoded_char = 'e'
# decoded_char = mapping[encoded_char]

# what do I need to do to get here?

# Have a "truth" LIST that is the alphabet sorted by most use

# Create a hash table that has a count of each character
# turn it into a list sorted by most use

# Loop thru the encoded list and find the decoded char at the same
# index on the truth list

import re

letter = re.compile("[A-Z]")

# truth is the alphabet ordered by standard/common usage of each character
truth = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

"""
Takes some text and returns a sorted count of how many times
each character is used
"""
def build_sorted_char_counts(text):
    counts = {}
    # split the text into characters
    characters = list(text)
    
    for char in characters:
        # ensure we only add alpha chars
        if letter.search(char) is not None:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
            
    # sort the characters by their count (usage)              count
    sorted_chars = sorted(list(counts.items()), key=lambda x: x[1], reverse=True)
    
    return sorted_chars

"""
Takes a list of encoded chars sorted by usage (desc)
and uses it to create a mapping from encoded char -> decoded char
"""
def create_mapping_from_sorted_chars(sorted_encoded_chars):
    mapping = {}
    for i in range(len(truth)):
        # sorted_encoded_chars is a list of tuples [(key, val)]
        encoded_char = sorted_encoded_chars[i][0]
        mapping[encoded_char] = truth[i]
    return mapping

"""
Takes some encoded text and a mapping, and uses the mapping
to decode each character of the  text
"""
def decode_text_with_mapping(encoded_text, mapping):
    decoded_text = ''
    characters = list(encoded_text)
    
    for char in characters:
        if letter.search(char) is not None:
            # this is an alpha char --> decode
            decoded_text += mapping[char]
        else: # this is a space or non-alpha char
            decoded_text += char
            
    return decoded_text


def main():
    with open("ciphertext.txt") as f:
        text = f.read()
        
    # get a list of encoded characters sorted by their usage
    sorted_ecoded_cars = build_sorted_char_counts(text)
    # get a mapping of encoded chars -> decoded chars
    mapping = create_mapping_from_sorted_chars(sorted_ecoded_cars)
    
    decoded_text = decode_text_with_mapping(text, mapping)
    print(decoded_text)
    
    f = open("decoded.txt", "w")
    f.write(decoded_text)
    f.close()

if __name__ == "__main__":
    main()




