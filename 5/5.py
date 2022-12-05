def getSeparationIdx(lines):
    separation_idx = -1
    for i, line in enumerate(lines):
        if line == "":
            separation_idx = i
            break
    return separation_idx

def createStacks(stacks_lines):
    stacks = [[] for _ in range(len(lines[separation_idx - 1]) //4 + 1)]
    for stack_line in reversed(stacks_lines):
        i = 1
        while i < len(stack_line):
            if stack_line[i] != " ":
                stacks[i // 4].append(stack_line[i])
            i += 4
    return stacks

def constructMessage(stacks):
    message = ""
    for stack in stacks:
        if len(stacks) == 0:
            continue
        message += stack[-1]
    return message

def runCrateMover(stacks, instructions, keepOrder):
    for instruction in instructions:
        words = instruction.split()

        amount = int(words[1])
        from_idx = int(words[3]) - 1
        to_idx = int(words[5]) - 1

        chunk = stacks[from_idx][-1 * amount:]
        if not keepOrder:
            chunk.reverse()

        stacks[from_idx] = stacks[from_idx][:-1 * amount]
        stacks[to_idx].extend(chunk)
    return constructMessage(stacks)

with open("input.txt") as file:

    lines = [line.rstrip() for line in file]

    separation_idx = getSeparationIdx(lines)

    stacks_lines = lines[:separation_idx - 1]
    stacks1 = createStacks(stacks_lines)
    stacks2 = createStacks(stacks_lines)

    instructions = lines[separation_idx + 1:]
    message1 = runCrateMover(stacks1, instructions, keepOrder=False)
    message2 = runCrateMover(stacks2, instructions, keepOrder=True)

    print(f"1) {message1}")
    print(f"2) {message2}")