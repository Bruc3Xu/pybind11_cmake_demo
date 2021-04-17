#include "b.h"

int __declspec(dllexport) divide(int a, int b)
{
  if (b == 0)
    return -1;
  return add_PI(a, b) / b;
}