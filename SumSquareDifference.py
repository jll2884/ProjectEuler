def sum(N):
    totalsquare = 0
    totalsum = 0
    for i in range(1,N+1,1):
        totalsquare+=i**2
        totalsum+=i
    squared = totalsum**2
    diff = squared-totalsquare

    print(diff)

sum(100)
