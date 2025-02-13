# revisiting function definitions

# 1. letter_grade
# 2. input should be numerical_score
# 3. action should be choosing the letter grade
#    for the score
# 4. output should be the letter grade

def letter_grade(numerical_score):
    # action TBD
    # but would go here...
    return "A"

print(letter_grade(85))
print(letter_grade(34))
print(letter_grade(93.5))

# importing functions

## default import
import random
print(random.randint(0, 10))

## importing as an alias

import random as rd # this is weird, don't do this
# for random.
# DO use this style if it matches community convention
print(rd.randint(0,10))
# random.randint() will no longer work

# danger zone styles, using "from"
# use with caution
from random import randint
# this will import just that one function
# but into your default namespace
# and none of the other random things are there
print(randint(0, 10))
# but random.anotherfunction() won't work

# the big caution one, is the wildcard
from random import *
# why are you using this, this is a weird choice
# I get all the stuff without dot notation

# conditionals

## how we make computers make choices

## boolean values
print(True)
print(False)

## to make these we use a few things

## boolean expressions
### boolean operators

print(3 > 5, 10 == 10)

### boolean methods

print("hello".isalpha())
print("hello1".isalpha())
print("HELLO".isupper())

### boolean keywords

# the in keyword is going to a best friend
# this is keyword is banned

# the in keyword is great! it checks membership in
# a sequence

print("h" in "hello")
print("hell" in "hello")
print("H" in "hello") # false

## letter grade choice

# score = 95
# if score >= 90:
#     letter = "A"
#
# print(letter)


# what if we want to do something
# if the result is false?
score = 80
if score >= 90:
    letter = "A"
else:
    letter = "not A"
# else: if the stuff above me isn't True
# then I will execute
print(letter)
