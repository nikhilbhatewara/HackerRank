#!/usr/bin/python
# -*- coding: utf-8 -*-
import statistics
import scipy.stats as sts
import operator
import numpy as np

digits = int(input())
values = input()
values_list = list(values.split(' '))

values_new = [int(v) for v in values_list]

mean_value = np.mean(values_new)


def getmedian(digits, values):
    values = sorted(values)
    mid = (digits - 1) // 2

    if digits % 2 != 0:
        return values[mid]
    else:
        return (values[mid] + values[mid + 1]) / 2.0


median_value = getmedian(digits, values_new)
mode_value = sts.mode(values_new)

print mean_value
print median_value
print int(mode_value[0])
