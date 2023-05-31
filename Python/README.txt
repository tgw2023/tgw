# tgw
TGW API

1.目录文件概览
├─Python
    │  README.txt
    │  中国银河证券格物金融服务平台(TGW)开发手册(Python版本).pdf
    ├─dist
    │      tgw-1.0.3-py3-none-any.whl        ---python版本TGW安装wheel包
    │  
    ├─Redhat-7.6
    │  ├─python3.6			--- python3.6版本目录
    │  │  │  pip_install.sh		--- tgw的wheel包安装脚本
    │  │  │  pip_uninstall.sh		--- tgw已安装python库卸载脚本
    │  │  │  pushdemo.sh		--- json接口推送示例脚本
    │  │  │  querydemo.sh		--- DataFrame或json接口同步方式查询示例脚本
    │  │  │  replaydemo.sh		--- DataFrame或json接口回放示例脚本
    │  │  │  run_demo.sh		--- 异步方式tgw_demo.py的执行脚本
    │  │  │  run_test36.sh		--- tgw_test.py的执行脚本
    │  │  │      
    │  │  └─etc			--- 配置文件
    │  │  │      test.json		--- tgw_test.py所需配置文件
    │  │  │      
    │  │  └─src
    │  │      ├─demo			--- 样例程序
    │  │      │      push_sample.py	
    │  │      │      query_sample.py
    │  │      │      replay_sample.py
    │  │      │      tgw_demo.py
    │  │      │      
    │  │      └─test			--- 样例程序（用于数据落csv文件）
    │  │              data_writer.py
    │  │              tgw_commom.py
    │  │              tgw_output_file.py
    │  │              tgw_test.py
    │  │          
    │  └─python3.8			--- python3.8版本目录
    │      │  pip_install.sh		--- tgw的wheel包安装脚本
    │      │  pip_uninstall.sh		--- tgw已安装python库卸载脚本
    │      │  pushdemo.sh		--- json接口推送示例脚本
    │      │  querydemo.sh		--- DataFrame或json接口同步方式查询示例脚本
    │      │  replaydemo.sh		--- DataFrame或json接口回放示例脚本
    │      │  run_demo.sh		--- 异步方式tgw_demo.py的执行脚本
    │      │  run_test38.sh		 --- tgw_test.py的执行脚本
    │      │      
    │      └─etc			--- 配置文件
    │      │      test.json		--- tgw_test.py所需配置文件
    │      │      
    │      └─src
    │          ├─demo			--- 样例程序
    │          │      push_sample.py
    │          │      query_sample.py
    │          │      replay_sample.py
    │          │      tgw_demo.py
    │          │      
    │          └─test			--- 样例程序（用于数据落csv文件）
    │                  data_writer.py
    │                  tgw_commom.py
    │                  tgw_output_file.py
    │                  tgw_test.py
    │              
    └─Windows
        ├─python3.6			--- python3.6版本目录
        │  │  pip_install.bat		--- tgw的wheel包安装脚本
        │  │  pip_uninstall.bat		--- tgw已安装python库卸载脚本
        │  │  pushdemo.bat		--- json接口推送示例脚本
        │  │  querydemo.bat		--- DataFrame或json接口同步方式查询示例脚本
        │  │  replaydemo.bat		--- DataFrame或json接口回放示例脚本
        │  │  run_demo.bat		--- 异步方式tgw_demo.py的执行脚本
        │  │  run_test36.bat		--- tgw_test.py的执行脚本
        │  │      
        │  └─etc			--- 配置文件
        │  │     test.json		--- tgw_test.py所需配置文件
        │  │      
        │  └─src
        │      ├─demo			--- 样例程序
        │      │      push_sample.py
        │      │      query_sample.py
        │      │      replay_sample.py
        │      │      tgw_demo.py
        │      │      
        │      └─test			--- 样例程序（用于数据落csv文件）
        │              data_writer.py
        │              tgw_commom.py
        │              tgw_output_file.py
        │              tgw_test.py
        │          
        └─python3.8			--- python3.8版本目录
            │  pip_install.bat		--- tgw的wheel包安装脚本
            │  pip_uninstall.bat		--- tgw已安装python库卸载脚本
            │  pushdemo.bat		--- json接口推送示例脚本
            │  querydemo.bat		--- DataFrame或json接口同步方式查询示例脚本
            │  replaydemo.bat		--- DataFrame或json接口回放示例脚本
            │  run_demo.bat		--- 异步方式tgw_demo.py的执行脚本
            │  run_test38.bat		--- tgw_test.py的执行脚本
            │      
            └─etc			--- 配置文件
            │      test.json		--- tgw_test.py所需配置文件
            │      
            └─src
                ├─demo			--- 样例程序
                │      push_sample.py
                │      query_sample.py
                │      replay_sample.py
                │      tgw_demo.py
                │      
                └─test			--- 样例程序（用于数据落csv文件）
                        data_writer.py
                        tgw_commom.py
                        tgw_output_file.py
                        tgw_test.py

2.运行系统环境
Redhat7.2、Redhat 7.4、Redhat 7.6、Win10

7.环境准备
1) 运行pip_uninstall.bat脚本
将前期安装的tgw包卸载

2) 运行pip_install.bat脚本
安装tgw-*.whl包

6.wheel 包安装
   1.直接在python3.8同一级目录下，运行tgw_install.sh脚本（windows系统脚本为tgw_install.bat）,再执行source ~/.bash_profile 命令(linux系统),该脚本会自动安装python3.8相关依赖动态库。
   2.进入python3.8目录，执行 pip_install.sh脚本安装wheel包，如果权限不够，请使用sudo执行脚本，出现pip3报错，设置pip3相关路径到PATH
 或者创建对应软连接或者自己手动 pip install安装即可

3.python版本使用
1) 进入到目录
cd python3.8

2) 运行push_sample.py，直接./pushdemo.sh(windows系统脚本为pushdemo.bat，需要修改必要的参数才能正确启动,参考demo程序中的注释说明)
3) 运行query_sample.py，直接./querydemo.sh(windows系统脚本为querydemo.bat，需要修改必要的参数才能正确启动,参考demo程序中的注释说明)
4) 运行replay_sample.py，直接./replaydemo.sh(windows系统脚本为replaydemo.bat，需要修改必要的参数才能正确启动,参考demo程序中的注释说明)
5) 运行tgw_demo.py，直接./run_demo.sh(windows系统脚本为run_demo.bat，需要修改必要的参数才能正确启动,参考demo程序中的注释说明)

6) 运行tgw_tets.py步骤：
   a) 修改参数(参考《中国银河证券格物金融服务平台(TGW)开发手册(Python版本).pdf》)
   b) 运行run_test.sh(windows系统脚本,windows系统脚本为run_test.bat)


