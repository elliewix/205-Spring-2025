sentence = "here's some stuff!!!"

for character in sentence:
    print(character)

# the replace method
# give it old, new
# returns a new string where that's been replaced

text = "11toeii34xxx"
print(text.replace("x", "9"))
print(text.replace("i", "1"))
print("line 13's text:", text)
# replacing old with new
text = text.replace("x", "9")
text = text.replace("i", "1")
print("line 17's text, after updating", text)


# what if we wanted to remove all the numbers?
## using replace to remove
## "replace" it with an empty string
print("remove 1", text.replace("1", ""))
print("remove 3", text.replace("3", ""))
print("remove 4", text.replace("4", ""))
print("replace 9", text.replace("9", ""))
print("and now text is...", text)

# okay let's update it though...

text = text.replace("1", "")
text = text.replace("3", "")
text = text.replace("4", "")
text = text.replace("9", "")
print("and now text is", text)

# let's think about how we can do this
# in a loop
# the question is, what do we loop over?
# well, what's changing? the content needing
# to be replaced is changing

numbers = "0123456789"
clean_this = "234p.i65eui72345bu94520!"

for num in numbers:
    # print(num)
    # this removes but doesn't save
    # print(clean_this.replace(num, ""))
    # this saves the intermediate results
    clean_this = clean_this.replace(num, "")

print("all those numbers are now gone", clean_this)

import string

print(string.punctuation)

for punc in string.punctuation:
    print(punc)

