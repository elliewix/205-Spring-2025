import string

text = "Fuzzy-Man, the **cat's** meow, is here!!!"

for punc in string.punctuation:
    text = text.replace(punc, "")
    print(punc, text)

## if want to act at level of word, we need
## to isolate them first

text = "Fuzzy-Man, the **cat's** meow, is here!!!"
# separate words
words = text.split()
print(words)
# isolate words
for w in words:
    print(w.strip(string.punctuation))
    cleaned_word = w.strip(string.punctuation)


#### changing gears
# list accumulator pattern
print("*" * 20)
print("list accumulator patterns")
import random
words = text.split()

print(random.choice(words))

random_word_collection = [] # my base
for i in range(10): # we want to repeat 10 times
    # choose a random word
    w = random.choice(words)
    # print(w)
    # save it to a new list
    # append doesn't use assignment
    random_word_collection.append(w)
print(random_word_collection)

## how to join these words together

l = ['a', 'b','k','a','e','r']
print(l)
print("".join(l))
print("X".join(l))
print("-".join(l))

##
print("our list put together as a sentence")
print(" ".join(random_word_collection))

# outfile pattern

outfile = open('mytext.txt', 'wt', encoding='utf-8')

for i in range(5):
    # oops missing newline!
    # you MAY NOT NEED TO DO THIS FOR HW3
    outfile.write(random.choice(words) + "\n")

outfile.close()