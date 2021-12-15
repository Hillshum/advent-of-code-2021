


lines = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]


print(len(lines[0]))
gamma = []
epsilon = []
for i in range(len(lines[0])):
    counts = {'0': 0, '1': 0}
    for line in lines:
        counts[line[i]] += 1
    if counts['0'] > counts['1']:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

gamma_val = int(''.join(gamma), 2)
epsilon_val = int(''.join(epsilon), 2)

print(gamma_val, epsilon_val)
print(gamma_val * epsilon_val)