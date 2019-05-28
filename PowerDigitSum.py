def number(N,raised):
    result = N**raised
    result = list(str(result))
    total = 0
    for i in range(len(result)):
        total+=int(result[i])

    print(total)



number(2,1000)