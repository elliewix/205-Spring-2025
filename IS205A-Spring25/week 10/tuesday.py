animals = ['cat', 'dog', 'snake', 'horse', 'fish']

for a in animals:
    # print(a + ".txt")
    fname = a + ".txt"
    print(fname)
    outfile = open(fname, 'wt', encoding='utf-8')
    outfile.write("some stuff")
    outfile.close()

# out old outfile pattern

outfile = open('mystuff.txt', 'wt', encoding='utf-8')
outfile.write("more stuff")
outfile.close()

# extend the old one with a loop for content
outfile = open('mystuff.txt', 'wt', encoding='utf-8')
for a in animals:
    outfile.write(a + '\n')
outfile.close()

# what happens if the outfile is in my loop here?

for a in animals:
    outfile = open('mystuff_withproblems.txt', 'wt', encoding='utf-8')
    outfile.write(a + '\n')
    outfile.close()

# let's go back to nested loops for a second

for a in animals:
    print(a)

for num in range(4):
    print(num)

# let's nest them
for num in range(4): # outer
    for a in animals: # inner
        # print(num, a)
        print(a, num)

# and the other way around
for a in animals:
    for num in range(4):
        print(a, num)

##
# oops, only seeing the last items for this
for num in range(4): # outer
    for a in animals: # inner
        outfile = open(a + '_withproblems.txt', 'wt', encoding='utf-8')
        outfile.write(str(num) + " " + a)
        outfile.close()

# and the other way around

for a in animals:
    fname = a + '.txt'
    outfile = open(fname, 'wt', encoding='utf-8')
    for num in range(4):
        outfile.write(str(num) + ' ' + a + "(stuff)\n")
        # don't close outfile here
    outfile.close() # close it here
# don't close outfile here


