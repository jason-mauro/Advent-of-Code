with open("../input.txt") as fin:
    inp = fin.read().split("\n\n")

grid = inp[0].splitlines()

for i in range(len(grid)):
    grid[i] = list(grid[i])

r = len(grid)
c = len(grid[0])



moves = "".join(inp[1].splitlines())


m = dict()
m['^'] = [-1,0]
m['>'] = [0, 1]
m['<'] = [0 , -1]
m['v'] = [1, 0]


curr = [0,0]

for x in range(r):
    for y in range(c):
        if grid[x][y] == '@':
            curr = [x,y]




for move in moves:
    dir = m[move]
    pos = curr
    steps = 0
    x,y = dir
    length = 0
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
    for y in range(c):
        if grid[x][y] == 'O':
            tot += 100 * x + y
print(tot)
    
   








