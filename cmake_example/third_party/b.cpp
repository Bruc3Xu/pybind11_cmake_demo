#include "b.h"

LIB_API int divide(int a, int b) {
  if (b == 0) return -1;
  return add_PI(a, b) / b;
}
