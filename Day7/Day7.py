
from itertools import product

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
ans = 0

for line in lines:
    parts = line.split(":")
    value = int(parts[0])
    nums = list(map(int,parts[1].split(" ")[1:]))


    # function to evaluate the given nums and combination of operators
    def test(combo):
        ans = nums[0]
        for i in range(1, len(nums)):
            if combo[i-1] == '+':
                ans += nums[i]
            elif combo[i-1] == '|': 
                ans = int(f"{ans}{nums[i]}")
            else:
                ans *= nums[i]

        return ans
    
    # product produces all combinations of the operators for length len(nums) - 1 and then loop through and do the operatiosn on them.
    for combo in product("*+|", repeat=len(nums)-1):
        if test(combo) == value:
            ans += value
            break


print(ans)





