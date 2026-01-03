ch=input("Enter string:")
v='a','e','i','o','u'
if (ch.isalpha()):
    if ch.lower() in v:
        print("vowel")
    else:
        print("consonants")
else:
   print("not an alphabet")
    