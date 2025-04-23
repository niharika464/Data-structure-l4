def printfactors(number):
    print("factors of this nuber are:")
    for i in range(1, number+1):
        if number %i==0:
            print(i)


number = int(input("Insert the no. to find its factors:"))
printfactors(number)
