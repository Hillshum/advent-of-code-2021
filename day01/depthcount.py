

with open('input.txt', 'r') as f:
    lines = f.readlines()

# lines = lines[:50]

# lines = ['199',
# '200',
# '208',
# '210',
# '200',
# '207',
# '240',
# '269',
# '260',
# '263']

def part1():
    count = 0
    for i, line in enumerate(lines):
        if i is 0:
            continue
        prev = int(lines[i-1].strip())
        curr = int(line.strip())
        print(curr, prev)
        if curr > prev:
            count += 1

    print(count)