from collections import defaultdict

with open("input.txt","r") as f:
    lines = f.read().split("\n")

V = len(lines)
H = len(lines[0]) 

nodes1 = set()
nodes2 = set()
antennas = defaultdict(list)

# Find antennas and add them to the dict
for y in range(0,V):
    for x in range(0,H):
        if lines[y][x] != '.':
            antennas[lines[y][x]].append((x,y))

for val in antennas.values():
    val.sort()
    for i in range(0,len(val) - 1):
        for j in range(i + 1, len(val)):
            # Calulate the slope and find the points and if valid add to nodes
            # val[i] is left point
            # val[j] is right point
            dy = val[j][1] - val[i][1]
            dx = val[j][0] - val[i][0]
            # part 1
            if val[i][0] - dx >= 0 and 0 <= (val[i][1] + -1 * dy) < V :
                nodes1.add((val[i][0] - dx, val[i][1] + -1 * dy))
            if val[j][0] + dx < H and 0 <= (val[j][1] + dy) < V :
                nodes1.add((val[j][0] + dx, val[j][1] + dy))
            
            left = val[i]
            right = val[j]
            # part 2

            # add the locatios of the antennas to the nodes as that is valid
            nodes2.add(left)
            nodes2.add(right)
            # Loop until each point on the lines will go off the grid
            while left[0] - dx >= 0 and 0 <= (left[1] + -1 * dy) < V :
                left = (left[0] - dx, left[1] + -1 * dy)
                nodes2.add((left[0], left[1]))
            while right[0] + dx < H and 0 <= (right[1] + dy) < V :
                right = (right[0] + dx, right[1] + dy)
                nodes2.add((right[0], right[1]))
                
                    
print(len(nodes1))
print(len(nodes2))
    




