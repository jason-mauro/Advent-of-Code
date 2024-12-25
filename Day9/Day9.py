from itertools import repeat
with open("input.txt", 'r') as fin:
    input = fin.readline()
    
ans = 0
blocks = []
id = 0

for i in range(0, len(input)):
    if i % 2 == 0:
        for i in range(int(input[i])):
            blocks.append(str(id))
        id += 1
    else:
        for i in range(int(input[i])):
            blocks.append('.')

for i in range(len(blocks) - 1, 0, -1):
    if blocks[i] != '.':
        for j in range(0, len(blocks)):
            if j >= i:
                break
            if blocks[j] == '.':
                blocks[i], blocks[j] = blocks[j], blocks[i]
                break

for i in range(0, len(blocks)):
    if blocks[i] != '.':
        ans += i * int(blocks[i])
print(ans)
