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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#fixed line: Example: "(022)40840621".
#Mobile numbers Example: "93412 66159".
#Tele marketers 1402316533"

def typeofTelphonenumber(number):
    if number[0] == '(':
        return 'fixed line'
    else:
        if number[0] == '1':
            return 'telemarketers'
        else:
            return 'mobile numbers'

# x = typeofTelphonenumber("93412 66159")
# print(x)
area_codes = []
for call in calls:
    banglore_calls = call[0].find("(080)")
    if banglore_calls != -1:
        #if it's banglore calls only then I'm interested in recieving_number's area codes and mobile prefixes
        if typeofTelphonenumber(call[1]) == 'mobile numbers':
            # area_code = call[1].split()
            area_codes.append(call[1][:4])
        else:
            if typeofTelphonenumber((call[1])) == 'fixed line':
                index = call[1].index(')')
                # print(call[1][1:index])
                area_codes.append(call[1][1:index])
            else:
                area_codes.append('140')

# print(area_codes)
# print(len(area_codes))

unique_area_codes = set(area_codes)
# print(unique_area_codes)
# print(len(unique_area_codes))

sorted_area_codes = list(unique_area_codes)
sorted_area_codes.sort()
print("The numbers called by people in Bangalore have codes:")
print(*sorted_area_codes, sep='\n')

totalbanglorecalls_count = 0
bangloretobanglorecalls_count =0
for call in calls:
    if call[0].startswith("(080)"):
        totalbanglorecalls_count+=1
    if call[0].startswith("(080)") and call[1].startswith("(080)"):
        bangloretobanglorecalls_count+=1

percentage = (bangloretobanglorecalls_count/totalbanglorecalls_count)*100

output = "{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
print(output.format(percentage))