if __name__ == '__main__':
    input()
    inp = input()
    out = ""
    for x in inp:
        if x == 'R':
            out += 'D'
        if x == 'D':
            out += 'R'
    print(out)

