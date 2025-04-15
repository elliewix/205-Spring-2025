# let's look at our endgame

result = {'original': "some text",
          'split': ['some', 'words'],
          'count': 2,
          'payload': {'a': ['apple', 'and'],
                      'b': ['banana']}
          }

# let's see the original value
print(result['original'])
print(result['count'])
print(result['payload']) # see the payload
print(result['payload']['b']) # see the list of b

# add something into the key of a
result['payload']['a'].append('ant')
result['count'] += 1
print(result)

# let's build this up
sen = "hello happy humans okay maybe not who knows"
words = sen.split()
data = {}
data['original'] = sen
data['words'] = words.copy() # best practice
data['count'] = len(words)
data['payload'] = {}
print(data)

# let's prepopulate the payload dictionary
for w in words:
    first = w[0] #we're not going to worry about empty strings
    # just overwrite dupes
    data['payload'][first] = []

print(data)

# increment up our dictionary

for w in words:
    first = w[0]
    data['payload'][first].append(w)

print(data)

# let's get this into a json file now
# only do this when your dict is completely ready to go

import json # normally do this at the top of your script

outfile = open('data.json', 'wt', encoding='utf-8')
json.dump(data, outfile, indent=4) # your dict, the outfile, indent of 4
outfile.close()

# the other way around

infile = open('data.json', 'rt', encoding='utf-8')
loaded_data = json.load(infile)
infile.close()

print(loaded_data['words'])