freq = {}

uInput = input("Key in your data : ")
for word in uInput.split():
    freq[word] = freq.get(word,0) + 1

words = freq.keys()
words = sorted(words)

for w in words:
    print("{} : {}".format(w,freq[w]))