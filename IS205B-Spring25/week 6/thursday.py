# read() pattern, classic infile

infile = open('stuff.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

lines = text.splitlines()
print(lines)
words = text.split()
print(words)

## we can also use readlines
# shortcut right to lines
infile = open('stuff.txt', 'rt', encoding='utf-8')
lines = infile.readlines()
infile.close()
print(lines)

## infile loop pattern
# please don't use this
infile = open('stuff.txt','rt', encoding='utf-8')
for line in infile:
    print(line)
infile.close()

#####

words = text.split()

for w in words:
    first_letter = w[0]
    last_letter = w[-1]
    print(first_letter, last_letter)

## indexing examples
print("indexing")

print(words[5])
print(words[7])

print("slicing")
print(words[5:7])

# omit start, presumes from the beginning
print(words[:7]) # first 7 words form the list
# omit stop, presumes to the end
print(words[11:])

# "the last number of things"
print(words[-3:-1])

# step
print("hello"[1:4])
print("hello"[-4:4])
# don't do dumb stuff
print("hello"[-4:-1])
print("hello"[-2:-5:-1])
print("hello"[-5:-2:-1]) # empty string

print("hello"[:2] + "hello"[1:3])

### loops again with filtering
print("find vowels")
for w in words:
    first = w[0]
    if first in "aeiou":
        print(w)

###
for w in words:
    for vowel in "aeiou":
        if w.startswith(vowel):
            print(w)

for vowel in "aeiou":
    for w in words:
        if w.startswith(vowel):
            print(w)

##