count = 0
h_count = 0
for l in "hello here's letters":
    count = count + 1
    if l == 'h':
        h_count = h_count + 1
print(count, h_count)

### core dict activities

# make an empty dict
d = {}

# add a key/value pair
d['h'] = 0
d['e'] = 0
print(d)
# updating a value
d['h'] = 5
print(d)
# update as in increment
d['h'] = d['h'] + 1
print(d)

# you can also have the key be in a variable
pickme = 'h'
d[pickme] = d[pickme] + 1
print(d[pickme])

# print(d['f']) # will fail, key error

## looping with dicts

text = "hello there fellow human"
# count all the characters in this string into a dict
# prepopulating dictionary
# we can run through all the chars, even the dupes,
# taking advantage that repetition will disappear
counted_chars = {}
for t in text:
    counted_chars[t] = 0
print(counted_chars)
# now count them
for t in text:
    # the "long" way
    # counted_chars[t] = counted_chars[t] + 1
    counted_chars[t] += 1 # the shortcut
print(counted_chars)

## a different way to count, all in one for loop

d1 = {}
text = "hello there fellow human"

for t in text:
    if (t in d1) == False: # checks if the key is in there or not
        # if I haven't seen it yet, I need to add it in
        d1[t] = 1 # 1 because we're looking at one
    else:
        d1[t] = d1[t] + 1
print(d1)

### now we want to only count a certain group of things
vowels_to_count = ['a', 'e','i','o','u', 'y']
vowels = {}
# prepoplated
for v in vowels_to_count:
    vowels[v] = 0 # create our baseline
print(vowels)

for t in text:
    if t in vowels: # if the current char is a key
        vowels[t] += 1 # increment it
print(vowels)