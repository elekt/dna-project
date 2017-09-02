import random

DEFAULT_AMINO_ACIDS = {
    ('U', 'U', 'U'): "Phe_(F)",
    ('U', 'U', 'C'): "Phe_(F)",
    ('U', 'U', 'A'): "Leu_(L)",
    ('U', 'U', 'G'): "Leu_(L)",
    ('U', 'C', 'U'): "Ser_(S)",
    ('U', 'C', 'C'): "Ser_(S)",
    ('U', 'C', 'A'): "Ser_(S)",
    ('U', 'C', 'G'): "Ser_(S)",
    ('U', 'A', 'U'): "Tyr_(Y)",
    ('U', 'A', 'C'): "Try_(Y)",
    ('U', 'A', 'A'): "STOP",
    ('U', 'A', 'G'): "STOP",
    ('U', 'G', 'U'): "Cys_(C)",
    ('U', 'G', 'C'): "Cys_(C)",
    ('U', 'G', 'A'): "STOP",
    ('U', 'G', 'G'): "Trp_(W)",
    ('C', 'U', 'U'): "Leu_(L)",
    ('C', 'U', 'C'): "Leu_(L)",
    ('C', 'U', 'A'): "Leu_(L)",
    ('C', 'U', 'G'): "Leu_(L)",
    ('C', 'C', 'U'): "Pro_(P)",
    ('C', 'C', 'C'): "Pro_(P)",
    ('C', 'C', 'A'): "Pro_(P)",
    ('C', 'C', 'G'): "Pro_(P)",
    ('C', 'A', 'U'): "His_(H)",
    ('C', 'A', 'C'): "His_(H)",
    ('C', 'A', 'A'): "Gln_(Q)",
    ('C', 'A', 'G'): "Gln_(Q)",
    ('C', 'G', 'U'): "Arg_(R)",
    ('C', 'G', 'C'): "Arg_(R)",
    ('C', 'G', 'A'): "Arg_(R)",
    ('C', 'G', 'G'): "Arg_(R)",
    ('A', 'U', 'U'): "Ile_(I)",
    ('A', 'U', 'C'): "Ile_(I)",
    ('A', 'U', 'A'): "Ile_(I)",
    ('A', 'U', 'G'): "Met_(M)/START",
    ('A', 'C', 'U'): "Thr_(T)",
    ('A', 'C', 'C'): "Thr_(T)",
    ('A', 'C', 'A'): "Thr_(T)",
    ('A', 'C', 'G'): "Thr_(T)",
    ('A', 'A', 'U'): "Asn_(N)",
    ('A', 'A', 'C'): "Asn_(N)",
    ('A', 'A', 'A'): "Lys_(K)",
    ('A', 'A', 'G'): "Lys_(K)",
    ('A', 'G', 'U'): "Ser_(S)",
    ('A', 'G', 'C'): "Ser_(S)",
    ('A', 'G', 'A'): "Arg_(R)",
    ('A', 'G', 'G'): "Arg_(R)",
    ('G', 'U', 'U'): "Val_(V)",
    ('G', 'U', 'C'): "Val_(V)",
    ('G', 'U', 'A'): "Val_(V)",
    ('G', 'U', 'G'): "Val_(V)",
    ('G', 'C', 'U'): "Ala_(A)",
    ('G', 'C', 'C'): "Ala_(A)",
    ('G', 'C', 'A'): "Ala_(A)",
    ('G', 'C', 'G'): "Ala_(A)",
    ('G', 'A', 'U'): "Asp_(D)",
    ('G', 'A', 'C'): "Asp_(D)",
    ('G', 'A', 'A'): "Glu_(E)",
    ('G', 'A', 'G'): "Glu_(E)",
    ('G', 'G', 'U'): "Gly_(G)",
    ('G', 'G', 'C'): "Gly_(G)",
    ('G', 'G', 'A'): "Gly_(G)",
    ('G', 'G', 'G'): "Gly_(G)"
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
