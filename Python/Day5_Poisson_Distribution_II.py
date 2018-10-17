meanA = 0.88
meanB = 1.55

meanA2 = meanA + meanA**2
meanB2 = meanB + meanB**2

CostA = 160+(40*meanA2)

CostB = 128+(40*meanB2)


print('%.3f' % CostA)
print('%.3f' % CostB)
