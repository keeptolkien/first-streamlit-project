def task_variant_a():
    def distance(point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


    k = 2
    clusters = [[] for _ in range(k)]

    lst = []
    for _ in range(2):
        lst.append([])

    best_centers = [None for _ in range(k)]

    with open('27_A.txt') as file:
        lst = []
        for line in file.readlines():
            x, y, name = line.split()
            lst.append((float(x), float(y), name))

    print(lst)


    for point in lst:
        x, y, _ = point
        if y > 15:
            clusters[0].append(point)
        else:
            clusters[1].append(point)

    for i in range(k):
        print(i, len(clusters[i]))

    white_blues_0 = []
    from fnmatch import fnmatch
    for point in clusters[0]:
        if fnmatch(point[2], 'B?IV'):
            white_blues_0.append(point)

    print(white_blues_0)


    for i in range(k):
        min_dist = 10 ** 10
        for p1 in clusters[i]:
            dist = 0
            for p2 in clusters[i]:
                dist += distance(p1, p2)

            if dist < min_dist:
                min_dist = dist
                best_centers[i] = p1

    print(best_centers)

    a2 = int(abs(best_centers[0][1] - best_centers[1][1]) * 10_000)
    print(a2)

# task_variant_a()

def task_variant_b():
    def distance_b(point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

    with open('27_B.csv') as file:
        lst = []
        for line in file.readlines():
            x, y, name = line.split()
            lst.append((float(x), float(y), name))

        print(lst[:5])

    k = 3
    clusters = [[] for _ in range(k)]

    for point in lst:
        x, y, _ = point
        if y > 25:
            clusters[0].append(point)
        elif x < 25:
            clusters[1].append(point)
        else:
            clusters[2].append(point)

    centers = [None for _ in range(k)]

    for i in range(k):
        min_dist = 10 ** 10
        for p1 in clusters[i]:
            dist = 0
            for p2 in clusters[i]:
                dist += distance_b(p1, p2)


            if dist < min_dist:
                min_dist = dist
                centers[i] = p1
    print(centers)

    yellow_super_giants = [[] for _ in range(k)]

    from fnmatch import fnmatch

    for i in range(k):
        # print(1, i)
        for point in clusters[i]:
            if fnmatch(point[2], 'G?I'):
                yellow_super_giants[i].append(point)

    for i in range(k):
        print(i, len(yellow_super_giants[i]))

    max_dist = []
    for i in range(k):
        for p1 in yellow_super_giants[i]:
            for p2 in yellow_super_giants[i]:
                dist = abs(p1[0] - p2[0])
                max_dist.append(dist)

    print(max(max_dist))

    b2 = int(max(max_dist) * 10_000)
    print(f'B2 answer: {b2}')

    for i in range(k):
        print(i, len(clusters[i]))

    red_dwarves = []

    for point in clusters[2]:
        if fnmatch(point[2], 'M?V'):
            red_dwarves.append(point)

    print(len(red_dwarves))

    red_dwarves_answer = []

    for point in red_dwarves:
        if abs(point[0] - centers[2][0]) > 0.35:
            red_dwarves_answer.append(point)

    print(f'Red_dwarves_answer: {len(red_dwarves_answer)}')

task_variant_b()

