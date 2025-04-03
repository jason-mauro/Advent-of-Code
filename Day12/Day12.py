from collections import deque

with open("../input.txt") as fin:
    finput = fin.read().splitlines()

grid = [list(string) for string in finput]

print(grid)
dd = [(0,1), (0,-1),(1,0),(-1,0)]

visited = set()

n = len(grid)
m = len(grid[0])

total = 0

def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < m)

# DFS to get area * perimeter of a letter
def getValue(i, j):
    PERIM = dict()
    if (i,j) in visited:
        return 0
    p = 0 # Perimeter
    a = 0 # Area
    stack = [(i,j)]
    current = grid[i][j] 

    while stack:
        curi, curj = stack.pop()
        if (curi, curj) in visited:
            continue
        visited.add((curi,curj))

        a += 1
        for di,dj in dd:
            ii,jj = curi + di, curj + dj
            if in_grid(ii,jj) and grid[ii][jj] == current:
                stack.append((ii,jj))
            else:
                if (di,dj) not in PERIM:
                    PERIM[(di,dj)] = set()
                PERIM[(di,dj)].add((curi,curj))
                p += 1

    sides = 0
    # Since you keep track of all the sides that go out at a certain direction, all the blocks that have side on left in 1 set
    # You just Keep track of all the points you see in that direction and go 1 in all directions. If on the left say, you check up and down and visit it as that is 1 side
    for k, vs in PERIM.items(): # returns tuple of direction, set
        SEEN_PERIM = set()
        for (pr,pc) in vs:
            if (pr,pc) not in SEEN_PERIM:
                sides += 1
                Q = deque([(pr,pc)])
                while Q:
                    r2,c2 = Q.popleft()
                    if (r2,c2) in SEEN_PERIM:
                        continue
                    SEEN_PERIM.add((r2,c2))
                    for dx,dy in dd:
                        rr, cc = r2 + dx, c2 + dy
                        if (rr, cc) in vs:
                            Q.append((rr,cc))

    return a * sides # Return p * a for Day 1 answer
    
  
   

for i in range(n):
    for j in range(m):
        total += getValue(i, j)



print(total)

