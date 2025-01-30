print(1)
print("cat")
print("1 cat")

# case matters....sometimes
print(True)
print(False)
# print(true) # would be an error

# variables

number = 12
total = 0

# coordinates, like (x, y)
x = 0
y = 0

# calculate mean
total = 120
n = 5 # sample

print(total / n)

# variable names
# can't start with numbers
# be careful with punctuation
# don't use reserved words
# but be mindful about using function names
# try not to

print(sum([1, 2, 4]))

# allowed, but bad
sum = 10
count = 3
print(sum/count)
# looks good but then...
# you get an error that it isn't callable
# because you've tried to put () after not a function
# print(sum([1,3,4]))

# this may also be an issue with min, max, etc.

# variables can also hold strings

name = "Elizabeth"
print("Hello " + name)

