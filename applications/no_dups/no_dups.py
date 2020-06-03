# loop thru split string
#     if word not in cache
#         add to new string
#     add word to cache

def no_dups(s):
    cache = {}
    # split string by space into array of words
    words = s.split()
    new_s = ''
    for word in words:
        if word not in cache:
            # build the new string with no dupes
            new_s += word + ' '
            cache[word] = True
    return new_s.rstrip() # <- trim the last trailing space off the end


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))