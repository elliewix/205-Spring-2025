## we've seen some functions


print("hi, I'm a function")
# name is print
# inputs are inside the ()
# it knows  how to make things appear
# and output is the stuff on the screen

print(max(1, 3, 9, -10))
# name is max
# inputs are the numbers in the ()
# action is to determine the max number
# output is to return that number

## write a function together

# 1. split_the_bill_in_half
# 2. inputs: the bill amount, call it bill
# 3. divide the bill in half
# 4. output: the calculated half of the bill, a number

### experiment with a proof of concept for the action

bill = 45
half = bill / 2
print("my experiment results")
print(half)

# now the function
## actually make the function

def split_the_bill_in_half(bill):
    half = bill / 2

    # return should always be the last thing
    return half

print(split_the_bill_in_half(45))