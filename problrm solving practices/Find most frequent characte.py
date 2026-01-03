def build_freq(s, i, freq):
    if i == len(s):
        return freq

    ch = s[i]
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

    return build_freq(s, i + 1, freq)


def most_freq_recursive(s, i, freq, max_char, max_count):
    if i == len(s):
        return max_char

    ch = s[i]
    if freq[ch] > max_count:
        return most_freq_recursive(s, i + 1, freq, ch, freq[ch])
    else:
        return most_freq_recursive(s, i + 1, freq, max_char, max_count)


# Driver
s = "banana"
freq = build_freq(s, 0, {})
print("Most frequent character:", most_freq_recursive(s, 0, freq, '', 0))
