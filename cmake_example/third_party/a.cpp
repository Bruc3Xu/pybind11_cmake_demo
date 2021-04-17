#include "a.h"

int __declspec(dllexport) add_PI(int a, int b)
{
  return a + b + PI;
}