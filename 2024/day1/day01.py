from pathlib import Path

# Looks next to this file, so it works from any folder.
input_path = Path(__file__).with_name("input.txt")
lines = input_path.read_text().splitlines()

left = []
right = []

for line in lines:
    nums = line.split()
    left.append(int(nums[0]))
    right.append(int(nums[1]))
        
left.sort()
right.sort()

# Day 1 -- part 1
def part1(left, right):
    dif = []

    for left, right in zip(left, right):
        dif.append(abs(left - right))

    print(sum(dif))

# Day 1 -- part 2

def part2(left, right):
    dups = {}
    total = 0

    for i in right:
        dups[i] = dups.get(i, 0) + 1
    for n in left:
        total += (n * dups.get(n, 0))

    print(total)
    
part1(left, right)               
part2(left, right)