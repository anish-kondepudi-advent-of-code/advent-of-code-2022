with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    totalCaloriesForElves = []

    totalCaloriesForElf = 0
    for line in lines:
        if line == '':
            totalCaloriesForElves.append(totalCaloriesForElf)
            totalCaloriesForElf = 0
        else:
            totalCaloriesForElf += int(line)

    totalCaloriesForElves.sort(reverse=True)

    print(f"1) {totalCaloriesForElves[0]}")
    print(f"2) {sum(totalCaloriesForElves[:3])}")