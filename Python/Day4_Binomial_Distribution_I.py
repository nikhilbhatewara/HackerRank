#!/usr/bin/python
# -*- coding: utf-8 -*-
# ratio of boys to girls= 1.09:1
# ration of boys= 1.09/(1.09+1) = 1.09/2.09


def factorial(n):
    return (1 if n == 1 or n == 0 else n * factorial(n - 1))


def b(x, n, p):
    fact_nx = factorial(n) / (factorial(x) * factorial(n - x))
    px = pow(p, x)
    q = 1 - p
    qnx = pow(q, n - x)
    return fact_nx * px * qnx


def listb(X, n, p):
    total_p = 0
    for x in X:
        total_p = total_p + b(x, n, p)
    return total_p


# here we want to calculate atleast 3 boys hence

X = [3, 4, 5, 6]
n = 6
p = 1.09 / 2.09

output = listb(X, n, p)

output = round(output, 3)
print output
