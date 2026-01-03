def vowels_count(vowels):
    text="aeiouAEIOU"
    count=0
    for ch in vowels:
        if ch in text:
            count+=1
    return count
print(vowels_count("PYyhon is amazing"))