import sys

path = sys.argv[1]

with open(path, 'r') as file:
    cals = [line.strip() for line in file]

totals=[]
this_elf=0

for cal in cals: # for each row in the input
    if not cal:  # if it's blank then
        totals.append(this_elf) # add the total for this elf to the totals list
        this_elf=0 # init this_elf ready for the next one
        continue   # get the next row
    this_elf+=int(cal) # otherwise add the value to this elf's total
totals.append(this_elf) # catch the last elf!
totals.sort(reverse=True) # sort largest first

print("Part 1:"+str(totals[0])) # print the single largest

top3=totals[0]+totals[1]+totals[2] # sum the top 3
print("Part 2:"+str(top3)) # print the total of the top 3
