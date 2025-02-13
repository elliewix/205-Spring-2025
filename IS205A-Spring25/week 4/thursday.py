score = 43

# check pass/fail

if score >= 60:
    print("pass")
else:
    print("fail")

# let's add more

score = 75

if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"
elif score >= 70:
    letter = "C"
elif score >= 60:
    letter = "D"
else:
    letter = "F"

# print(letter)

def choose_letter(score):
    if score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

print(choose_letter(85))
print(choose_letter(56))
print(choose_letter(93))

## let's use these results in another if statement
# calcaulate if this is pass or fail
exam_score = 92
letter_result = choose_letter(exam_score)
print(letter_result)
letter_result = "E"

# go to town with alllll the things
if letter_result == "A":
    print("pass")
elif letter_result == "B":
    print("pass")
elif letter_result == "C":
    print("pass")
elif letter_result == "D":
    print("pass")
elif letter_result == "F":
    print("fail")
else:
    print('this should never print')

# compact it....oddly

if letter_result == "A" or letter_result == "B" or letter_result == "C" or letter_result == "D":
    print("pass")
else:
    print("fail")

if letter_result == "F":
    print("Fail")
else:
    print("pass")

if letter_result in ["A", "B", "C", "D"]:
    print("pass")
else:
    print("fail")

if letter_result in ["A", "B", "C", "D"]:
    print("pass")
elif letter_result == "F":
    print("fail")
else:
    print("error")

