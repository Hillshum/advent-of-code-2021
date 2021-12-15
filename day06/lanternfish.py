
fish = '3,4,3,1,2'


# with open('input.txt', 'r') as f:
#     fish = f.read()
# fish.strip()


fish = fish.split(',')
fish = [int(f) for f in fish]
print(fish)

def process_day(fishes):
    new_fishes = []

    for f in fishes:
        if f == 0:
            new_fishes.append(6)
            new_fishes.append(8)

        else:
            new_fishes.append(f-1)
    
    return new_fishes


for i in range(80):
    fish = process_day(fish)

print(len(fish))