

# calculate a stream operator for odd/even
def k(ls):
    v = ls[0]
    for x in ls[1:]:
        v = not (v ^ x)
    return v

# calculate
def generator(ls, max):
    vNext = k(ls)
    print vNext

    if max==1:
        return

    # generate new list with vNext and last remainingg of list
    generator(ls[1:] + [vNext], max-1)

    return

def genTop(ls, max):
    print(ls)
    generator(ls, max)

# take first, generate next, save

# binary stream to true false array



if __name__ == "__main__":

    genTop([False, False], 2)
    print("-----------------")

    generator([False, False], 2)
    print("-----------------")

    genTop([False, False], 8)
    print("-----------------")

    generator([False, False], 8)
    print("-----------------")

    generator([True, True], 8)

    print("-----------------")

    generator([True, False], 8)

    print("-----------------")

    print((k([False, False]) == True))
    print((k([False, True]) == False))
    print((k([True, False]) == False))
    print((k([True, True]) == True))

    print((k([False, False, False]) == False))
    print((k([False,False, True]) == True))
    print((k([False,True, False]) == True))
    print((k([False,True, True]) == False))
    print((k([True,False, False]) == True))
    print((k([True,False, True]) == False))
    print((k([True,True, False]) == False))
    print((k([True,True, True]) == True))

