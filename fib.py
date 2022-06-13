if __name__ == '__main__':
    n = int(input())

    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c

    if n < 2:
        print(n)
    elif n == 2:
        print(1)
    else:
        print(a)

