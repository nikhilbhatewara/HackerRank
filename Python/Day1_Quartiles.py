#!/usr/bin/python
# -*- coding: utf-8 -*-
digits = int(input())
values_input = input()
values_list = list(values_input.split(' '))
values = [int(v) for v in values_list]

#get median of series
def getmedian(digits, values):
    values = sorted(values)
    mid = (digits - 1) // 2

    if digits % 2 != 0:
        return values[mid]
    else:
        return (values[mid] + values[mid + 1]) / 2.0


def getparts(series):
    series = sorted(series)
    digits = int(len(series))
    mid_series = getmedian(digits, series)
    lower = [None] * (digits // 2)
    higher = [None] * (digits // 2)
    lower.clear()
    higher.clear()
    #if there are odd number of values, then we will not include middle value in quartile calculation
    if digits % 2 == 0:
        for s in series:
            if s < mid_series:
                lower.append(s)
            else:
                higher.append(s)
    else:
        for s in series:
            if s < mid_series:
                lower.append(s)
            elif s == mid_series:
                pass
            else:
                higher.append(s)
    return (lower, higher)


(L, H) = getparts(values)

# print(L)
# print(H)

q1 = getmedian(int(len(L)), L)
q2 = getmedian(digits, values)
q3 = getmedian(int(len(H)), H)
print int(q1)
print int(q2)
print int(q3)
