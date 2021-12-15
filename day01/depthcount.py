

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

def part2():
    sums = []
    for i, line in enumerate(lines):
        if i is 0:
            continue
        if i is 1:
            continue
        prev = int(lines[i-1].strip())
        prev2 = int(lines[i-2].strip())
        curr = int(line.strip())
        print(curr, prev, prev2)
        sums.append(curr + prev + prev2) 


    print(sums)

    count = 0
    for i, line in enumerate(sums):
        if i is 0:
            continue
        prev = int(sums[i-1])
        curr = int(line)
        print(curr, prev)
        if curr > prev:
            count += 1

    print(count)



if __name__ == '__main__':
    part2()