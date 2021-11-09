setA = input("Enter list A and space the values:")
lisA = setA.split()
setB = input("Enter listB and space the values:")
lisB = setB.split()
lisC = []
lisD = []
listE = []
def subset():
    for item1 in lisB:
        for item2 in lisA:
            if item1 == item2:
                listE.append(item1)
    if bool(listE) is True and listE == lisB:
        print("B is a subset of A")
    else:
        print("B is not a subset of A")

def set_difference():
    for item1 in lisA:
        if item1 not in lisB:
            lisC.append(item1)

    print("A-B=", lisC)

def cartesian_product():
    for item1 in lisA:
        for item2 in lisB:
            v = item1, item2
            lisD.append(v)
    print("AxB=", lisD)


subset()
set_difference()
cartesian_product()

