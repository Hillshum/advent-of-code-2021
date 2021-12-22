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

risk = 0

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

        print(i,j, neighbors)
        if col < min(neighbors):
            # print(col, i, j)
            # print(col)
            risk += 1 + col


print(risk)