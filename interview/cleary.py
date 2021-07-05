from collections import Counter, defaultdict


def get_most_frequent_n_paths(fp, n=4, y=1):
    counts = Counter()

    def get_four_paths(path):
        for i in range(len(path)):
            if i + n > len(path):
                break
            current_path = ",".join(p for p in path[i:i+n])
            counts[current_path] += 1

    with open(fp, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip()
            line = line.split(",")
            get_four_paths(line)

    file.close()
    frequency_to_path = defaultdict(list)
    for k, v in counts.items():
        frequency_to_path[v].append(k)
    max_frequency = max(counts.values())

    four_paths = []

    while y > 0 and max_frequency > 0:
        if max_frequency in frequency_to_path:
            for path in frequency_to_path[max_frequency]:
                four_paths.append(path.split(","))
            y -= 1
        max_frequency -= 1
    return four_paths


# print(get_most_frequent_n_paths("paths2.txt"))
# print(get_most_frequent_n_paths("paths2.txt", 5))
#print(get_most_frequent_n_paths("paths2.txt", 7))

print(get_most_frequent_n_paths("paths2.txt", 4, 5))
