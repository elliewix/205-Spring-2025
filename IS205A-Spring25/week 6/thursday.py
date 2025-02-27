# infile classic

infile = open('stuff.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

lines = text.splitlines()
print(lines)

# readlines pattern

infile = open('stuff.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()

print(lines)

# "infile loop pattern" :-( not my fav

infile = open('stuff.txt', 'rt', encoding='utf-8')
for line in infile:
    print(line)

infile.close()

# let's grab the words

words = text.split()

print(words)

for w in words:
    first_character = w[0]
    last_character = w[-1]
    # print(first_character, last_character)
    if first_character in "aeiou":
        print(w)

# just a preview
print("line 40 break")
for w in words:
    for vowel in "aeiou":
        if w.startswith(vowel):
            print(w)
print("line 45 break")
for vowel in "aeiou":
    for w in words:
        if w.startswith(vowel):
            print(w)

#### back to indexing and slicing
print("indexing examples")
print(words[0]) # first word
print(words[-1]) # last word

print("slicing examples")
print(words[:3]) # first three words
# index on a list you get that exact element
# slice a list and you get a list back
print(words[-3:]) # last three words

print(words[4:8])