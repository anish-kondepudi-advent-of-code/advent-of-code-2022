with open("input.txt") as file:
    lines = [line.rstrip().split(",") for line in file]

    fully_contain_pairs = 0
    overlaps = 0
    for range1, range2 in lines:
        range1_start, range1_end = map(int, range1.split('-'))
        range2_start, range2_end = map(int, range2.split('-'))

        range_is_subset = [
            range1_start <= range2_start <= range2_end <= range1_end,
            range2_start <= range1_start <= range1_end <= range2_end
        ]

        if any(range_is_subset):
            fully_contain_pairs += 1

        range_overlaps = [
            range1_start <= range2_start <= range1_end,
            range1_start <= range2_end <= range1_end,
            range2_start <= range1_start <= range2_end,
            range2_start <= range1_end <= range2_end,
        ]

        if any(range_overlaps):
            overlaps += 1

    print(f"1) {fully_contain_pairs}")
    print(f"2) {overlaps}")

