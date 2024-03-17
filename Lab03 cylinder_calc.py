# For this lab, you will be creating a cylinder “stats” calculator!
# First, create a file called “cylinder_calc.py” to house your lab work. In this file, you will write 5 different
# functions. The section Cylinder Formulas describes the first 4 functions that you will write, and the
# section Printing Function describes the last function.
# By the end of this lab, you should be more comfortable creating and using functions. You will also see
# that functions help make your life easier by allowing you to repeat calculations very easily!


def Surface_Area(r, h):
    pi = 3.14
    r = int(r)
    h = int(h)
    a = 2 * pi * r * h + 2 * pi * r ** 2
    return a

def Volume(r, h):
    pi = 3.14
    r = int(r)
    h = int(h)
    a = pi * r ** 2 * h
    return a

def Lateral_Area(r, h):
    pi = 3.14
    r = int(r)
    h = int(h)
    a =  2 * pi * r * h
    return a

def Base_Area(r,h):
    pi = 3.14
    r = int(r)
    h = int(h)
    a = pi * r ** 2
    return a

def Print_Cylinder(r, h):
    SA = Surface_Area(r, h)
    V = Volume(r, h)
    LA = Lateral_Area(r, h)
    BA = Base_Area(r, h)
    print("Radius:", r)
    print("Height:", h)
    print("Surface Area:", SA)
    print("Volume:", V)
    print("Lateral Area:", LA)
    print("Base Area:", BA)
    return SA

r = input("The radius of the thing: ")
h = input("The height of the thing: ")
Print_Cylinder(r, h)







