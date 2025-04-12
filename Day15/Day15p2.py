with open("../input.txt") as fin:
    inp = fin.read().split("\n\n")

ogrid = inp[0].splitlines()

for i in range(len(ogrid)):
    ogrid[i] = list(ogrid[i])

r = len(ogrid)
c = len(ogrid[0])

grid = [[] for _ in range(r)]

moves = "".join(inp[1].splitlines())


m = dict()
m['^'] = [-1,0]
m['>'] = [0, 1]
m['<'] = [0 , -1]
m['v'] = [1, 0]


curr = [0,0]

for x in range(r):
    for y in range(c):
        if ogrid[x][y] == '#':
            grid[x].append('#')
            grid[x].append('#')
        elif ogrid[x][y] == 'O':
            grid[x].append('[')
            grid[x].append(']')
        elif ogrid[x][y] == '.':
            grid[x].append('.')
            grid[x].append('.')
        else:
            grid[x].append('@')
            grid[x].append('.')   

for x in range(r):
    for y in range(c * 2):
        if grid[x][y] == '@':
            curr = [x,y]






for move in moves:

    boxes = set() # List of tuples of positions of boxes to shift 1 position

    dir = m[move]
    pos = curr
    x,y = dir


    # Keep track of all the x values with boxes, check each one in the direction to see if it runs into a '#' or if it is a [].

    # if there is not any [] or # then we stop

    if grid[pos[0] + x][pos[1] + y] == '[':
        boxes.append((pos[0] + x,pos[1] + y ))
        boxes.append((pos[0] + x,pos[1] + y + 1))
    elif grid[pos[0] + x][pos[1] + y] == ']':
        boxes.append((pos[0] + x,pos[1] + y ))
        boxes.append((pos[0] + x,pos[1] + y - 1))
    else: 
        steps = 0
        length = 0
        # Try to just move the '@' if there is space
        while grid[pos[0]][pos[1]] != '.':
            steps += 1
            pos = [pos[0] + x, pos[1] + y]
            if grid[pos[0]][pos[1]] == '#':
                steps = 0
                break
        # Shift the boxes over
        for s in range(steps, 0, -1):
            grid[curr[0] + x * s][curr[1] + y * s] = grid[curr[0] + x * (s-1)][curr[1] + y * (s-1)]

        # if it moved update the position and replace the old pos with a '.'
        if steps > 0:
            grid[curr[0]][curr[1]] = '.'
            curr[0] += x
            curr[1] += y





    # Count number of steps until an empty space
    # if you run into a '#' before the robot does not move therefor steps = 0
    # else increment the number of steps each time until you run into an empty space
    while grid[pos[0]][pos[1]] != '.':
        steps += 1
        pos = [pos[0] + x, pos[1] + y]
        if grid[pos[0]][pos[1]] == '#':
            steps = 0
            break

    print("\n".join(("".join(g) for g in grid)))
        


    # Shift the boxes over
    for s in range(steps, 0, -1):
        grid[curr[0] + x * s][curr[1] + y * s] = grid[curr[0] + x * (s-1)][curr[1] + y * (s-1)]

    # if it moved update the position and replace the old pos with a '.'
    if steps > 0:
        grid[curr[0]][curr[1]] = '.'
        curr[0] += x
        curr[1] += y
    
tot = 0

for x in range(r):
    for y in range(c * 2):
        if grid[x][y] == 'O':
            tot += 100 * x + y
print(tot)
    
   








