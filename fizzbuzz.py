if __name__ == '__main__':
    n = int(input())

    for i in range(1, n+1):
        f = 0
        b = 0
        if i%3 == 0:
            f = 1
        if i%5 == 0:
            b = 1

        if f == 1 and b == 0:
            print("fizz", end="")
        elif f == 0 and b == 1:
            print("buzz", end="")
        elif f == 1 and b == 1:
            print("fizzbuzz", end="")
        else:
            print(i, end="")
        if i != n:
            print(",", end="")