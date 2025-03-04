import random

infile = open('stuff.txt', 'rt')
words = infile.read().split()
infile.close()

my_random_words = []

for i in range(20):
    w = random.choice(words)
    my_random_words.append(w)

print(my_random_words)

