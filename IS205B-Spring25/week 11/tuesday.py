# a standard kind of counter

count = 0
h_count = 0
text = "here's some stuff"
for t in text:
    count = count + 1
    if t == 'h':
        h_count = h_count + 1
print(count, h_count)

# if we wanted to count everything
# we don't want to have 20+ variables

counted = {}
# but before we can start putting stuff in, we
# need to look at how to do the basics with a dict

# create an empty dict
d = {} # dict()

# add a key/value pair in
# d['key'] = 'value'
d['h'] = 0
d['e'] = 0
print(d)
# update/change a value
d['h'] = 5
print(d)
# increment a value
d['h'] = d['h'] + 1
# a shorthand, does the same thing
d['h'] += 1
print(d)
# just want to see one value
print(d['h'])

pickme = 'h'
print(d[pickme])
d[pickme] = d[pickme] + 1
print(d)

# print(d['pickme']) # gives an error, key doesn't exist
print(d[pickme]) # what i intended

#### so back to our problem

text = "hello there fellow human"
# count all the characters in this
counts = {}
# prepopulate our keys in the dict
for t in text:
    counts[t] = 0
print(counts)
# now we can increment and do the actual counting
for t in text:
    counts[t] =  counts[t] + 1
print(counts)

# doing all this in one phase
# but still counting all the stuff

counts = {}
text = "hello there fellow human"
for t in text:
    # check if we haven't seen it yet
    if (t in counts) == False: # if we haven't seen it yet
        counts[t] = 1 # establish it with 1 because we're looking at one
    else: # but if we have seen it
        counts[t] = counts[t] + 1
print(counts)

## what if we wanted to count just some specific things?

text = "hello there fellow human"
vowels_to_count = ['a','e','i','o','u']

vowels = {}
# prepopulate
for v in vowels_to_count:
    vowels[v] = 0 # establish the key/value

for t in text:
    if t in vowels: # if t is something we want to count
        vowels[t] = vowels[t] + 1

print(vowels)
