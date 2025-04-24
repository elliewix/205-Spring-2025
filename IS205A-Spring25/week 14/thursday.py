import csv
import random

# first we need to make some data
# headers: a 1D list
# data: a 2D list

# let's make some random data first

words = ['sidewalk', 'apple', 'tree', 'pear', 'grass', "bush"]

outer_list = []

# do a for loop where we create the rows and collect data

for i in range(20): # we want 20 rows of data
    # we need to create and collect our rows
    # print(random.choices(words, k = 3))
    row = random.choices(words, k = 3)
    outer_list.append(row)
print(outer_list)

headers = ["choice 1", "choice 2", "choice 3"]

# only once we have these two things can we write csv

outfile = open('mydata.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile) # makes our csv writer obj

csvout.writerow(headers) # singular for headers
csvout.writerows(outer_list) # plural for 2d data

# make some data in a diff way
# practice creating these 2D lists

outer_list2 = []

people = ['a','b', 'c', 'd','e', 'f']

for p in people:
    # p name, city and state, some number
    citystate = random.choice(words).title() + ", IL"
    number = len(random.choice(words)) # len of random word
    # print(p, citystate, number) # once this looks good
    row = [p, citystate, number]
    outer_list2.append(row)

# now we need to make some headers

headers = ['participant name', 'city', 'count']

outfile = open('moredata.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile)
csvout.writerow(headers)
csvout.writerows(outer_list2)