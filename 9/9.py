def getNewTailPosition(tx, ty, hx, hy):
    # On Top case
    if tx == hx and ty == hy:
        return hx, hy

    # Diagonal case (do nothing)
    dirs = ((1,1),(1,-1),(-1,-1),(-1,1))
    for dx, dy in dirs:
        if tx + dx == hx and ty + dy == hy:
            return tx, ty

    # Double jump
    if abs(hy - ty) == 2 and abs(hx - tx) == 2:
        if hy > ty and hx > tx:
            return hx - 1, hy - 1
        if hy > ty and hx < tx:
            return hx + 1, hy - 1
        if hy < ty and hx > tx:
            return hx - 1, hy + 1
        if hy < ty and hx < tx:
            return hx + 1, hy + 1

    # Horizontal case
    if tx == hx or abs(hy - ty) == 2:
        if hy > ty:
            return hx, hy - 1
        else:
            return hx, hy + 1

    # Vertical case
    if ty == hy or abs(hx - tx) == 2:
        if hx > tx:
            return hx - 1, hy
        else:
            return hx + 1, hy

with open("input.txt") as file:
    lines = [line.rstrip().split() for line in file]

    hx, hy, tx, ty = 0, 0, 0, 0
    dirMap = {
        "R": (1,0),
        "L": (-1,0),
        "U": (0,1),
        "D": (0,-1)
    }

    tailPositionsSet1 = set()
    tailPositionsSet2 = set()

    tailPositions = [[0,0] for _ in range(9)]
    hx, hy = 0, 0

    for dir, amt in lines:
        dx, dy = dirMap[dir]
        for _ in range(int(amt)):

            # Update Head
            hx += dx
            hy += dy

            # Update chain of tails
            tailPositions[0][0], tailPositions[0][1] = getNewTailPosition(tailPositions[0][0], tailPositions[0][1], hx, hy)
            for i in range(1, 9):
                tailPositions[i][0], tailPositions[i][1] = getNewTailPosition(tailPositions[i][0], tailPositions[i][1], tailPositions[i-1][0], tailPositions[i-1][1])

            # Mark first and last tail positions
            tailPositionsSet1.add((tailPositions[0][0], tailPositions[0][1]))
            tailPositionsSet2.add((tailPositions[-1][0], tailPositions[-1][1]))

    print(f"1) {len(tailPositionsSet1)}")
    print(f"2) {len(tailPositionsSet2)}")

