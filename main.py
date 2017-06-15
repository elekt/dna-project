from util import get_random_base, get_base_pair, search_pattern

sense = []
for i in range(0, 50):
    base = get_random_base()
    pair = get_base_pair(base)
    sense.append((base, pair))

pattern = [ sense[len(sense)-3], sense[len(sense)-2], sense[len(sense)-1]]
print(sense)
print(pattern)
search_pattern(sense, pattern)
