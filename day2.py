import sys
# A rock X 1
# B paper Y 2
# C scissors Z 3
# lose=0 X
# draw=3 Y
# win=6  Z

path = sys.argv[1]

def score(me):
    switch={
        'X':1,
        'Y':2,
        'Z':3,
        }
    return switch.get(me)

def result(game):
    switch={
        'A X':3,
        'A Y':6,
        'A Z':0,
        'B X':0,
        'B Y':3,
        'B Z':6,
        'C X':6,
        'C Y':0,
        'C Z':3,
        }
    return switch.get(game)

def score_2(elf,me):
    game_score=0
    switch={
        'X':0,
        'Y':3,
        'Z':6,
        }
    loss={
        'A':3,
        'B':1,
        'C':2,
        }
    win={
        'A':2,
        'B':3,
        'C':1,
        }
    draw={
        'A':1,
        'B':2,
        'C':3,
        }
    game_score += switch.get(me)
    if me == 'Y': # i draw, get score for same as elf
        game_score += draw.get(elf)
    elif me == 'X': # a loss
        game_score += loss.get(elf)
    else: # a win
        game_score += win.get(elf)
    return(game_score)




with open(path, 'r') as file:
    games = [line.strip() for line in file]

total_score = 0
total_score_2 = 0
game_score = 0

for game in games:
    (elf,me) = game.split()
    game_score += score(me)
    game_score += result(game)
    total_score += game_score

    total_score_2 += score_2(elf,me)

    game_score=0
    
print("Part 1:"+str(total_score))
print("Part 2:"+str(total_score_2))




