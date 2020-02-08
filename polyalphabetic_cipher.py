from collections import Counter

LETTER_FREQUENCY = {'E': 12.0,
                    'T': 9.10,
                    'A': 8.12,
                    'O': 7.68,
                    'I': 7.31,
                    'N': 6.95,
                    'S': 6.28,
                    'R': 6.02,
                    'H': 5.92,
                    'D': 4.32,
                    'L': 3.98,
                    'U': 2.88,
                    'C': 2.71,
                    'M': 2.61,
                    'F': 2.30,
                    'Y': 2.11,
                    'W': 2.09,
                    'G': 2.03,
                    'P': 1.82,
                    'B': 1.49,
                    'V': 1.11,
                    'K': 0.69,
                    'X': 0.17,
                    'Q': 0.11,
                    'J': 0.10,
                    'Z': 0.07}


def decode(cipher_text, key):
    cipher = ''.join(cipher_text.split())
    key_extended = (key * (len(cipher) // len(key) + 1))[:len(cipher)]
    message = ''
    for c1, c2 in zip(cipher, key_extended):
        message += chr((ord(c1) - ord(c2)) % 26 + ord('A'))
    print(message)


def substring(s, n):
    s = ''.join(s.split())
    sub_strings = {}
    for i in range(len(s) - n + 1):
        ss = s[i:i + n]
        if ss in sub_strings:
            sub_strings[ss] += [i]
        else:
            sub_strings[ss] = [i]

    for ss in sub_strings:
        temp = []
        for idx in range(len(sub_strings[ss])):
            if idx == 0:
                continue
            temp.append(sub_strings[ss][idx] - sub_strings[ss][idx - 1])
        sub_strings[ss] = temp

    max_ss = sorted(sub_strings.keys(), key=lambda x: len(sub_strings[x]), reverse=True)
    return max_ss, sub_strings


def freq(s, n):
    s = ''.join(s.split())
    counts = []
    for i in range(n):
        c = Counter(s[i::n])
        # c_sum = sum(c.values())
        # c = [c[k] / c_sum for k in c]
        counts.append(c)
    return counts


def freq_distance(counts):
    n_char = sum(counts.values())
    total_d = 0
    for c in LETTER_FREQUENCY:
        if c in counts:
            d = (counts[c] / n_char - LETTER_FREQUENCY[c]) ** 2
        else:
            d = LETTER_FREQUENCY[c] ** 2

        total_d += d

    return total_d / len(LETTER_FREQUENCY)


def calc_shift(counts):
    dists = {}

    for shift in range(26):
        shift_counts = {}
        k = chr(shift + ord('A'))
        for c in counts:
            shift_c = chr((ord(c) - ord(k)) % 26 + ord('A'))
            shift_counts[shift_c] = counts[c]
        dists[k] = freq_distance(shift_counts)

    sorted_dist = {}
    for k in sorted(dists, key=lambda x: dists[x]):
        sorted_dist[k] = round(dists[k], 2)

    return sorted_dist


def main():
    # cipher_text = 'KZFQ QQXLYPFYXM JIJS GSQIIMX CEXNT III XZPQII'
    # key = 'FIRE'
    # decode(cipher_text, key)

    with open('s1.txt') as f:
        s = ''.join(f.readlines())

    # for i in range(10, 1, -1):
    #     max_ss, sub_strings = substring(s, i)
    #     for j in range(5):
    #         try:
    #             print(max_ss[j], sub_strings[max_ss[j]], end=',')
    #         except IndexError:
    #             continue
    #     print()

    key_length = 5
    key = ''
    for e in freq(s, key_length):
        print(e)
        dists = calc_shift(e)
        print(dists)
        key += min(dists, key=lambda x: dists[x])

    print(key)
    decode(s, key)


if __name__ == '__main__':
    main()
