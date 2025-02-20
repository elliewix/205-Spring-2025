sentence = "235U@$1uoeu ,.u `245"
# replace, takes old, new

# just calling it doesn't save the change
print(sentence.replace("2", "x"))
print(sentence.replace("3", "x"))

# do reassignment to save the change
sentence = sentence.replace("2", "x")
sentence = sentence.replace("3", "x")
print("my new text is", sentence)

# so for all the numbers, what if we wanted to
# get rid of them? so erase/move
sentence = "235U@$1uoeu ,.u `245"
# so the "" is *airquotes* nothing
print(sentence.replace("2", ""))
print(sentence.replace("3", ""))

# so let's iteratively save these results

sentence = sentence.replace("1", "")
sentence = sentence.replace("2", "")
sentence = sentence.replace("3", "")
sentence = sentence.replace("4", "")
sentence = sentence.replace("5", "")
print("and my new text is:", sentence)

weird_text = "235ei45ui85.pui023hu7345b"
numbers = "0123456789"
for num in numbers:
    # print(num)
    # does the action but doesn't save it
    # print(weird_text.replace(num, ""))
    # do both, action and save the result
    weird_text = weird_text.replace(num, "")

print("my cleaned string is", weird_text)

# what the punctuation?
import string
print(string.punctuation)
for punc in string.punctuation:
    print(punc)
#
# # a brief aside about immutable vs mutable
# original = "hello"
# upper_original = original.upper() # returing method
# # so I need a variable assignment to save it
# print(original, upper_original)
#
# # lists are mutable, so can change them
# my_list = ['a', 'b']
# # so I want to change this list right above
# # if I have a mutating method, no assignment
# my_list.append("c") # no assignment!
# print(my_list)
# my_list.reverse()
# print(my_list)
