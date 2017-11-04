from util import get_random_base, get_tobacco_mosaic_virus, get_base_pair, make_m_rns, get_aminoacids

sense = []
tmv = get_tobacco_mosaic_virus()
for base in tmv:
    pair = get_base_pair(base)
    sense.append((base, pair))


m_rns = make_m_rns(sense)
# print("mRNS: {}".format(m_rns))

amino_acids = get_aminoacids(m_rns)
print(" ".join(amino_acids))
