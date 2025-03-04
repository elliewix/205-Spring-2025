import string

text = "Fuzzy-Man, the **cat's** meow, is here!!!"

for punc in string.punctuation:
    text = text.replace(punc, "")
    print(punc, text)

# this previous version was just taking everything out
# now, we just want the punc on the sides
# leaving the middle intact

text = "Fuzzy-Man, the **cat's** meow, is here!!!"
# separate the data
words = text.split()
print(words)
# now isolate the words
for w in words:
    print(w.strip(string.punctuation))

## switching gears
print("*" * 20)
print("list accumulator pattern")

words = text.split()
import random

random_word_collection = []
for i in range(5):
    w = random.choice(words)
    # print(w) # my random word
    random_word_collection.append(w)
print(random_word_collection)

## connecting strings from a list

l = ['a', 'c','b','u','g']
print(l)
print("".join(l))
print("X".join(l))
print("-".join(l))
print("stuff".join(l))

sentence = " ".join(random_word_collection)
print(sentence)

## writing out files
## outfile pattern

outfile = open('mytext.txt', 'wt', encoding='utf-8')

for i in range(10):
    # in my case I need the newline
    # YOU MAY NOT NEED TO DO THIS FOR HW3
    outfile.write(random.choice(words) + "\n")

outfile.close()
