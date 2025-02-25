# the core infile pattern



infile = open('stuff.txt', 'rt', encoding = 'utf-8')
text = infile.read()
infile.close()

print(text)

for character in text:
    print(character)

# get just the words

words = text.split()
print(words)
# never want to see
dontdothis = text.split(" ")
# print(dontdothis)

lines = text.split("\n")
print(lines)

### loop over the words

words = text.split()
# for w in words:
#     print(w, len(w))

# filtering pattern
for w in words:
    # print(w, w.startswith("a"))
    if w.startswith("a"):
        print(w)

## indexing and slicing
print("indexing below")
print(words[5])
print(words[-1])
print(words[0])