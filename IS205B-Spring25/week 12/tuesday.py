# so if our goal is something like
"""
"stuff stuff silly things"
{
 's': ['stuff', 'stuff', 'silly'],
 't': ['things']
}
"""
# let's start with just playing with dicts to see
# what this syntax could look like
d = {}
d['a'] = []
d['b'] = []
print(d)

# let's revisit list stuff
l =[]
l.append('thing1')
l.append('thing2')
l.append('thing3')
print(l)

# how to put these together?
# print(d['a'])
d['a'].append('apple')
print(d)

## setting up the problem


# we're going to ignore that we may have
# empty strings somewhere at some point
sen = "some silly strings are here"
words = sen.split()
collected_words = {}
for w in words:
    # print(w[0]) # this will be our key
    first = w[0]
    if first in collected_words:
        continue
    else:
        collected_words[first] = []
print(collected_words)

# now we proceed with populating the values
print(words)
for w in words:
    first = w[0]
    collected_words[first].append(w)
# store the word count as well
# for i, w in enumerate(words):
#     first = w[0]
#     collected_words[first].append((i, w))

print(collected_words)
# so a diff example, what if we wanted a-z

import string
print(string.ascii_lowercase)
all_letters = {}
for c in string.ascii_lowercase:
    all_letters[c] = []

# print(all_letters)
for w in words:
    first = w[0]
    all_letters[first].append(w)
print(all_letters)

sen = "some more text here and also él"
words = sen.split()
for w in words:
    first = w[0]
    if not (first in all_letters):
        all_letters[first] = []
    all_letters[first].append(w)
print(all_letters)