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


def pattern_positions(sense, pattern):
    positions = []
    for i in range(0, len(sense) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and pattern[j] == sense[i + j]:
            j += 1
        if j == len(pattern):
            positions.append(i)
    return positions


def make_m_rns(sense):
    m_rns = []
    pattern_start = [ 'A', 'C']
    pattern_end = [ 'C', 'A']

    # T -> U
    for (b, p) in sense:
        d_base = b
        if d_base == 'T':
            d_base = 'U'
        m_rns += d_base

    print(m_rns)

    # remove signedparts
    start_list = pattern_positions(m_rns, pattern_start)
    ends_list = pattern_positions(m_rns, pattern_end)

    print("start list: {} end list: {}".format(start_list, ends_list))
    m_rns_index_offset = 0
    for start in start_list:
        i = 0
        if len(ends_list) == 0:
            return m_rns

        while i < len(ends_list) and ends_list[i] <= start + len(pattern_start) - 1:
            i += 1

        if i < len(ends_list):
            end = ends_list[i] + len(pattern_end) - 1
            # remove the part from start -> i from m_rns
            if len(ends_list) > 0 and i < len(ends_list):
                ends_list = ends_list[i:]
                start_with_offset = start - m_rns_index_offset
                end_with_offset = end - m_rns_index_offset + 1
                if start_with_offset < end_with_offset:
                    print("removed {} {}".format(start_with_offset, end_with_offset))
                    m_rns = m_rns[:start_with_offset] + m_rns[end_with_offset:]
                    m_rns_index_offset += end - start + 1
                    print m_rns
                    continue

    # add prefix, suffix

    return m_rns