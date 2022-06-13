if __name__ == '__main__':
    inp = list(input())
    key = list(input())
    out = ""
    for i in range(len(inp)):
        new = chr((ord(inp[i])-65 + ord(key[i])-65) % 26+65)
        out+=new
    print(out)

