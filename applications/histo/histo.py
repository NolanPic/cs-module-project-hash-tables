import re

with open("robin.txt") as f:
    words = f.read()

# lookup table for number-to-hashmarks
hashmarks = {}
def gen_hashmark_lookup(length):
    for i in range(1, length+1):
        hashes = ''
        for __ in range(i):
            hashes += '#'
        hashmarks[i] = hashes

def get_sorted_word_counts(s):
    
    counts = {}
    
    # split the string by spaces to get all words
    words = s.split()
    for word in words:
        
        # clean and lowercase the word
        word = clean(word.lower())
        if word in counts:
            counts[word] += 1
        elif len(word) > 0:
            counts[word] = 1
            
    # now sort by count, word                                       count  word
    sorted_counts = dict(sorted(list(counts.items()), key=lambda x: (x[1], x[0]), reverse=True))
    return sorted_counts

def clean(word):
    return re.sub('[^a-zA-Z\']', '', word)

def print_histo(sorted_word_counts):
    
    for i in sorted_word_counts.items():
        word = i[0]
        count = i[1]
        print(f'{word:20}{hashmarks[count]}')
    



if __name__ == "__main__":
    gen_hashmark_lookup(len(words))
    sorted_counts = get_sorted_word_counts(words)
    
    print('\n')
    print_histo(sorted_counts)   
    