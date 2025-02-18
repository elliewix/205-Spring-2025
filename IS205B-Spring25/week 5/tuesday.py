total = 5 + 7 + 3
print(total)

print(total + 5)
print(total)
total = total + 5
total = total + 3
print(total)

## starting up with loops
count = 0

count = count + 1
count = count + 1
count = count + 1
count = count + 1
count = count + 1
count = count + 1

print(count)

## let's use a structure to repeat the line for us

count = 0

for number in range(6):
    count = count + 1

print("count, but from a for loop", count)

count = 0
for number in "sticks":
    count = count + 1

print(count)
# each has 6 things to loop over
# making the body of the loop execute 6 times

# a shorthand version
count += 1

## looking at other stuff

for letter in "here's a string":
    print(letter)

# more realistic example

my_string = "hello I'm a string"

for letter in my_string:
    print(letter)

weird_string = "aoeuidhtns- 24 134oeu 52houk 1 u"
for letter in weird_string:
    print(letter)

# string methods

weird_upper = weird_string.upper()
print(weird_upper)
print(weird_string.isalpha())

print(weird_string.split())

### a filtering loop

for letter in weird_string:
    # print(letter, letter.isalpha())
    if letter.isalpha() == True:
        print(letter)

# let's count the results

count_everything = 0
count_trues = 0
count = 0
for letter in weird_string:
    # print(letter, letter.isalpha())
    count_everything = count_everything + 1
    if letter.isalpha() == True:
        count_trues = count_trues + 1

print(count)
print(count_everything, count_trues)

another_weird_one = "aUUUIEU iuReuUnhiE245NUI U U 5"
sentence = "Hello, Cats drool Too Much"

print("cats" in sentence) # false, C and c are diff
print("cats" in sentence.lower()) # true, because everything is lower

print("cat" in sentence.lower()) # True, because substr

lower_sentence = sentence.lower()
split_sentence = lower_sentence.split()
print(split_sentence)

print("cats" in split_sentence) # True
print("cat" in split_sentence) # False
# in with a list looks for exact matches