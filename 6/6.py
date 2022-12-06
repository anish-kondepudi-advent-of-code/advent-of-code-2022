def find_idx_with_n_contiguous_unique_elements(buffer_stream, n):
    for i in range(n, len(buffer_stream) + 1):
        if len(set(buffer_stream[i-n:i])) == n:
            return i
    return -1

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    buffer_stream = lines[0]

    start_idx = find_idx_with_n_contiguous_unique_elements(buffer_stream, 4)
    message_idx = find_idx_with_n_contiguous_unique_elements(buffer_stream, 14)

    print(f"1) {start_idx}")
    print(f"2) {message_idx}")