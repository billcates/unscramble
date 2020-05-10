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
phone=set()
for each in texts:
    phone.add(each[0])
    phone.add(each[1])
for each in calls:
    phone.add(each[0])
    phone.add(each[1])
print("There are {a} different telephone numbers in the records.".format(a=len(phone)))
