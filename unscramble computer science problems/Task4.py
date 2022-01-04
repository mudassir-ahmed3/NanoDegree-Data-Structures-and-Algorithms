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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
possible_telemarketers = []
recieved_calls_list =[]
msg_sender_list = []
msg_recieve_list = []

for text in texts:
    msg_sender_list.append(text[0])
    msg_recieve_list.append(text[1])
for call in calls:
    recieved_calls_list.append(call[1])
    if call[0] not in recieved_calls_list and call[0] not in msg_sender_list and call[0] not in msg_recieve_list:
        if not call[0].startswith('140'):# to avoid adding those who are established telemarketers already
            possible_telemarketers.append(call[0])

# print(len(possible_telemarketers))
unique_possible_telemarketers = set(possible_telemarketers)
sorted_possible_telemarketers = list(unique_possible_telemarketers)
sorted_possible_telemarketers.sort()

# print(sorted_possible_telemarketers)
# print(len(sorted_possible_telemarketers))
print("These numbers could be telemarketers: ")
print(*sorted_possible_telemarketers,sep='\n')