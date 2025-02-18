total = 5 + 3 + 7
print(total)
print(total + 5) # this doesn't do anything to total
total = total + 5
print(total)
total = total + 3
print(total)

# loops over numbers

## counter pattern
## count up by one

count = 0 # establish base

count = count + 1
count = count + 1
count = count + 1
count = count + 1
count = count + 1
count = count + 1
# you might see this
count += 1 # this is just a shorthand for the same thing
print(count)

# we can use a for loop to repeat things
# we'll use a range loop to repeat a specific number of times
count = 0
for number in range(7):
    count = count + 1
print(count)

# will do the same thing

count = 0
for wont_use_this in range(7):
    count = count + 1
print(count)
# mess with the syntax a bit more
count = 0
for number in range(10, 15):
    count = count + 1
print(count)

## for loops and strings

# a for loop that counts how many letters
# are in a string

count = 0
for letter in "here's a string":
    count = count + 1
    print(letter, count)

print("final count is", count)

for letter in "hey, here's a string":
    print(letter)

# abstract this more

my_string = "yet another string"

for letter in my_string:
    print(letter)

weird_string = "stuff 4 12345 ous1y52 uio"

for letter in weird_string:
    # print(letter.isalpha())
    if letter.isalpha() == True:
        print(letter)

##
print(weird_string)
split_string = weird_string.split()
print(split_string)

print("cat" in split_string)

print("345" in weird_string) # true because substring
print("345" in split_string) # false because not a perfect match
