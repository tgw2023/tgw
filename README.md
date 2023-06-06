# tgw<br>
[![Github workers](https://img.shields.io/github/watchers/tgw2023/tgw.svg?style=social&label=Watchers&)](https://github.com/tgw2023/tgw/watchers)
[![GitHub stars](https://img.shields.io/github/stars/tgw2023/tgw.svg?style=social&label=Star&)](https://github.com/tgw2023/tgw/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tgw2023/tgw.svg?style=social&label=Fork&)](https://github.com/tgw2023/tgw/fork)

# 1.简介
（1）中国银河证券格物机构金融服务平台提供集数据接入、推送、查询、计算和分析为一体的投研数据解决方案，为机构和高净值个人用户提供市场前沿、可靠、全面、极速的金融数据api服务。 	<br/>

（2）支持Python和C++两种编程语言 	<br/>

（3）支持Windows和linux两种操作系统 	<br/>

（4）支持的数据包括： 	<br/>
*   实时行情数据推送<br>
$\qquad$ K线数据（1/3/5/10/15/30/60/120分钟线/日/周/月/季年线）<br> 
$\qquad$ Level-1现货快照数据<br> 
$\qquad$ 指数快照数据<br> 
$\qquad$ 期权快照数据<br> 
$\qquad$ 期货快照数据<br> 
$\qquad$ 港股通快照数据<br> 
$\qquad$ 盘后定价交易快照数据<br> 
$\qquad$ 中证指数快照数据<br> 
$\qquad$ 深交所国证指数快照数据<br> 
$\qquad$ 港股通实时额度数据<br> 
$\qquad$ 港股通产品状态快照数据<br> 
$\qquad$ 港股市场波动调节机制(VCM)推送数据<br> 



*   历史行情数据查询<br>
$\qquad$ K线历史数据（日/周/月/季年线、1/3/5/10/15/30/60/120分钟线/日/周/月/季年线）<br> 
$\qquad$ Level-1快照历史数据<br> 

*   行情基本信息数据查询<br>
$\qquad$ 证券个股基本信息查询<br> 
$\qquad$ 证券代码表信息查询<br> 
$\qquad$ 复权因子表信息查询<br> 



*   股票基础信息<br>
$\qquad$ A股基本资料<br>
$\qquad$ A股行业分类<br>
$\qquad$ 公司简介<br>
$\qquad$ 股本结构<br>
$\qquad$ 公司主营业务<br>
$\qquad$ 历史股票列表<br>
*   发行与上市<br>
$\qquad$ A股首次公开发行<br>
$\qquad$ A股增发数据<br>
*   收益分配<br>
$\qquad$ A股股票分红<br>
$\qquad$ A股股票配股 <br>
*   股本与股东<br>
$\qquad$ A股十大股东名单<br>
$\qquad$ 限售股解禁明细 <br>
$\qquad$ 解禁数据 <br>
$\qquad$ 股权持股冻结/质押情况<br>
*   财务数据<br>
$\qquad$ A股资产负债表<br>
$\qquad$ A股利润表 <br>
$\qquad$ A股现金流表<br>
$\qquad$ A股财务指标<br>
*   日交易数据<br>
$\qquad$ 交易日历 <br>
$\qquad$ 个股资金流向<br>
*   交易异动统计<br>
$\qquad$ 大宗交易数据 <br>
$\qquad$ 交易异动营业部买卖信息 <br>
*   融资融券数据<br>
$\qquad$ 融资融券交易明细<br>
$\qquad$ 融资融券成交汇总 <br>
*   基金基本信息<br>
$\qquad$ 基金最新指标<br>
*   指数信息<br>
$\qquad$ A股指数成分股 <br>
*   资讯数据信息<br>
$\qquad$ 查询资讯数据更新日期<br>

*   公共参数表<br>
$\qquad$ 交易市场代码表<br>
$\qquad$ 证券类别代码表<br>
$\qquad$ 公司类型代码表<br>
$\qquad$ 股票增发进度代码表<br>
$\qquad$ 股票分红进度代码表<br>
$\qquad$ 股票配股进度代码表<br>
$\qquad$ 报表类型代码表<br>

# 2.Python 库安装
（1）使用pypi库安装<br> 
    pip install tgw<br> 
（2）使用wheel文件安装<br> 
    下载wheel文件后 pip install tgw-***.whl <br> 
 
# 3.Python api调用的主要代码demo
```python
# -*- coding: utf-8 -*-
from tgw import tgw
import time

def Init():
    cfg = tgw.Cfg()

    # 服务器地址配置
    cfg.server_vip = "10.4.**.**"
    cfg.server_port = 9**0
    # 用户登录账号配置
    cfg.username = "z***"  # 账号
    cfg.password = "zd******"  # 密码
    # 运行模式配置
    api_mode = tgw.ApiMode.kColocationMode # 设置api模式 托管机房模式
    # api_mode = tgw.ApiMode.kInternetMode  # 设置api模式 互联网模式
    if (api_mode == tgw.ApiMode.kColocationMode):
        cfg.coloca_cfg.channel_mode = tgw.ColocatChannelMode.kQTCP  # tcp查询模式
        cfg.coloca_cfg.qtcp_channel_thread = 2
        cfg.coloca_cfg.qtcp_max_req_cnt = 1000

    # 初始化返回错误码，完成登录验证、运行模式设置、传实例到订阅方法三个功能
    error_code = tgw.IGMDApi_Init(spi, cfg, api_mode)
    # 如初始化失败，退出流程
    if error_code != tgw.ErrorCode.kSuccess:
        print("Init TGW failed")
        tgw.IGMDApi_Release()
        exit(-1)

if __name__ == "__main__":
    # ---------订阅spi实例---------
    spi = IAMDSpiApp()

    # ---------查询spi实例---------
    # k线查询spi实例
    spi_kline = IQueryKlineSpi()
    # 快照查询spi实例
    spi_snap = IQuerySnapshotSpi()
    # 逐笔委托查询spi实例
    spi_tick_order = IQueryTickOrderSpi()
    # 逐笔成交spi实例
    spi_tick_exec = IQueryTickExecutionSpi()
    # 委托队列spi实例
    spi_order_queue = IQueryOrderQueueSpi()
    # 代码表查询spi实例
    spi_code_table = IQueryCodeTableSpi()
    # 证券代码信息查询spi实例
    spi_secur_info = IQuerySecuritiesInfoSpi()
    # 复权因子表信息查询spi实例
    spi_ex_factor = IQueryExFactorSpi()
    # 加工因子查询spi实例
    spi_factor = IQueryFactorSpi()
    # 资讯数据查询spi实例
    spi_third_info = IQueryThirdInfoSpi()

    # ---------回放spi实例---------
    spi_replay = IReplayApp()

    Init()

    time.sleep(2)
    # 修改密码
    HandleUpdatePassword()
    # 订阅接口
    DealSub()
    # 查询接口
    DealQuery()
    # 回放接口
    DealReplay()
```
# 4.权限开通
（1）试用权限开通，可登录官网自助注册<br/>
   官网： http://www.chinastock.com.cn/newsite/cgs-services/strategyTrade/geWuInstitution.html <br/>
   流程如下：<br/>
                       ![](https://github.com/tgw2023/tgw/blob/main/picture/%E8%AF%95%E7%94%A8%E8%B4%A6%E6%88%B7%E5%BC%80%E9%80%9A%E6%B5%81%E7%A8%8B%20.jpg) <br> 
（2）正式权限开通请咨询中国银河证券营业部<br/>
# 5.联系方式
（1）格物官方联系企业微信：<br/>
             ![](https://github.com/tgw2023/tgw/blob/main/picture/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%B4%BB%E7%A0%81.png) <br> 
（2）格物官方联系联系邮箱：<br/>
     yhgwjgszhtyfw@chinastock.com.cn<br/>
