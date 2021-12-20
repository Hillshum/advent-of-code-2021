from collections import defaultdict


input_string = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

with open('input.txt', 'r') as f:
    input_string = f.read()

X = 0
Y = 1
START = 0
END = 1

def parse_coords(s):
    return [*map(int, s.split(','))]

def parse_line(s):
    coords = s.split('->')
    # print(coords)

    return [*map(parse_coords, coords )]

print(input_string)
coordinates = map(parse_line, input_string.strip().split('\n'))
# print([*coordinates])

vents = defaultdict(lambda: 0)

def is_straight(coords):
    if coords[START][X] == coords[END][X]:
        return True

    if coords[START][Y] == coords[END][Y]:
        return True

    return False

straight_lines = filter(is_straight, coordinates)
# print(len([*straight_lines]))

def get_rangestep(s, e):
    if e < s:
        return -1
    return 1

for line in straight_lines:
    # print(line)
    x_direction = get_rangestep(line[START][X], line[END][X])
    for i in range(line[START][X], line[END][X] + x_direction, x_direction):
        y_direction = get_rangestep(line[START][Y], line[END][Y])
        # print(y_direction)
        for j in range(line[START][Y], line[END][Y] + y_direction, y_direction):
            vents[f"{i}x{j}"] += 1
    # print(vents)

# print(vents)

dangerous_vents = filter(lambda x: x>=2, vents.values())

print(len([*dangerous_vents]))