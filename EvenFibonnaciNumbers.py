def fibonacci():
    lst = [1,2]
    sum = 2
    while lst[-1]<4000000:
        newNum = lst[-1]+lst[-2]
        if(newNum%2==0):
            sum+=newNum
            print(newNum)
        lst.append(newNum)
    print("the sum of the even numbers is: "+str(sum))
    print(lst)

fibonacci()