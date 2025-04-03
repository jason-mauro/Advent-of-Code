with open("input.txt") as fin:
    grid = fin.read().strip().split("\n")


n = len(grid)


dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < n)

def score(i, j):
    if grid[i][j] != "0":
        return 0
    
    ans = 0
    
    stack = [(i, j)]
    visited = set()
    while len(stack) > 0:
        curi, curj = stack.pop()
        # For part 2 remove the visited part and you get the answer as you can visit the same place twice in a grid for different paths
        if (curi,curj) in visited:
            continue
        visited.add((curi,curj))
        cur = int(grid[curi][curj])

        if cur == 9:
            ans += 1
            continue

        for di, dj in dd:
            ii, jj = curi + di, curj + dj
            
            if not in_grid(ii, jj):
                continue

            nbr = int(grid[ii][jj])
            if nbr != cur + 1:
                continue
            stack.append((ii, jj))

    return ans


ans = 0
for i in range(n):
    for j in range(n):
        ans += score(i, j)

print(ans)