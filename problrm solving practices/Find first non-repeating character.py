def build_freq(s, i, freq):
    if i == len(s):
        return freq

    ch = s[i]
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

    return build_freq(s, i + 1, freq)
def first_non_repeat(s, i, freq):
    if i == len(s):
        return None

    if freq[s[i]] == 1:
        return s[i]

    return first_non_repeat(s, i + 1, freq)
s = "swiss"
freq = build_freq(s, 0, {})
print(first_non_repeat(s, 0, freq))
