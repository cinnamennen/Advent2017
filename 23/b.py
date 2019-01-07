a = 0
b = 0x4f
c = b
b = 0x1a57c
c = b + 0x4268

while True:
    d = 0x1
    e = 0x2
    while True:
        f = 0x2
        while True:
            if f * e == b:
                d = 0x0

            f = f + 0x1
            if f == b:
                break
            else:
                continue
        e = e + 0x1
        if e == b:
            break
        else:
            continue

    if d == 0x0:
        a = a + 0x1

    if b == c:
        break

    b = b + 0x11

print("Out of range: %d\n", a)
