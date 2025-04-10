# if something like
"""
{'a': ['apple', 'a'], ...
 'h': ['here', 'hello'], ... }
then I know I can practice a few things to
build this up.
"""

data = {}
# okay add something to the dict
data['a'] = [] # I can add something with a
data['h'] = []
# list as the valu
print(data)
# now we have our keys can we figure out
# how to add stuff in our lists in here?
# going back to lists
l = []
l.append("something")
l.append('in')
l.append('here')
print(l)
# can we put these skills together?

# let's get access to the list

# print(data['a'])
data['a'].append('apple')
print(data)

### okay so let's break out a list of words

sen = "here is a happy home sentence of stuff"
words = sen.split()
print(words)

# let's prepopulate a dict with just the starting
# letters that appear
# for w in words:
#     # let's first find that first char, w[0]
#     if len(w) > 0: # check that the str isn't empty
#         first = w[0]
#

# so let's populate the unique characters
word_data = {}

for w in words:
    if len(w) > 0:
        first = w[0] # this will be my key
    else:
        continue # next iteration if this is empty
    if first in word_data:
        continue # skip if we already have it
    else:
        word_data[first] = [] # establish if we don't

print(word_data)

for w in words:
    if len(w) > 0: # only non empty strings
        first = w[0] # this is our key
        # print(first, word_data[first]) # looks good let's proceed
        word_data[first].append(w) # now use it to add the word
print(word_data)
# if I wanted to preserve the word order, count
word_data = {}
for i, w in enumerate(words):
    if len(w) > 0: # only non empty strings
        first = w[0] # this is our key
        if not (first in word_data):
            word_data[first] = []
        # print(first, word_data[first]) # looks good let's proceed
        word_data[first].append((i, w)) # now use it to add the word
print(word_data)

### so what if we wanted a baseline of a-z
import string
# print(string.ascii_lowercase)
collected_letters = {}
for c in string.ascii_lowercase:
    collected_letters[c] = []
print(collected_letters)
words = "here is another silly sentence of stuff él".split()
for w in words:
    first = w[0]
    if not (first in collected_letters):
        collected_letters[first] = []
    collected_letters[first].append(w)
print(collected_letters)