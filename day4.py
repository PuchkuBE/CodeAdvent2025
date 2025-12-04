lines = open('input/day4.txt','r').read().splitlines()

def isReachable(row, col, grid):
    rolls_around = 0
    for r in range(row-1,row+2):
        for c in range(col-1, col+2):
            # Outside the grid are no rolls
            if not ((r<0 or r >= len(grid)) or (c<0 or c >= len(grid[r]))):
                rolls_around += 1 if grid[r][c] == '@' else 0
    return rolls_around < 5 # Roll itself was included, so 5 instead of 4

ans1 = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        # If we are on a roll, check if reachable
        if lines[r][c] == '@':
            ans1 += 1 if isReachable(r, c, lines) else 0

ans2 = 0
while True:
    prev_ans2 = ans2
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            # If we are on a roll, check if reachable
            if lines[r][c] == '@':
                if isReachable(r, c, lines):
                    lines[r] = lines[r][:c] + '.' + lines[r][c+1:]
                    ans2 += 1
    if ans2 == prev_ans2:
        break

print(f'Solution for day4/part1: {ans1}')
print(f'Solution for day4/part2: {ans2}')