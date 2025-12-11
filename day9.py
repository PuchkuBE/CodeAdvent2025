from array import array
from collections import namedtuple
from itertools import combinations

with open('input/day9b.txt', 'r') as f:
    lines = f.read().splitlines()

def area(square):
    return (abs(square[1].x - square[0].x) + 1) * (abs(square[1].y - square[0].y) + 1)

tile = namedtuple('tile', ['y','x'])
tiles = [tile(*map(int,line.split(","))) for line in lines]

squares = [tuple(x) for x in combinations(tiles, 2)]

squares.sort(key=area, reverse=True)
print(f'Solution for day9/part1: {area(squares[0])}')

#grid = [[0 for i in range(0,100000)] for j in range(0,100000)]

rows, cols = 100000, 100000  # or your desired size
grid = [array('B', [0]*cols) for _ in range(rows)]

print('Empty grid created')

#Connect the tiles
t = tiles[0]
grid[t.x][t.y]=2
tiles.append(tiles[0])
for tile in tiles[1:]:
    grid[tile.x][tile.y]=2
    if tile.x == t.x: # Same row
        miny = min(tile.y, t.y)
        maxy = max(tile.y, t.y)
        for c in range(miny+1,maxy):
            grid[tile.x][c] = 1
    elif tile.y == t.y: # Same col
        minx = min(tile.x, t.x)
        maxx = max(tile.x, t.x)
        for r in range(minx+1,maxx):
            grid[r][t.y] = 1
    t = tile

print('Tiles connected')

def fill_enclosed2(grid):
    # First search a point inside
    print('searching inside')
    inside = (0,0)
    for ir,row in enumerate(grid):
        if not inside == (0,0):
            break
        for iv, val in enumerate(row):
            if val == 1:
                if grid[ir][iv+1] == 0:
                    inside = (ir, iv+1)
                    break
                else:
                    break # go to next row
    print(inside)
    neighbors = ((0,-1),(-1,0),(0,1),(1,0))
    def fillpoint(x, y):
        if grid[x][y] == 0:
            grid[x][y] = 3
            for dx,dy in neighbors:
                fillpoint(x+dx,y+dy)
    fillpoint(inside[0],inside[1])
    return grid

grid = fill_enclosed2(grid)

def valid(square, grid):
    tile1 = square[0]
    tile2 = square[1]
    minx = min(tile1.x, tile2.x)
    maxx = max(tile1.x, tile2.x)
    miny = min(tile1.y, tile2.y)
    maxy = max(tile1.y, tile2.y)
    hor = ((minx, miny),(minx, maxy)),((maxx, miny),(maxx,maxy))
    ver = ((minx, miny),(maxx, miny)),((minx, maxy),(maxx, maxy))
    for (lx, ly),(rx, ry) in hor:
        if any([grid[lx][y] == 0 for y in range (ly, ry+1)]):
            return False
    for (tx, ty),(bx, by) in ver:
        if any([grid[x][ty]== 0 for x in range (tx, bx+1)]):
            return False
    return True

for square in squares:
    if valid(square, grid):
        print(f'Solution for day8/part2: {area(square)}')
        exit(0)
print('No solution found for day8/part2')

