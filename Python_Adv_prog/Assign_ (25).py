
# * Write four functio that directly mutate a list

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
