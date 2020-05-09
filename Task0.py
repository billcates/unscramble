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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
t=(texts[0])
l=(len(calls))
g=(calls[l-1])
print("First record of texts, {a} texts {b} at time {c}".format(a=t[0],b=t[1],c=t[2]))
print("Last record of calls, {a} calls {b} at time {c}, lasting {d} seconds".format(a=g[0],b=g[1],c=g[2],d=g[3]))
