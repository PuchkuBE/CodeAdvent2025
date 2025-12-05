from operator import itemgetter
from collections import deque

with open('input/day5.txt', 'r') as f:
    lines = f.read().splitlines()

def part2(ranges):
    ans = 0
    sorted_ranges = deque(sorted(ranges, key=itemgetter(0), reverse=False))
    while len(sorted_ranges) >= 2:
        low1, high1 = sorted_ranges.popleft()
        low2, high2 = sorted_ranges.popleft()
        if high1 >= low2: # Create compacted range and add it again for processing
            sorted_ranges.appendleft((low1, max(high1,high2)))
        else: # First item can't be merged, add range to answer, and add second item for processing again
            ans += high1 - low1 +1
            sorted_ranges.appendleft((low2, high2))
    # One range left in sortedrange
    low, high = sorted_ranges.pop()
    return ans + high - low +1

ranges = []
ingredients = []
for line in lines:
    if not line:
        break
    low, high = map(int, line.split("-"))
    ranges.append((low, high))
ingredients = [int(line) for line in lines[len(ranges)+1:] if line]

ans1 = sum(any(low <= ingredient <= high for low, high in ranges) for ingredient in ingredients)
ans2 = part2(ranges)

print(f'Solution for day5/part1: {ans1}')
print(f'Solution for day5/part2: {ans2}')