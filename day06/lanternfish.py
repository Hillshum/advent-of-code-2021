from collections import defaultdict

fish = '3,4,3,1,2'


with open('input.txt', 'r') as f:
    fish = f.read()
fish.strip()


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


# for i in range(80):
#     fish = process_day(fish)

# print(len(fish))


fish_dict = defaultdict(lambda : 0)

for f in fish:
    fish_dict[f] += 1

# print(fishes)


max_age = 9

def process_day_batch(fishes):
    new_fishes = defaultdict(lambda: 0)
    for i in range(max_age):
        fishes_this_age = fishes[i]
        if i == 0:
            new_fishes[8] += fishes_this_age
            new_fishes[6] += fishes_this_age
            # print(new_fishes)

        else:
            new_fishes[i-1] += fishes_this_age
            # print(new_fishes)
    
    # print(new_fishes)
    return new_fishes



print(fish_dict)
for i in range(256):
    fish_dict = process_day_batch(fish_dict)

print(fish_dict)
answer = sum(fish_dict.values())

print(answer)
correct_answer = 26984457539
print(answer == correct_answer)