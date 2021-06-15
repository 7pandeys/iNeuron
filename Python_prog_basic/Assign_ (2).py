
# ! Write a Python program to convert kilometers to miles?
import cmath
import calendar


def km_m(km):
    try:
        val = float(km)
        print("{:.2f} miles in {:.4f} kilometers :".format(val*0.6214, val))
    except ValueError:
        print("That's not an numerical value!")
    return 1  # 0.6214*km


km_m("2")
km_m(5.1)
km_m(6)
km_m("Cobra")

# ! Write a Python program to convert Celsius to Fahrenheit?


def c_f(temp):
    try:
        val = float(temp)
        print("{:.2f} Fahrenheit in {:.1f} Celsius :".format((val*9)/5, val))
    except ValueError:
        print("That's not an numerical value!")
    return 1  # 0.6214*km


c_f("2")
c_f(5.1)
c_f(6)
c_f("Cobra")


# ! Write a Python program to display calendar?
def cal(y, m):
    try:
        year = int(y)
        month = int(m)
        # display the calendar
        print(calendar.month(year, month))
    except ValueError:
        print("That's not an numerical value!")
    return 1


cal(2021, 6)
cal(2021, 'jun')
cal(1000, 5)

# ! Write a Python program to solve quadratic equation?

# import cmath


def quad(x, a=1, b=2, c=4):
    #a = input("Enter value")
    print("Equation : {0}*{1}**2 + {2}*{3} + {4}".format(a, x, b, x, c))

    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # fine two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('The solution are {:.2f} and {:.2f}'.format(sol1, sol2))

    return 1


quad(9)


# ! Write a Python program to swap two variables without temp variable?

def swap(v1, v2):
    print("Before swap :\t v1 = {v1} \t v2 = {v2}".format(v1=v1, v2=v2))
    v1 = v1 + v2
    v2 = v1 - v2
    v1 = v1 - v2

    print("After swap :\t v1 = {v1} \t v2 = {v2}".format(v1=v1, v2=v2))
    return 1


swap(6, 7)
