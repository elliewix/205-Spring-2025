## we already know a bunch of functions

print("hello I am a function!!")

# 1. name is print
# 2. inputs: whatever stuff you want to appear, goes in ()
# 3. Action? knows how to make the console go
# 4. output: your text in the console

print(max(1, 100, -3))

# name: max
# inputs: some numbers in the ()
# action: figure out how to find the highest num
# output: that highest num

## define a function

# let's write a function that splits a bill in half
# name: split_the_bill_in_half
# inputs: the bill amount or total, call it bill
# action: do the math to calculate the half
# output: that half amount

# experiment with the action item first

bill = 45
print(bill / 2)

# so now we actually do the function
print("let's run a function")
def split_the_bill_in_half(bill):
    # action zone
    half = bill / 2
    # nothing after return
    return half

# you have to call the function
print(split_the_bill_in_half(45))
print(split_the_bill_in_half(135))