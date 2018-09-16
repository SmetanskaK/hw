def gen_primes():
    lst = []
    for i in range(2, 100):
        for k in range(2, i):
            if i % k == 0:
                break
        else:
                lst.append(i)
    return lst


print(gen_primes())
