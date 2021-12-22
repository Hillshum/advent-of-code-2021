input_string = """2199943210
3987894921
9856789892
8767896789
9899965678
"""

with open('input.txt', 'r') as f:
    input_string = f.read()


points = [[int(i) for i in line] for line in input_string.strip().split('\n')]

print(points)


def get_neighbor_indexes(r, c, width, height):
    neighbors = []

    new_c = c -1
    # left
    if (new_c >= 0):
        neighbors.append((r, new_c))

    new_r = r-1
    # up-left
    # if (new_r >= 0 and new_c >= 0):
    #     neighbors.append((new_r, new_c))

    # up
    if (new_r >= 0):
        neighbors.append((new_r, c))
    
    # up-right
    new_c = c + 1
    # if (new_c < width and new_r >= 0):
    #     neighbors.append((new_r, new_c))

    # right
    if (new_c < width) :
        neighbors.append((r, new_c))

    new_r = r + 1
    # right-down

    # if (new_c < width and new_r < height):
    #     neighbors.append((new_r, new_c))

    # down
    if (new_r < height):
        neighbors.append((new_r, c))

    # down-left
    new_c = c -1
    # if (new_r < height and new_c >= 0):
    #     neighbors.append((new_r, new_c))

    return neighbors


lows = []
for i, row in enumerate(points):
    for j, col in enumerate(row):
        neighbors = []
        try:
            index = i-1
            if (index >= 0):
                neighbors.append(points[index][j])
        except IndexError:
            pass

        try:
            neighbors.append(points[i + 1][j])
        except IndexError:
            pass

        try:
            neighbors.append(points[i][j + 1])
        except IndexError:
            pass

        try:
            index = j-1
            if (index >= 0):
                neighbors.append(points[i][index])
        except IndexError:
            pass

        # print(i,j, neighbors)
        if col < min(neighbors):
            # print(col, i, j)
            # print(col)
            lows.append((i, j))

risk = sum([points[i][j] for i,j in lows]) + len(lows)
print(risk)

cache = set()

def build_basin(row, col):
    if (row, col) in cache:
        return 0
    neighbors = get_neighbor_indexes(row, col, len(points[0]), len(points))

    current_height = points[row][col]
    cache.add((row, col))
    print(current_height)
    basin_neighbors = [(r,c) for r,c in neighbors if current_height < points[r][c] < 9 ]
    print(basin_neighbors)

    return 1 + sum([build_basin(r,c) for r, c in basin_neighbors])


# print(build_basin(0,1))

    
# print(build_basin(0,9))

basin_sizes = [build_basin(r, c) for r, c in lows]

basin_sizes.sort(reverse=True)

result = 1
for size in basin_sizes[:3]:
    result *= size

print(result)