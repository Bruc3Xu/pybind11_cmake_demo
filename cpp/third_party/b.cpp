#include "../include/b.h"


LIB_API double divide(double a, double b)
{
  if (b == 0.0)
    return -1.0;
  return a / b;
}
