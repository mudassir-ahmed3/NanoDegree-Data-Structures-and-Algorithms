"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# mydict ={
#     "hello": 23,
#     "world":22
# }
# print(mydict)
#
# mydict.update({"hello":mydict["hello"]+7})
# print(mydict)
dict = {}
#key would be phone no and time spent on phone should bge it's value
#if he made the call or recieved the call that duration will add up to calculate time spent on phone
#idea is to iterate through calls if key already there in dict update it's value by adding call[3] to old value if it's not already there simply assign call[3] as it's value
for call in calls:
    if call[0] not in dict:
        dict[call[0]] = int(call[3])
    else:
       dict[call[0]]= dict[call[0]]+int(call[3])
    if call[1] not in dict:
        dict[call[1]] = int(call[3])
    else:
        dict[call[1]]= dict[call[1]]+int(call[3])

# print(dict)
maxtime =0
maxcalltimenumber = ''
for number in dict.keys():
    if dict[number]>maxtime:
        maxtime = dict[number]
        maxcalltimenumber = number

print(maxcalltimenumber+" spent the longest time, "+str(maxtime)+" seconds, on the phone during September 2016")





