from util import get_random_base, get_base_pair, make_m_rns

sense = []
for i in range(0, 35):
    base = get_random_base()
    pair = get_base_pair(base)
    sense.append((base, pair))

m_rns = make_m_rns(sense)
