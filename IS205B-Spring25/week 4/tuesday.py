# practice for defining functions
# making a "placeholder" function

# 1. letter_grade
# 2. input will be numerical_score
# 3. action will be to determine the letter
#    grade, but we're making it a placeholder
#    for now.
# 4. output should be the letter grade

def letter_grade(numerical_score):
    # the action zone here
    # leaving empty for now
    # placeholder, so everyone gets an A
    # for now
    letter = "A"
    return letter

print(letter_grade(95))
print(letter_grade(67))
print(letter_grade(70))

# before we go further.... let's talk about importing modules
# this should be your default choice
import random

print(random.randint(0, 10))

# import as an alias
import random as rd
# can't use random anymore, must us rd instead
print(rd.randint(0,10))

# the weirder zone
from random import randint
# used mostly in specific technical situations
# not for general use
# this changes our syntax a lot
# no need to specify the module name
print(randint(0,10))

# the danger zone
# really only used for very specific situations
# DO NOT USE outside of those
from random import *
#importing everything into your namespace

### let's go back to conditionals

# boolean operators

print(3 > 5)
print(10 == 10)

score = 70
print(score > 60) # needs to be greathan 60 to pass
score = 46
print(score > 60) # false

# boolean methods

print("hello".isupper())
print("hello".isalpha()) # is this just text?
print("hello1".isalpha())

# boolean keywords

# in will be your best friend

# in with a string

print("h" in "hello")
print("ll" in "hello")
print("hell" in "hello")
print("H" in "hello") # False, H isn't h

## let's see these questions in our logic frame
print("let's calculate some scores")
score = 70
# if score > 60:
#     print("pass")

# if you change this to be false
# you'll see nothing
# score = 34
# if score > 60:
#     print("pass")

# we can use else: to take an action if the question isn't True

score = 30
if score > 60:
    print("pass")
else:  # think more "otherwise"
    print("fail")
    # else will execute if everything above it fails

# instead of printing the result, we can save it as a variable

score = 99
if score >= 60:
    result = "pass"
else:
    result = "fail"

print("Your results are: " + result)

# okay let's put this in a function

# 1. name will be determine_result
# 2. input will be score
# 3. action is the logic structure to choose pass/fail
# 4. return the pass/fail result

def determine_result(score):
    # action zone
    if score >= 60:
        result = "pass"
    else:
        result = "fail"
    # output
    return result

print("Your result is: " + determine_result(65))
print("Your result is: " + determine_result(99))
print("Your result is: " + determine_result(32))


