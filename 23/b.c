int _main() {
int a,b,c,d,e,f,g,h,mul;
    a = 0x0;
    mul = 0x0;
    b = 0x4f;
    c = b;
    if (0x1 != 0x0) {
            mul = 0x1;
            b = 0x1a57c;
            c = b - 0xffffffffffffbd98;
    }
    do {
            d = 0x1;
            e = 0x2;
            do {
                    f = 0x2;
                    do {
                            mul = mul + 0x1;
                            if (f * e == b) {
                                    d = 0x0;
                            }
                            f = f - 0xffffffffffffffff;
                            if (f == b) {
                                break;
                            }
                            else {
                                continue;
                            }
                    } while (true);
                    e = e - 0xffffffffffffffff;
                    if (e == b) {
                        break;
                    }
                    else {
                        continue;
                    }
            } while (true);
            if (d == 0x0) {
                    a = a - 0xffffffffffffffff;
            }
            if (b == c) {
                break;
            }
            b = b - 0xffffffffffffffef;
    } while (true);
    printf("Out of range: %lld\n", 0x0);
    printf("Mul: %lld\n", mul);
    return 0x0;
}
