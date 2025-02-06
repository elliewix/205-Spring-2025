# split the bill in half

def split_the_bill_in_half(bill):
    half = bill /2
    return half

result = split_the_bill_in_half(32)
print(result)

# what if you have multiple bills to split?
# reuse the function!
print(split_the_bill_in_half(43))
print(split_the_bill_in_half(94))
print(split_the_bill_in_half(23))

# split the bill in general?
# we can add another parameter as input

def split_the_bill(bill, portions):
    splitted = bill / portions
    return splitted

print(split_the_bill(43, 4))
print(split_the_bill(23, 2))
print(split_the_bill(111, 3))

# return vs print

total = split_the_bill(43, 4) + split_the_bill(111, 3)
print("your total is", total)
print("your total is " + str(total) + " for the bills")