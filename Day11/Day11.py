with open("input.txt") as fin:
    input = fin.read().strip()

stones = list(map(int, input.split(" ")))
print(stones)

# This takes forever it is easier to make it using default dict and creating the entries that way
def transform(stones):
    i = 0
    while i < len(stones):
        stone = stones[i]
        l = len(str(stone))
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if stone == 0:
            stones[i] = 1

        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
        # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
        # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        elif len(str(stones[i])) % 2 == 0:
            # Remove the current stone and add left and right stones
            stones.pop(i)  
            stones.insert(i,int(str(stone)[:l // 2]) ) 
            stones.insert(i + 1,int(str(stone)[l // 2:]) ) 

            # Skip the added stone
            i += 1

        #If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        else:
            stones[i] = stones[i] * 2024

        i += 1

for i in range(75):
    transform(stones)
    print(i)
    
print(len(stones))