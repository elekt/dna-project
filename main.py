from util import get_random_base, get_base_pair, make_m_rns, get_aminoacids

sense = []
start_codon = [('A', get_base_pair('A')), ('U', get_base_pair('U')), ('G', get_base_pair('G'))]
stop_codon = [('A', get_base_pair('A')), ('U', get_base_pair('U')), ('U', get_base_pair('U'))]
sense.extend(start_codon)
for i in range(0, 21):
    base = get_random_base()
    pair = get_base_pair(base)
    sense.append((base, pair))
sense.extend(stop_codon)
print("Original sense: {}".format(sense))
m_rns = make_m_rns(sense)
print(get_aminoacids(m_rns))
