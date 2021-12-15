
lines = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


def parse_line(command):
    direction, distance = command.split(' ')
    distance = int(distance)
    print(direction, distance)

    if direction == 'forward':
        return (0, distance)

    if direction == 'down':
        return (distance, 0)

    if direction == 'up':
        return (-distance, 0)



def get_position():
    depth = 0
    horizontal = 0

    for line in lines:
        delta_depth, delta_hor = parse_line(line)
        depth += delta_depth
        horizontal += delta_hor

    print (depth, horizontal)
    print(depth * horizontal)

if __name__ == '__main__':
    get_position()