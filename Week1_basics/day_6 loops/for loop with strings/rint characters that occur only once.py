text = 'aapllee'
m = ''

for ch in text:
    count = 0
    for chh in text:         # manually count occurrences
        if ch == chh:
            count += 1
    if count == 1:           # keep only if appears once
        m += ch

print("Characters that appear only once:", m)

