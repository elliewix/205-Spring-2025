# the classic infile pattern

infile = open('stuff.txt', 'rt', encoding='utf-8')
text = infile.read()
infile.close()

print(text)

for character in text:
    print(character)

# the string split method

# print(text.split(" ")) # never want to see this
print(text.split()) # gets words out
print(text.split("\n"))

words = text.split()
for w in words:
    # print(w, len(w))
    # what are the words that start with a?
    # print(w, w.startswith("a"))
    if w.startswith("a"): # filter pattern
        print(w)

## indexing and slicing

print("the 0th item:", words[0]) # index out the 0th item
print("the 0th item from text:", text[0])