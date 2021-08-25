#ifndef UTILS_H_
#define UTILS_H_

#if defined(WIN32) || defined(_WIN64)

#ifdef LIB_EXPORTS
#define LIB_API extern "C" __declspec(dllexport)
#else
#define LIB_API extern "C" __declspec(dllimport)
#endif  // LIB_EXPORTS

#elif defined __linux__

#ifndef LIB_API
#define LIB_API extern "C"
#endif  // LIB_API

#endif  // defined (WIN32) || defined (_WIN64)

#endif
