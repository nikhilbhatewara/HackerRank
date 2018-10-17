#!/usr/bin/python
# -*- coding: utf-8 -*-

# since 12% have faults, 82% are correct
# p=0.82


def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)


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


# Since we want no more than 2 rejects then
# for Q1 let us calculate total probability of rejects

X = [0, 1, 2]
n = 10
p = 0.12

p_q1 = listb(X, n, p)

# this is the probability of having atmost 2 rejects

# Q2, probability of at least 2 rejects

X = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]
n = 10
p = 0.12

p_q2 = listb(X, n, p)

print(round(p_q1, 3))
print(round(p_q2, 3))
