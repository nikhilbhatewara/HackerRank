#!/usr/bin/python
# -*- coding: utf-8 -*-
digits = int(input())
X_input = input()
W_input = input()


def convertinput(a):
    x = list(a.split(' '))
    y = [int(float(i)) for i in x]
    return y


p = [0] * digits
X = convertinput(X_input)
W = convertinput(W_input)

for i in range(0, digits):
    p[i] = X[i] * W[i]

num = sum(p)
den = sum(W)

wmean = float(num / den)
print('%.1f' % wmean)
