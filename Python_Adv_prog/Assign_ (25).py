
# * 1. rite four functio that directly mutate a list

import numpy as np
import numpy as numpy


def repeat(lst, n):  # Repeat lst n times.
    return lst * n


def add(lst, x):  # Adds x to the end of the lst.
    lst.append(x)
    return lst


# Removes all elements between indices m and n inclusive in lst.
def remove(lst, m, n):
    for i in range(m, n):
        lst.pop(m)
    return lst


def concat(lst, x):  # concatenates lst with x(another list).
    lst = lst + x
    return lst


lst = [1, 2, 3, 4]
n = 3
x = 1
m = 1
n1 = 12
lst = repeat(lst, n)
print(lst)
lst = add(lst, x)
print(lst)
lst = remove(lst, m, n1+1)
print(lst)
lst = concat(lst, [3, 4])
print(lst)


# * 2. Mastermind game

def guess_score(m, n):
    b = 0
    w = 0
    d = {}
    m = list(m)
    n = list(n)
    m_l = len(m)-1
    if len(m) == len(n) and (len(m) == 4 or len(m) == 6):
        for i in range(m_l):
            if m[i] == n[i]:
                b = b+1
                m.remove(m[i])
                n.remove(n[i])
                m_l = m_l - 1

        # print(m, n, m_l)
        n_s = list(set(n))
        m_s = list(set(m))
        # print(n_s, m_s)
        for i in range(len(n_s)):
            if n_s[i] in m_s:
                w = w + 1

        # print(m, n, m_l)

    else:
        print("No Rule followed")

    d = {"black": b, "white": w}
    return d


print(guess_score("1423", "5678"))
print(guess_score("1423", "2222"))
print(guess_score("1423", "1234"))
print(guess_score("1423", "2211"))


#  * 3. Product of two numbers in the list

def two_product(l, n):
    m = len(l)
    for i in range(m):
        for j in range(len(l)-1):
            if i != j and l[j]*l[i] == n:
                return [l[j], l[i]]


print(two_product([1, 2, -1, 4, 5], 20))  # ➞ [4, 5]

print(two_product([1, 2, 3, 4, 5], 10))  # ➞ [2, 5]

print(two_product([100, 12, 4, 1, 2], 15))  # ➞ None


# * 4.  Sort Dates

def sort_dates(dats, order):
    if order == 'ASC':
        dats.sort()
        return dats
    elif order == 'DSC':
        dats.sort(reverse=True)
        return dats
    else:
        return "Order is not correct"


print(sort_dates(
    ["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC"))
print(sort_dates(
    ["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC"))

# * 5 informed to support for correction


def same_vowel_group(l):
    v = ['a', 'e', 'i', 'o', 'u']
    k = []
    str = ""
    for i in range(len(l)-1):
        for j in range(5):
            if v[i] in l[i]:
                str = str+v[i]

        k.append(str)
    print(k)
    return k


same_vowel_group(["toe", "ocelot", "maniac"])  # ➞ ["toe", "ocelot"]

same_vowel_group(["many", "carriage", "emit",
                 "apricot", "animal"])  # ➞ ["many"]

same_vowel_group(["hoops", "chuff", "bot", "bottom"]
                 )  # ➞ ["hoops", "bot", "bottom"]


# * 6 LCM


def lcm_of_list(l):
    print(np.lcm.reduce(l))
    return


lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # ➞ 2520

lcm_of_list([13, 6, 17, 18, 19, 20, 37])  # ➞ 27965340

lcm_of_list([44, 64, 12, 17, 65])  # ➞ 2333760
