with open("../input.txt") as f:
    lines = f.read().splitlines()


r = 103
c = 101

grid = [[0 for _ in range(c)] for _ in range(r)]

pos = [] # Array of current robot positions
vel = [] # Array of robots velocity



for line in lines:
    # Parse the 4 numbers in the line (p and v)
    ps = [0] * 2
    vs = [0] * 2
    parts = line.split()
    par = parts[0].split("=")
    n = par[1].split(",")
    ps[0] = int(n[1])
    ps[1] = int(n[0])
    par = parts[1].split("=")
    n = par[1].split(",")
    vs[0] = int(n[1])
    vs[1] = int(n[0])
    pos.append(ps)
    vel.append(vs)
    grid[ps[0]][ps[1]] += 1

    
for i in range(101):
    for j in range(len(pos)):
        print(pos[j])
        print(vel[j])
        grid[pos[j][0]][pos[j][1]] -= 1
        # (r,c)
        if (pos[j][0] + vel[j][0] < 0):
            pos[j][0] = (r) + pos[j][0] + vel[j][0] # Wrap to the right
        elif (pos[j][0] + vel[j][0] >= r):
            pos[j][0] = pos[j][0] + vel[j][0] - r
        else:
            pos[j][0] += vel[j][0]
            
        if (pos[j][1] + vel[j][1] < 0):
            pos[j][1] = (c) + pos[j][1] + vel[j][1] # Wrap to the right
        elif (pos[j][1] + vel[j][1] >= c):
            pos[j][1] = pos[j][1] + vel[j][1] - c
        else:
            pos[j][1] += vel[j][1]

        print("pos" + str(pos[j]))
        grid[pos[j][0]][pos[j][1]] += 1

q1 = 0
q2 = 0
q3 = 0
q4 = 0


# Rows
# 0 - 102
# 0- 50
# 52 - 102


# 0 - 49
# 51 - 100


for i in range(51):
    for j in range(50):
        q1 += grid[i][j]
        q2 += grid[i][j + 51]
        q3 += grid[i + 52][j]
        q4 += grid[i + 52][j + 51]

print(q1 + q2 + q3 + q4)
print(q1 * q2 * q3 * q4)


# 1 (0, 50) rows (0,49)
# 2 (0,50) (51, 100)
# 3 (52, 102) (0, 49)
# 4 (52, 102) (51, 100)


