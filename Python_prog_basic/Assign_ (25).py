# Q1
def fun(a, b, c):
    if a == b and b == c and c == a:
        print(3)
    elif a == b or b == c or c == a:
        print(2)
    else:
        print(0)
    return 1


(fun(3, 4, 3))

# Q2


def dict_to_list(d):
    l = list(d.items())
    l.sort()
    print(l)
    return 1


dict_to_list({
    "D": 1,
    "B": 2,
    "C": 3
})

# Q3


def mapping(l):
    d = {}
    for i in range(len(l)):
        d[l[i].lower()] = l[i].upper()
    print(d)
    return 1


mapping(["a", "v", "y", "z"])

# Q4


def vow_replace(s, v):
    vw = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vw)):
        if vw[i] in s:
            t = s.replace(vw[i], v)
            s = t

    print(t)
    return 1


vow_replace("apples and bananas", "u")
# Q5


def ascii_capitalize(s):
    l = list(s)
    for i in range(len(l)):
        if l[i].isalpha():
            if ord(l[i]) % 2 != 0:
                l[i] = l[i].lower()

            else:
                l[i] = l[i].upper()

    ls = "".join(l)
    print(ls)
    return 1


ascii_capitalize("to be or not to be!")
