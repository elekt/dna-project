import random

DEFAULT_AMINO_ACIDS = {
    ('A', 'A', 'B'): "amino_acid_0",
    ('A', 'G', 'U'): "amino_acid_1",
    ('A', 'U', 'U'): "amino_acid_2",
    ('A', 'U', 'G'): "metionin"
}

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


def pattern_positions(sense, pattern_start, pattern_end):
    start_positions = []
    end_positions = []
    is_searching_start = True

    i = 0
    # if in the end start is coming and longer than
    while i < len(sense) - len(pattern_end) + 1:
        j = 0
        pattern = pattern_end
        if is_searching_start:
            pattern = pattern_start

        while j < len(pattern) and pattern[j] == sense[i + j]:
            j += 1

        if j == len(pattern):
            if is_searching_start:
                start_positions.append(i)
                is_searching_start = False
            else:
                end_positions.append(i)
                is_searching_start = True
            i += j
        else:
            i += 1

    if not is_searching_start:
        _ = start_positions.pop()

    if len(start_positions) != len(end_positions):
        print("ERROR: different start position count than end")

    return start_positions, end_positions


def make_m_rns(sense):
    m_rns = []

    # T -> U
    for (b, p) in sense:
        d_base = b
        if d_base == 'T':
            d_base = 'U'
        m_rns += d_base

    m_rns = remove_dns_parts(m_rns)
    print("mRNS with removed parts: {}".format(m_rns))

    return m_rns


def remove_dns_parts(m_rns):
    sliced_m_rns = []
    pattern_start = ['A', 'A']
    pattern_end = ['G', 'C']

    # remove signedparts
    start_list, end_list = pattern_positions(m_rns, pattern_start, pattern_end)

    start = len(m_rns)
    end = len(m_rns)
    if len(start_list) > 0:
        start = start_list.pop(0)
        end = end_list.pop(0)
    for i in range(0, len(m_rns)):
        if i < start:
            sliced_m_rns.append(m_rns[i])
        elif i == end + len(pattern_end) - 1:
            if len(start_list) > 0:
                start = start_list.pop(0)
                end = end_list.pop(0)
            else:
                start = len(m_rns)
                end = len(m_rns)
        i += 1
    return sliced_m_rns


def get_aminoacids(m_rns):
    amino_acids = []

    for i in range(0, len(m_rns) - 3, 3):
        codon = (m_rns[i], m_rns[i+1], m_rns[i+2])
        if codon in DEFAULT_AMINO_ACIDS:
            amino_acids.append(DEFAULT_AMINO_ACIDS[codon])

    return amino_acids
