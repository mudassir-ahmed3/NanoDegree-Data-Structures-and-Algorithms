"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#first idea was to transform list to sets so that dupilcates can be removed but set()could not handle list of lists
joined_list = texts + calls
# print(len(joined_list))
unique_list = []
for number in joined_list:
    if number[0] not in unique_list:
        unique_list.append(number[0])
    if number[1] not in unique_list:
        unique_list.append(number[1])
print("There are "+str(len(unique_list))+" different telephone numbers in the records")