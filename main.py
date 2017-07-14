from util import get_random_base, get_base_pair, search_pattern

sense = []
for i in range(0, 10000):
    base = get_random_base()
    pair = get_base_pair(base)
    sense.append((base, pair))

pattern = [('G', 'C'), ('A', 'T')]
print(sense)
print(pattern)

if search_pattern(sense, pattern):
    m_rns = []
    for (b, p) in sense:
        d_base = b
        if d_base == 'T':
            d_base = 'U'
        m_rns += d_base
    print(m_rns)
