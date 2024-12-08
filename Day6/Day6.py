import copy

with open("input.txt", "r") as f:
    lines1 = list(f.read().split("\n"))

lines = [list(line) for line in lines1]
p1 = 0


for i in range(0, len(lines)):
    if '^' in lines[i]:
        sx,sy = lines[i].index("^"), i
        break;


def isLoop(x,y,line2, start):
    positions = {(x,y)}
    direction = 0
    pos = set()
    while x >= 0 and x < len(line2[0]) and y >= 0 and y < len(line2):
            #UP
            if direction == 0:
                y -= 1
                if y < 0:
                    break;
                if line2[y][x] == '#':
                    direction += 1
                    y += 1
                    if (x,y,direction) in pos:
                        return True
                    pos.add((x,y,direction))

            #right
            if direction == 1:
                x += 1
                if x == len(line2[0]):
                    break;
                if line2[y][x] == '#':
                    direction += 1
                    x -= 1
                    if (x,y,direction) in pos:
                        return True
                      
                    pos.add((x,y,direction))
        
    
            #down
            if direction == 2:
                y += 1
                if y == len(line2):
                    break;
                if line2[y][x] == '#':
                    direction += 1
                    y -= 1
                    if (x,y,direction) in pos:
                   
                        return True;
                    pos.add((x,y,direction))
        
            #left
            if direction == 3:
                x -= 1
                if x == -1:
                    break;
                if line2[y][x] == '#':
                    direction = 0
                    x += 1
                    if (x,y,direction) in pos:
                        return True;
                    pos.add((x,y,direction))
            positions.add((x,y))
    if start:
        return len(positions)
    return False



# Walk through and add obstacles for in each posiiton and check for loop

boxes = set()


turn = False
p2 = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        x,y = sx,sy
        if (x,y) == (j,i):
            continue
        lines_with_obstacle = copy.deepcopy(lines)
        lines_with_obstacle[i][j] = '#'
        if isLoop(sx,sy,lines_with_obstacle, False):
            p2 += 1

p1 = isLoop(sx,sy,lines,True)


print(p1)
print(p2)






