import sys
import re
import collections

# first format input
# create deque for each stack? appendleft each item as it's read? (list of deque?)
# for move X popright stack a and append stack b
# for solution query last in each stack

# how to format stacks?
# length=(cols * 4)-1
# contents are at pos 2,6,10,...,(colN*4)-2

# how to format moves?
# split line on ' '; x,moveNum,x,fromStack,x,toStack = line.split

# moveNum times: popright fromStack, append toStack

path = sys.argv[1]

with open(path, 'r') as file:
    lines = [line.strip("\n") for line in file]

# How many stacks?

numStacks=0
# find number of Stacks
for line in lines:
    if re.search("^ 1",line): # find the line with the stack numbers
        stacks = re.split(" ",line.strip()) # split it on space
        numStacks = int(stacks.pop()) # find the last (highest) position
        break

# initialise the stacks
stacks=[] # stacks for part1
stacks2=[] # stacks for part2
for i in range(0,numStacks): # for each stack
    stacks.append(collections.deque()) # add an empty deque
    stacks2.append(collections.deque())

for line in lines: # for each line in the file
    if re.search("^ 1",line): # break point = end of the crate diagram
        break
    for i in range(1,(numStacks*4),4): # i is the position of the contents of the crates between [ ]
        space=(i-1)//4 # i don't even know 
        if line[i] != " ": # if there is a crate (not empty)
            stacks[space].appendleft(line[i]) # load it into the left (bottom) of the deque for that column i
            stacks2[space].appendleft(line[i])

for line in lines:
    crate2=collections.deque() # dummy variable for part 2, lifting in chunks
    if re.search("^move",line): # find each line that starts 'move'
        x,moveNum,x,fromStack,x,toStack = line.split(" ") # assign the number to move, from and to
        for i in range(0,int(moveNum)): 
            crate=stacks[int(fromStack)-1].pop() # for part1, pop each content from 'from' stack
            stacks[int(toStack)-1].append(crate) # and append it to the 'to' stack
            crate2.appendleft(stacks2[int(fromStack)-1].pop()) # for part2, create a substack of size moveNum
        stacks2[int(toStack)-1]+=crate2 # and add it to the 'to' stack

topcrates=""
topcrates2=""
# find the top of each stack and output
for stack in stacks:
    topcrates+=stack.pop()

for stack in stacks2:
    topcrates2+=stack.pop()
print("Part 1:",topcrates)
print("Part 2:", topcrates2)
