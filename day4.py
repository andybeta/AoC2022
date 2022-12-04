# split line at ,
# enumerate range into a sets ass1 and ass2. Is there a quicker way?
# intersection of ass1 and ass2 = ass1 or ass2, then count++

path = sys.argv[1]

with open(path, 'r') as file:
    lines = [line.strip() for line in file]

total = 0
total2 = 0

def make_ass_set(rangeX): # given a range A-D return a set of assignments {A,B,C,D}
    start,end=rangeX.split("-")
    ass = set()
    for i in range(int(start),int(end)+1):
        ass.add(i)
    return ass


for line in lines:
    range1,range2=line.split(",") # split the line on ,
    ass1=make_ass_set(range1) # get assignment set 1
    ass2=make_ass_set(range2) # get assignment set 2
    intersect = set(ass1) & set(ass2) # find the intersect
    if intersect == ass1 or intersect == ass2: # if it is the same as either assignment
        total+=1                                # that set is contained in the other
    if intersect != set():          # part 2, if the intersect is not empty then it overlaps
        total2+=1

print("Part 1:"+str(total))
print("Part 2:"+str(total2))
