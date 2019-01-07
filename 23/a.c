#include <stdio.h>
#include <stdbool.h>

int main(void) {
  int a = 1LL;
  int b = 0LL;
  int c = 0LL;
  int d = 0LL;
  int e = 0LL;
  int f = 0LL;
  int g = 0LL;
  int h = 0LL;
  int j = 0LL;


line1: b = 79;
line2: c = b;
line3: if (a) { goto line5;};
line4: if (1) { goto line9;};
line5: b *= 100;
line6: b += 100000;
line7: c = b;
line8: c += 17000;
line9: f = 1;
line10: d = 2;
line11: e = 2;
line12: g = d;
line13: g *= e;
line14: g -= b;
line15: if (g) { goto line17;};
line16: f = 0;
line17: e += 1;
line18: g = e;
line19: g -= b;
line20: if (g) { goto line12;};
line21: d += 1;
line22: g = d;
line23: g -= b;
line24: if (g) { goto line11;};
line25: if (f) { goto line27;};
line26: h += 1;
line27: g = b;
line28: g -= c;
line29: if (g) { goto line31;};
line30: if (1) { goto line33;};
line31: b += 17;
line32: if (1) { goto line9;};

line33:
    printf("Out of range: %d\n", h);
  return 0;
}
