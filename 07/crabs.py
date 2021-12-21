crab_string = '16,1,2,0,4,2,7,1,2,14'

with open('input.txt', 'r') as f:
    crab_string = f.read()


crabs = [*map(int, crab_string.split(','))]
# print([*crabs])


farthest_crab = max(crabs)

def triangle(i):
    return int(i * (i +1)/ 2)

def get_distance(target):
    distances = map(lambda crab: abs(target-crab), crabs)
    return sum(distances)
    
def get_distance_triangle(target):
    distances = map(lambda crab: triangle(abs(target-crab)), crabs)
    return sum(distances)

distances = map(get_distance, range(farthest_crab + 1))

shortest = min(distances)

print(shortest)

trangle_distances = map(get_distance_triangle, range(farthest_crab + 1))

print(min(trangle_distances))