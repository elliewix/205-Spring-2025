score = 85

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

print(letter)

# let's write our function to contain this

# 1. name is choose_grade
# 2. input is score
# 3. action: the logic structure
# 4. return letter

def choose_grade(score):
    # do stuff???
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

print(choose_grade(85))
print(choose_grade(35))

### let's write a pass/fail thing in a bunch of ways

letter_grade = choose_grade(85)

# everything option

if letter_grade == "A":
    print("pass")
elif letter_grade == "B":
    print("pass")
elif letter_grade == "C":
    print("pass")
elif letter_grade == "D":
    print("pass")
elif letter_grade == "F":
    print("fail")
else:
    print("this should never print, error")

# alt
print("alt options")
letter_grade = choose_grade(44) # all should fail in this
letter_grade = "E"

if (letter_grade == "A") or (letter_grade == "B") or (letter_grade == "C") or (letter_grade == "D"):
    print("pass")
elif letter_grade == "F":
    print("fail")
else:
    print("error")

if (letter_grade == "A") or (letter_grade == "B") or (letter_grade == "C") or (letter_grade == "D"):
    print("pass")
else:
    print("fail")

if letter_grade == "F":
    print("fail")
else:
    print("pass")

if letter_grade in ["A", "B", "C", "D"]:
    print("pass")
else:
    print("fail")