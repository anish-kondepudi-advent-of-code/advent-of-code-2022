def getPriority(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1


with open("input.txt") as file:

    totalPriority = 0
    lines = [line.rstrip() for line in file]
    for line in lines:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]

        first_half_set = set([c for c in first_half])
        second_half_set = set([c for c in second_half])

        common_char = tuple(first_half_set.intersection(second_half_set))[0]
        totalPriority += getPriority(common_char)

    print(f"1) {totalPriority}")

    totalPriority = 0
    for i in range(len(lines)//3):
        chunk = lines[3*i: 3*i+3]

        s1 = set([c for c in chunk[0]])
        s2 = set([c for c in chunk[1]])
        s3 = set([c for c in chunk[2]])

        common_char = tuple(s1.intersection(s2).intersection(s3))[0]
        totalPriority += getPriority(common_char)

    print(f"2) {totalPriority}")