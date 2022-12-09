def inBounds(forest, x, y):
    return 0 <= x < len(forest) and 0 <= y < len(forest[0])

def isEdge(forest, x, y):
    return x == 0 or x == len(forest) - 1 or y == 0 or y == len(forest[0]) - 1

def isVisible(forest, x, y):
    currHeight = forest[x][y]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx, dy in dirs:
        nx, ny = x, y
        while inBounds(forest, nx+dx, ny+dy) and forest[nx+dx][ny+dy] < currHeight:
            nx+=dx
            ny+=dy
        if isEdge(forest, nx, ny):
            return True
    return False

def getScenicScore(forest, x, y):
    score = 1
    currHeight = forest[x][y]
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx, dy in dirs:
        nx, ny = x, y
        while inBounds(forest, nx+dx, ny+dy) and forest[nx+dx][ny+dy] < currHeight:
            nx+=dx
            ny+=dy
        distance = abs(nx-x) + abs(ny-y) + 1 - int(isEdge(forest, nx, ny))
        score *= distance
    return score

with open("input.txt") as file:
    forest = [line.rstrip() for line in file]

    numVisible = 0
    maxScore = 0
    for x in range(len(forest)):
        for y in range(len(forest[0])):
            if isVisible(forest, x, y):
                numVisible += 1
            maxScore = max(maxScore, getScenicScore(forest, x, y))

    print(f"1) {numVisible}")
    print(f"2) {maxScore}")

