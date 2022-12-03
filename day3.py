import sys
import string
# create map a-z:1-26
# and A-Z:27-52
# split line in half
# for each letter in 1, is it in 2?
# if yes, look up score and add to total; break

path = sys.argv[1]

with open(path, 'r') as file:
    lines = [line.strip() for line in file]

# ord(a) = 97
# ord(A) = 65

total = 0


for line in lines:
    # assume always even?
    n=len(line)
    comp1 = line[0:n//2]
    comp2 = line[n//2:]

    for item in comp1:
        if item in comp2:
            if item in string.ascii_uppercase:
                total+=ord(item)-38
            else:
                total+=ord(item)-96
            break

print("Part 1:"+str(total))

# part2
# get lines in groups of 3
# for each item in comp1, is it in 2 and 3?
# if yes, lookup score and add to total; break

total = 0

def getSublists(lst):
    subListLength = len(lst) // (int(len(lst)/3))
    for i in range(0, len(lst), subListLength):
        yield lst[i:i+subListLength]

for group in getSublists(lines):
    bag1,bag2,bag3=group
    for item in bag1:
        if item in bag2 and item in bag3:
            if item in string.ascii_uppercase:
                total+=ord(item)-38
            else:
                total+=ord(item)-96
            break

print("Part 2:"+str(total))
