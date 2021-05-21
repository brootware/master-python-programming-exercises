def integral(n):
    ht = {}
    for i in range(n+1):
        ht[i] = i*i

    return ht

print(integral(8))