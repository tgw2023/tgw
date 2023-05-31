#pragma once
#if defined (_WIN32)                                //Windows
    #if !defined (TGW_HAS_DLL)
        #define TGW_HAS_DLL 1
    #endif

    #if defined TGW_HAS_DLL && (TGW_HAS_DLL == 1)   //动态库
        #if defined (TGW_BUILD_DLL)
            #define TGW_EXPORT __declspec(dllexport)
        #else /* TGW_BUILD_DLL */
            #define TGW_EXPORT __declspec(dllimport)
        #endif /* TGW_BUILD_DLL */
    #else                                           // 静态库
        #define TGW_EXPORT
    #endif
#else /* !_WIN32 */                                 // linux
    #define TGW_EXPORT
#endif /* _WIN32 */
