
# ! Write a Python Program to Check if a Number is Positive, Negative or Zero?

def num(n):
    if n > 0:
        return "Positive"
    elif n == 0:
        return "Zero"
    else:
        return "Negative"


print(num(5))
# ! Write a Python Program to Check if a Number is Odd or Even?


def num(n):
    if n % 2 == 1:
        return "Odd"
    else:
        return "Even"


print(num(5))

# ! Write a Python Program to Check Leap Year?


def leap(y):
    if y % 400 == 0:
        return "It is a leap year"
    elif y % 100 == 0:
        return "It is not a leap year"
    elif y % 4 == 0:
        return "It is a leap year"
    else:
        return "It is not a leap year"


print(leap(1700))
print(leap(2000))
print(leap(2021))

# ! Write a Python Program to Check Prime Number?


def prim(n):
    cnt1 = 1
    for j in range(2, n):
        if n % j == 0:
            cnt1 = 0
        # else:
         #   cnt2 = 1
    if cnt1 == 1:
        return "It is a prime number"
    else:
        return "It is not a prime number"


print(prim(1))

# ! Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


def prim():
    i = 4
    l = [1, 2, 3]
    while(i <= 10000):
        cnt1 = 1
        for j in range(2, i):
            if i % j == 0:
                cnt1 = 0
            # else:
             #   cnt2 = 1
        if cnt1 == 1:
            l = l + [i]

        i = i + 1
    return l


print(prim())
