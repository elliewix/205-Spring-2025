# what does our endgame look like?
"""
{
    'payload': {'a': ['apple', 'and'],
                'b': ['banana']},
        'info': {'original': 'apple and banana'}
}
"""

result = {'payload': {'a': ['apple', 'and'],
                      'b': ['banana']},
          'info': {'original': 'apple and banana'}}

print(result['payload']['b'])
result['payload']['a'].append('ant')
print(result)

###
# so let's built it up

sen = "here are some happy humans maybe who knows"
words = sen.split()
print(words)

# do some prepopulation
data = {}
data['original'] = sen
data['words'] = words.copy() # best practice
data['count'] = len(words)
print(data)
data['payload'] = {}
print(data)

for w in words: # we're not worried about empty strings
    first = w[0]
    data['payload'][first] = [] # letting it overwrite dupes

print(data)
# let's add the words now

for w in words:
    first = w[0]
    data['payload'][first].append(w)
print(data)

# writing this out a json file
# only do this when your dict is ready to go
import json # normally do this at the top
outfile = open('data.json', 'wt', encoding='utf-8')
json.dump(data, outfile, indent=4) # dictionary, outfile, say indent = 4
outfile.close()

# let's read that file in and get data from it

infile = open('data.json', 'rt', encoding='utf-8')
loaded_data = json.load(infile)
infile.close()
print(loaded_data)
