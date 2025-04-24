import csv
import random

words = ['cat','grass', 'tree', 'banana', 'sidewalk']

outer_list = []
# this is a silly example to just create some 2D data
for i in range(20): # just making 20 rows of data
    row = random.choices(words, k = 3)
    # print(row)
    outer_list.append(row)
print(outer_list)
headers = ["choice 1", "choice 2", "choice 3"]
# to write out a csv, we need:
# headers as a 1D list
# data as a 2D list
# ONLY when you have these can you write out the data

# boilerplate for writing out a CSV

outfile = open('ourdata.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile)
csvout.writerow(headers) # singular for headers, the 1D list
csvout.writerows(outer_list) # plural for data, the 2D list

# another example where we need to do more work to create the 2D list of rows

participants = ['a', 'b','c','d','e','f']

outer_list2 = []

for p in participants:
    # I'm doing silly tasks, but to make fields
    city = random.choice(words).title() + ", IL"
    option = random.choice(words)
    number = len(random.choice(words))
    # first just print the fields
    # print(p, city, option, number) # once this looks good
    row = [p, city, option, number] # we collect it into row
    outer_list2.append(row) # and collect the row
print(outer_list2)

headers = ["participant id", "city", "choice", "number"]
# my headers and 2d list are ready so now I can write it out
outfile = open('moredata.csv', 'wt', encoding='utf-8')
csvout = csv.writer(outfile)
csvout.writerow(headers)
csvout.writerows(outer_list2)
