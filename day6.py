import sys
import re

# assign input to string
# for position i, take substring len x (x=4)
# function check string:
#   for pos j, take char at j, if regex count (whole string) > 1 return false else true
# if true, print pos i and exit, else i+=1

path = sys.argv[1]
seqLen=int(sys.argv[2])

with open(path, 'r') as file:
    line = file.readline()

def isSignal(packet):
    count=0
    for j in range(len(packet)):
        char=packet[j:j+1]
        count+=len(re.findall(char, packet))
    if count == len(packet):
        return True
    else:
        return False

for i in range(len(line)):
    packet=line[i:i+seqLen]
    if isSignal(packet):
        print("Answer:",i+seqLen)
        break
