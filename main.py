from util import get_random_base, get_base_pair, search_pattern

sense = []
for i in range(0, 500):
    base = get_random_base()
    pair = get_base_pair(base)
    sense.append((base, pair))

pattern = [('G', 'C'), ('G', 'C'), ('A', 'T')]
print(sense)
print(pattern)
search_pattern(sense, pattern)
