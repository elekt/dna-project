import random


def get_random_base():
    baseint = random.randint(0, 99)

    if baseint < 40:
        return 'C'
    elif baseint < 50:
        return 'T'
    elif baseint < 80:
        return 'G'
    else:
        return 'A'


def get_base_pair(base):
    if base == 'C':
        return 'G'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    else:
        return 'T'


def search_pattern(sense, pattern):
    for i in range(0, len(sense) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and pattern[j] == sense[i + j] :
            j += 1
        if j == len(pattern):
            print("HEUREKA")


def make_m_rns(sense):
    m_rns = []
    for (base, pair) in sense:
        m_rns.append(base)

    # remove signedparts
    for i in range(len(m_rns)):
        print(m_rns[i])

    # add prefix, suffix

    return m_rns