s = "bankai i kk we ret"
count = 0
prev_space = True   # ← THIS IS THE KEY

for ch in s:
    if ch != ' ' and prev_space:
        count += 1
    prev_space = (ch == ' ')

print(count)
