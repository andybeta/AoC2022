import sys

path = sys.argv[1]

with open(path, 'r') as file:
    cals = [line.strip() for line in file]

totals=[]
this_elf=0

for cal in cals: # for each row in the input
    if cal:  # if it's not blank then
        this_elf+=int(cal) # add the value to this elf's total
    else:
        totals.append(this_elf) # add the total for this elf to the totals list
        this_elf=0 # init this_elf ready for the next one
        continue   # get the next row
totals.sort(reverse=True) # sort largest first

print("Part 1:"+str(totals[0])) # print the single largest
print("Part 2:"+str(sum(totals[:3])))
