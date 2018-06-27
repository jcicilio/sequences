

# calculate a stream operator for odd/even
def k(ls):
    v = ls[0]
    for x in ls[1:]:
        v = not (v ^ x)
    return v

# calculate
def generator(ls, max, r):
    vNext = k(ls)
    r.append(vNext)

    if max==1:
        return r

    # generate new list with vNext and last remainingg of list
    generator(ls[1:] + [vNext], max-1, r)

    return r

# take first, generate next, save

# binary stream to true false array

def s(n):
    r = []
    for k in range(2**n):
        t = 2**(n-1)
        v = []
        for j in range(n):
            v.append(bool(t & k))
            t /=2
        r.append(v)

    return r


def a(n):
    # generate values
    for i in range(2, n+1):
        # set to test
        set = s(i)
        for j in range(len(set)):
            with open("/temp/test.out", "a") as myfile:
                myfile.write(("\""+str(set[j])+"\" -> \""+str(generator(set[j],i,[]))+"\"\n").replace(" ",""))
            print ("\""+str(set[j])+"\" -> \""+str(generator(set[j],i,[]))+"\"").replace(" ","")

    return


if __name__ == "__main__":

    a(10)
    print("-----------------")

    print s(3)
    print("-----------------")



    print(generator([False, False], 2,[]))
    print("-----------------")



    generator([False, False], 8,[])
    print("-----------------")

    generator([True, True], 8,[])

    print("-----------------")

    generator([True, False], 8,[])

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

