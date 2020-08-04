def solve(dna_string):
    max_length = 1
    cur_length = 1
    for i in range(1, len(dna_string)):
        if dna_string[i] != dna_string[i-1]:
            cur_length = 1
        else:
            cur_length += 1
        max_length = max(max_length, cur_length)
    print(max_length)


if __name__ == '__main__':
    s = input()
    solve(s)
