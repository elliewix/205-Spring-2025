animals = ['cat', 'dog', 'snake', 'horse', 'fish']

for a in animals:
    print(a)

for num in range(4):
    print(num)

## let's loop over both together in a nested loop

for a in animals:
    for num in range(4):
        print(a, num)

# and the inverse

for num in range(4):
    for a in animals:
        print(a, num)

# making multiple files in one loop

for a in animals:
    # print(a + ".txt")
    fname = a + '.txt' # print this to check first
    outfile = open(fname, 'wt', encoding='utf-8') # opening file
    outfile.write(a) # doing stuff to it
    outfile.close() # closing it

# adding stuff to a file in a loop
# this creates our content
for num in range(4):
    print(str(num) + " animal(s)")

# add it all to a single file
outfile = open('results.txt', 'wt', encoding='utf-8')
for num in range(4):
    # print(str(num) + " animal(s)")
    outfile.write(str(num) + " animal(s)\n")
    # don't close outfile here
outfile.close() # close it here at the same indent level

# so how do we combine these
# use this one for hw4 and lab 4
for a in animals:
    # print(a + '.txt')
    outfile = open(a + '.txt', 'wt', encoding='utf-8')
    for num in range(4):
        outfile.write(str(num) + " " + a + "(s)\n")
        # don't close the file here
    outfile.close() # close the file here
# don't close the file here

# here's how things can go wrong
# this pattern can be used but not for this problem
for num in range(4):
    for a in animals:
        # we only get the last item
        outfile = open(a + "-withproblems.txt", 'wt',encoding='utf-8')
        outfile.write(str(num) + " " + a + '\n')
        outfile.close()