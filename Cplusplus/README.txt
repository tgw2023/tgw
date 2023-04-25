# tgw
TGW API

1.目录文件概览
├─Cplusplus		---C++版本目录
    │  README.txt
    │  中国银河证券格物金融服务平台(TGW)开发手册(C++版).pdf
    │  
    ├─Redhat-7.6
    │  │  tgw_install.sh	---tgw库安装脚本
    │  │  
    │  └─c++
    │      ├─demo		--- demo样例程序
    │      │      make.sh	--- 样例程序编译脚本
    │      │      Makefile	--- tgw_demo.cpp编译的Makefile文件
    │      │      tgw_demo.cpp	--- demo样例程序
    │      │      tgw_push_spi.cpp
    │      │      tgw_push_spi.h
    │      │      tgw_query_spi.cpp
    │      │      tgw_query_spi.h
    │      │      tgw_replay_spi.cpp
    │      │      tgw_replay_spi.h
    │      │      
    │      ├─include		--- 所需头文件
    │      │      tgw.h
    │      │      tgw_datatype.h
    │      │      tgw_export.h
    │      │      tgw_history_spi.h
    │      │      tgw_struct.h
    │      │      
    │      ├─lib		--- 库文件,包含库依赖文件
    │      │      .ca.crt
    │      │      libaaf.so
    │      │      libadk.so
    │      │      libami.so
    │      │      libamigrpc++.so
    │      │      libamigrpc.so
    │      │      libcrypto.so.10
    │      │      libentry_wrapper.so
    │      │      libfmdutil.so
    │      │      libllmi.so
    │      │      libpcap.so.1
    │      │      librmm.so
    │      │      librum.so
    │      │      libsample_engine.so
    │      │      libssh.so.4
    │      │      libssl.so.10
    │      │      libtgw.so
    │      │      libz.so.1
    │      │      
    │      └─test_tool		--- test测试工具（具体使用参见使用文档）
    │          │  run.sh
    │          │  
    │          ├─bin
    │          │      tgw_test
    │          │      
    │          └─etc
    │                  tgw.json
    │                  
    └─Windows
        │  tgw_install.bat
        │  
        └─c++
            ├─demo			--- demo样例程序
            │  │  tgw_demo.cpp		--- demo样例程序
            │  │  tgw_push_spi.cpp
            │  │  tgw_push_spi.h
            │  │  tgw_query_spi.cpp
            │  │  tgw_query_spi.h
            │  │  tgw_replay_spi.cpp
            │  │  tgw_replay_spi.h
            │  │  
            │  └─project
            │      │  tgw_demo.sln		--- 样例程序VS解决方案
            │      │  
            │      └─tgw_demo
            │              tgw_demo.vcxproj
            │              tgw_demo.vcxproj.filters
            │              tgw_demo.vcxproj.user
            │              
            ├─include			--- 所需头文件
            │      tgw.h
            │      tgw_datatype.h
            │      tgw_export.h
            │      tgw_history_spi.h
            │      tgw_struct.h
            │      
            ├─lib			--- 库文件,包含库依赖文件
            │      .ca.crt
            │      boost_random-vc140-mt-1_62.dll
            │      boost_system-vc140-mt-1_62.dll
            │      libcrypto-1_1-x64.dll
            │      libssl-1_1-x64.dll
            │      tgw.dll
            │      tgw.lib
            │      tgw.pdb
            │      
            └─test_tool			--- test测试工具（具体使用参见使用文档《中国银河证券格物金融服务平台(TGW)开发手册(C++版).pdf》）
                │  run.bat
                │  
                ├─bin
                │      tgw_test.exe
                │      
                └─etc
                        tgw.json

2.运行系统环境
Redhat7.2、Redhat 7.4、Redhat 7.6、Win10

3.环境准备
1)包外层含有tgw_install.sh脚本，主要用于互联网模式环境变量设置和证书配置
2)运行该脚本请使用命令：source tgw_install.sh
3)不使用source运行时，环境变量将无法即时在本终端生效，需要另起终端或者手动source ~/.bash_profile

4.C++版本编译使用步骤：
1) 进入到目录
cd c++

2)编译tgw_demo.cpp
make
make install   --- 将tgw_demo到bin目录下
make clean     --- 清除./目录下的*.o文件

3) 运行 (在当前目录下运行)
LD_LIBRARY_PATH=./lib ./bin/tgw_demo

4) make.sh脚本包含了make makeinstall等操作，可直接运行make.sh脚本

5) Windows系统下，请使用Visual Studio编辑器打开tgw_demo.sln解决方案，进行编译（VS2013、VS2015、VS2017均支持）

6)tgw_test使用步骤如下
该demo为tgw标准测试样例程序，支持参数配置，数据选择性输出，落地csv文件。
a) 修改参数
test_tool/etc/tgw.json关键参数更改
{
    "ApiMode":1,                        // API模式，1：托管机房模式 2：互联网模式
    "CsvFileDir": "./",                 // csv文件保存地址
    "CommandMode": 1,                   // 命令输入模式 1：动态输入命令 2：文件读取命令
    "DynamicSubscribeIp": "127.0.0.1",  // 动态订阅ip地址，仅可为本机ip地址
    "DynamicSubscribePort":8017,        // 动态订阅端口，可改动
    "ReqFile":"./req_file.txt",         // 查询命令文件路径及文件
    "ServerVip": "127.0.0.1",           // nginx vip地址
    "ServerPort": 9200,                 // nginx 端口
    "UserName" : "amd",                 // 用户名
    "Password" : "amd@2022",            // 密码

    "ColocChannelMode": ["TCP"],        // 托管机房模式 ["TCP","QTCP","RTCP"] 通道模式（ApiMode为1时需要配置）
    "ColocQTcpReqTimeOut": 1,           // 托管机房模式 QTCP查询通道请求超时时间
    "ColocQTcpChannelThread": 2,        // 托管机房模式 QTCP查询解析线程数
    "ColocQTcpMaxReqCnt": 100,          // 托管机房模式 QTCP查询最大请求数
    "MinLogLevel": 2                    // 输出日志等级，默认info级别
}

b) 运行 ./run.sh即可启动tgw_test程序
    具体关于该工具使用说明参照《中国银河证券格物金融服务平台(TGW)开发手册(C++版).pdf》文档