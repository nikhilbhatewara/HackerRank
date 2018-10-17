#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
digits = int(input())
X_input = input()


def convertinput(a):
    x = list(a.split(' '))
    y = [int(float(i)) for i in x]
    return y


X = convertinput(X_input)


def mean(x):
    s = sum(x)
    m = s / len(x)
    return m


mean_x = mean(X)


def sd(A):
    m = mean(A)  # mean of A
    p = []
    for a in A:
        p.append(m - a)
    p = [i ** 2 for i in p]
    sp = sum(p)  # sum of p
    N = len(A)
    sigma = math.sqrt(sp / N)
    return sigma


print '%.1f' % sd(X)
