# split the bill in half

def split_the_bill_in_half(bill):
    half = bill / 2
    return half

result = split_the_bill_in_half(42)
print(result)

## do more calculations or something

print(split_the_bill_in_half(111))
print(split_the_bill_in_half(30))
print(split_the_bill_in_half(56.4))

# let's generalize this more

def split_bill(bill, portions):
    p = bill / portions
    return p

print(split_bill(111, 2))
print(split_bill(32, 4))
print(split_bill(700, 3))
# print(p) # will be an error, can't see
# within the function

# returning

print(split_bill(45, 2) + split_bill(700,3))

## how to make a nice output

print("Your total share is " + str(split_bill(39, 3)))
