a = 0
b = 79
c = b
b = 107900
c = b + 17000

while True:
    d = 1
    e = 2
    while True:
        f = 2
        while True:
            if f * e == b:
                d = 0

            f = f + 1
            if f == b:
                break
            else:
                continue
        e = e + 1
        if e == b:
            break
        else:
            continue

    if d == 0:
        a = a + 1

    if b == c:
        break

    b = b + 17

print("Out of range: %d\n", a)
