import math
mean, std = 70, 10


def cdf(x): return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


# More than 80 => 1 - P(less than 80)
print('{:.2f}'.format(100*(1-cdf(80))))
# More than 60
print('{:.2f}'.format(100*(1 - cdf(60))))
# Less than 60
print('{:.2f}'.format(100*cdf(60)))
