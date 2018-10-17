l = 2.5
k = 5


def factorial(n):
    return (1 if n == 1 or n == 0 else n * factorial(n - 1))


def poisson(l, k):
    e = 2.71828
    numerator = ((l ** k) * (e ** (-l)))
    denominator = factorial(k)
    probability = numerator/denominator
    return probability


def listpoisson(l, K):
    total_probability = 0
    for k in K:
        total_probability = total_probability + poisson(l, k)
    return total_probability


K = range(0, 4)
p = poisson(l, k)

print('%.3f' % p)
