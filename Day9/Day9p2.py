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

# iterate through the list in reverse and count the legnth of the given ID, then compare that ID to free space lengths and swap the file blocks and free spaces
i = len(blocks) - 1
while i >= 0:
    if blocks[i] != '.':
        length = 0
        temp = i
        while blocks[i] == blocks[temp]:
            length += 1
            temp = temp -1
        j = 0
        # count the spaces
        while j < len(blocks):            
            if j < i and blocks[j] == '.':
                space = 0
                temp = j
                while blocks[temp] == '.':
                    space += 1
                    temp = temp + 1
                if space >= length:
                    # Swap the blocks
                    for k in range(length):
                        blocks[i - k], blocks[j + k] = blocks[j + k], blocks[i - k]
                    j = len(blocks)
                j += space
            else:
                j += 1
        i -= length 
    else:
      i -= 1 

# Sum the solution
for i in range(0, len(blocks)):
    if blocks[i] != '.':
        ans += i * int(blocks[i])

print(ans)

