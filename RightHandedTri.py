def RightHandTri():
    triangle = int(input("Enter number: "))
    for t in range(triangle):
        for a in range(t+1):
            print("#",end='')
        print("")
RightHandTri()        