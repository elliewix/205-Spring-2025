data = {'file_name': 'Three-years-in-europe.txt',
        'num_terms': 3,
        'oxford': {'count': 43, 'lines': ['hello oxford']},
        'cat': {'count': 52, 'lines': ['cat was here']},
        'London': {'count': 2, 'lines': ['London is cool']}
        }
# I added some random data

print(data['cat']['count']) # print the count of cat
# increment cat up by 1
data['cat']['count'] += 1
print(data['cat'])
print()# print the lines for London
print()# print the number of terms

terms = ['cat', 'dog']
d = {}
for t in terms:
        d[t] = {'count': 0, 'lines': []}

print(d)