import math
maxW = int(input())
nBox = int(input())
dMean = int(input())
dStd = int(input())

mean = nBox * dMean


std = math.sqrt(nBox) * dStd


def cdf(x): return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))


# Less than maxW
print('{:.4f}'.format(cdf(maxW)))
