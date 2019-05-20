def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)

def total(n):
    arr = list(str(n))
    total = 0
    for i in arr:
        total+=int(i)
    return total


if __name__ == '__main__':
    number = factorial(100)
    print(total(number))
