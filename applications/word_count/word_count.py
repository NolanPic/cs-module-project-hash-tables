import re

def word_count(s):
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
    return counts

# takes a word and removes unnecessary characters
def clean(word):
    return re.sub('[^a-zA-Z\']', '', word)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count("Hello    hello"))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))