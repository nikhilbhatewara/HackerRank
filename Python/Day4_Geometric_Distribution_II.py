#!/usr/bin/python
# -*- coding: utf-8 -*-

# p defective is 1/3
# during 5th inspection => n=5


def g(n, p):
    return (1 - p) ** (n - 1) * p


p = 1 / 3

output = 0
for n in range(1, 6):
    output = output + g(n, p)

print round(output, 3)
