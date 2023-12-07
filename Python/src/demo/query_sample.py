import json
import tgw
import time
import pandas as pd
class MyLogSpi(tgw.ILogSpi):
    def __init__(self) -> None:
        super().__init__()
        pass
    def OnLog(self, level, log, len):
        print("TGW log: level: {}     log:   {}".format(level, log.strip('\n').strip('\r')))

    def OnLogon(self, data):
        print("TGW Logon information:  : ")
        print("api_mode : ", data.api_mode)
        print("logon json : ", data.logon_json)


def OnResponse(result, status):
    print(result)

def get_code_list(code_table_df):
    code_table_shsz_df = code_table_df[code_table_df['market_type'].isin([101, 102])]
    code_sh_list = list(code_table_shsz_df[code_table_shsz_df['security_type'].isin(['ASH', 'KSH'])]['security_code'])
    code_sz_list = list(code_table_shsz_df[code_table_shsz_df['security_type'].isin([ '1', '2', '3'])]['security_code'])
    return code_sh_list, code_sz_list



# 第一步：设置日志spi，保证有日志输出
log_spi = MyLogSpi()
tgw.SetLogSpi(log_spi)

# # 第二步，登录
cfg = tgw.Cfg()
cfg.server_vip = "127.0.0.1"
cfg.server_port = 8000
cfg.username = "****"  # 账号
cfg.password = "****"  # 密码
cfg.coloca_cfg.channel_mode = tgw.ColocatChannelMode.kTCP | tgw.ColocatChannelMode.kQTCP # tcp订阅通道和查询通道初始化
cfg.coloca_cfg.qtcp_channel_thread = 2
cfg.coloca_cfg.qtcp_max_req_cnt = 1000
cfg.coloca_cfg.enable_order_book = tgw.OrderBookType.kServerOrderBook
cfg.coloca_cfg.entry_size = 10
cfg.coloca_cfg.order_queue_size = 10
cfg.coloca_cfg.order_book_deliver_interval_microsecond = 10000
#success = tgw.Login(cfg, tgw.ApiMode.kColocationMode, './')#托管机房模式初始化，可指定证书文件地址
success = tgw.Login(cfg, tgw.ApiMode.kInternetMode, './') #互联网模式初始化，可指定证书文件地址
if not success:
    print("login fail")
    exit(0)
print("SDK version is :",tgw.GetVersion())
root = './'
return_DF = True

# 查询快照
req_tick = tgw.ReqDefault()
req_tick.market_type = tgw.MarketType.kSZSE
req_tick.date = 20230517
req_tick.begin_time = 90000000
req_tick.end_time = 170000000
req_tick.security_code = "000001"
# 异步方式 查询快照数据
# df , err = tgw.QuerySnapshot(req_tick, query_spi=OnResponse, return_df_format=return_DF)
# time.sleep(10)
# 同步方式 查询快照数据
df, error = tgw.QuerySnapshot(req_tick,return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'Snapshot.csv', encoding='gbk', index=False)
elif  df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root+'Snapshot.csv', encoding='gbk', index=False)
else:
    print("QuerySnapshot错误码：",error)

# 同步方式 查询逐笔委托
req_tick_order = tgw.ReqDefault()
req_tick_order.begin_time = 90000000
req_tick_order.date = 20230517
req_tick_order.end_time = 170000000
req_tick_order.security_code = "000001"
req_tick_order.market_type = tgw.MarketType.kSZSE
df, error = tgw.QueryTickOrder(req_tick_order,return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'TickOrder.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'TickOrder.csv', encoding='gbk', index=False)
else:
    print("QueryTickOrder错误码：",error)

# 同步方式 查询逐笔成交
req_tick_exec = tgw.ReqDefault()
req_tick_exec.begin_time = 90000000
req_tick_exec.date = 20230517
req_tick_exec.end_time = 170000000
req_tick_exec.security_code = "000001"
req_tick_exec.market_type = tgw.MarketType.kSZSE
df,error = tgw.QueryTickExecution(req_tick_exec,return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'TickExecution.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'TickExecution.csv', encoding='gbk', index=False)
else:
    print("QueryTickExecution错误码：",error)


# 同步方式 查询委托队列
req_tick_ordqueue = tgw.ReqDefault()
req_tick_ordqueue.begin_time = 90000000
req_tick_ordqueue.date = 20230517
req_tick_ordqueue.end_time = 170000000
req_tick_ordqueue.security_code = "000001"
req_tick_ordqueue.market_type = tgw.MarketType.kSZSE
df, error = tgw.QueryOrderQueue(req_tick_ordqueue,return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'OrderQueue.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'OrderQueue.csv', encoding='gbk', index=False)
else:
    print("QueryOrderQueue错误码：",error)


# 同步方式 k线查询
req_kline = tgw.ReqKline()
req_kline.security_code = "000001"
req_kline.market_type = tgw.MarketType.kSZSE
req_kline.cq_flag = 0
req_kline.auto_complete = 1
req_kline.cyc_type = tgw.MDDatatype.kDayKline
req_kline.begin_date = 20000517
req_kline.end_date = 20230906
req_kline.begin_time = 900
req_kline.end_time = 1700
df, error = tgw.QueryKline(req_kline,return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'Kline.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'Kline.csv', encoding='gbk', index=False)
else:
    print("QueryKline错误码：",error)

# 同步方式 三方资讯
taskid = tgw.GetTaskID()
tgw.SetThirdInfoParam(taskid,"function_id","A010060002")
tgw.SetThirdInfoParam(taskid,"market_code","000001.SZ")
tgw.SetThirdInfoParam(taskid,"start_date","20000101")
tgw.SetThirdInfoParam(taskid,"end_date","20231231")
# tgw.SetThirdInfoParam(taskid,"count","10000")
df, error = tgw.QueryThirdInfo(taskid,return_df_format=True)
if df is not None and return_DF == True:
    df.to_csv(root+'ThirdInfo.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'ThirdInfo.csv', encoding='gbk', index=False)
else:
    print("QueryThirdInfo错误码：",error)


# 同步方式 查询因子
req_factor = tgw.ReqFactorCfg()
req_factor.task_id = tgw.GetTaskID()
req_factor.factor_type = "SpecialFactor"
req_factor.factor_sub_type = "Default"
req_factor.factor_name = "market_match"
req_factor.begin_date = 20230828
req_factor.end_date = 20230828
req_factor.begin_time = 90000000
req_factor.end_time = 92000000
req_factor.security_code = "*"
req_factor.market = 0
req_factor.category = 0
req_factor.count = 5000
df, error = tgw.QueryFactor(req_factor)
if df is not None and len(df) > 0:
    headers_keys = set().union(*(d['headers'].keys() for d in df))
    body_keys = set()
    for d in df:
        body_dict = json.loads(d['body'])
        body_keys.update(body_dict.keys())
    dfout = pd.DataFrame([{**d['headers'], **json.loads(d['body'])} for d in df], columns=list(headers_keys.union(body_keys)))
    dfout.to_csv(root + 'Factor.csv', encoding='gbk', index=False)
else:
    print("QueryFactor错误码：",error)


# 同步方式 查询多个证券信息列表
item1 = tgw.SubCodeTableItem()
item1.market = tgw.MarketType.kSSE
item1.security_code = "600000"

item2 = tgw.SubCodeTableItem()
item2.market = tgw.MarketType.kSZSE
item2.security_code = "000001"
df, error = tgw.QuerySecuritiesInfo([item1,item2],return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'SecuritiesInfo.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'SecuritiesInfo.csv', encoding='gbk', index=False)
else:
    print("QuerySecuritiesInfo错误码：",error)


# 同步方式 查询当天全部证券信息列表
time.sleep(1)
itemAll = tgw.SubCodeTableItem()
itemAll.market = tgw.MarketType.kNone
itemAll.security_code = ""
df, error = tgw.QuerySecuritiesInfo([itemAll],return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'All_SecuritiesInfo.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'All_SecuritiesInfo.csv', encoding='gbk', index=False)
else:
    print("Query All SecuritiesInfo错误码：",error)


#-----------------------------如何获取代码表 START
# 同步方式 查询当日代码列表信息
df, error = tgw.QueryCodeTable(return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'CodeTable.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'CodeTable.csv', encoding='gbk', index=False)
else:
    print("QueryCodeTable错误码：",error)

# 同步方式 查询指定日期范围内的历史代码列表信息
taskid = tgw.GetTaskID()
tgw.SetThirdInfoParam(taskid, "function_id", 'A010010007')
tgw.SetThirdInfoParam(taskid, "start_date", '20230725')
tgw.SetThirdInfoParam(taskid, "end_date", '20230726')
df, error = tgw.QueryThirdInfo(taskid,return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'history_codelist.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'history_codelist.csv', encoding='gbk', index=False)
else:
    print(error)
#-----------------------------如何获取代码表 END


# 同步方式 查询ETF基础信息和成分股信息
security_cfg = tgw.SubCodeTableItem()
security_cfg.market = tgw.MarketType.kNone
security_cfg.security_code = "159506"
df,error = tgw.QueryETFInfo(security_cfg,return_df_format=return_DF)
if df is not None and return_DF == True:
    for j in df:
        j[0].to_csv(root+'ETFInfo'+security_cfg.security_code+'.csv', encoding='gbk', index=False)
        j[1].to_csv(root+'ETFConstitu'+security_cfg.security_code+'.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    for j in df:
        dfJsonETF = pd.DataFrame(j[0],index=[0])
        dfJsonETF.to_csv(root+'ETFInfo'+security_cfg.security_code+'.csv', encoding='gbk', index=False)
        dfJsonConsti = pd.DataFrame(j[1])
        dfJsonConsti.to_csv(root+'ETFConstitu'+security_cfg.security_code+'.csv', encoding='gbk', index=False)
else:
    print("QueryETFInfo错误码：",error)



# 同步方式 查询复权因子表
df, error = tgw.QueryExFactorTable('000001',return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'ExFactorTable.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'ExFactorTable.csv', encoding='gbk', index=False)
else:
    print("QueryExFactorTable错误码：",error)



# 期货如何查询夜盘数据(通过begin_time、end_time固定如下设置,可同时查询夜盘数据和日盘数据)
req_tick = tgw.ReqDefault()
req_tick.market_type = tgw.MarketType.kDCE
req_tick.date = 20230918
req_tick.begin_time = 200000000
req_tick.end_time = 195959000
req_tick.security_code = "c2311"
# 同步方式 查询快照数据
df, error = tgw.QuerySnapshot(req_tick,return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root+'Fut_DN_Snapshot.csv', encoding='gbk', index=False)
elif  df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root+'Fut_DN_Snapshot.csv', encoding='gbk', index=False)
else:
    print("QuerySnapshot_Fut_DN 错误码：",error)


# 查询港股快照
req_tick = tgw.ReqDefault()
req_tick.market_type = tgw.MarketType.kHKEx
req_tick.date = 20230517
req_tick.begin_time = 90000000
req_tick.end_time = 170000000
req_tick.security_code = "00001"
df, error = tgw.QuerySnapshot(req_tick, return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root + 'HK_Snapshot.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'HK_Snapshot.csv', encoding='gbk', index=False)
else:
    print("HK QuerySnapshot错误码：", error)

# 查询港股委托挂单
req_tick = tgw.ReqDefault()
req_tick.market_type = tgw.MarketType.kHKEx
req_tick.date = 20230517
req_tick.begin_time = 90000000
req_tick.end_time = 170000000
req_tick.security_code = "00001"
req_tick.data_type = 1
df, error = tgw.QuerySnapshot(req_tick, return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root + 'HK_Order.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'HK_Order.csv', encoding='gbk', index=False)
else:
    print("HK QueryOrder错误码：", error)


# 查询港股经纪席位
req_tick = tgw.ReqDefault()
req_tick.market_type = tgw.MarketType.kHKEx
req_tick.date = 20230517
req_tick.begin_time = 90000000
req_tick.end_time = 170000000
req_tick.security_code = "00001"
req_tick.data_type = 2
df, error = tgw.QuerySnapshot(req_tick, return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root + 'HK_Broker.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'HK_Broker.csv', encoding='gbk', index=False)
else:
    print("HK QueryBroker错误码：", error)

# 查询港股指数席位
req_tick = tgw.ReqDefault()
req_tick.market_type = tgw.MarketType.kHKEx
req_tick.date = 20230517
req_tick.begin_time = 90000000
req_tick.end_time = 170000000
req_tick.security_code = "CES100"
req_tick.data_type = 0
df, error = tgw.QuerySnapshot(req_tick, return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root + 'HK_Index.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'HK_Index.csv', encoding='gbk', index=False)
else:
    print("HK QueryIndexSnapshot错误码：", error)


# 同步方式 查询港股成交数据
req_tick_exec = tgw.ReqDefault()
req_tick_exec.begin_time = 90000000
req_tick_exec.date = 20230517
req_tick_exec.end_time = 170000000
req_tick_exec.security_code = "00001"
req_tick_exec.market_type = tgw.MarketType.kHKEx
df, error = tgw.QueryTickExecution(req_tick_exec, return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root + 'HK_TickExecution.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'HK_TickExecution.csv', encoding='gbk', index=False)
else:
    print("HK QueryTickExecution错误码：", error)


# 同步方式 港股k线查询
req_kline = tgw.ReqKline()
req_kline.security_code = "00001"
req_kline.market_type = tgw.MarketType.kHKEx
req_kline.cq_flag = 0
req_kline.auto_complete = 1
req_kline.cyc_type = tgw.MDDatatype.kDayKline
req_kline.begin_date = 20000517
req_kline.end_date = 20230906
req_kline.begin_time = 900
req_kline.end_time = 1700
df, error = tgw.QueryKline(req_kline, return_df_format=return_DF)
if df is not None and return_DF == True:
    df.to_csv(root + 'HK_Kline.csv', encoding='gbk', index=False)
elif df is not None and return_DF == False:
    dfJson = pd.DataFrame(df)
    dfJson.to_csv(root + 'HK_Kline.csv', encoding='gbk', index=False)
else:
    print("HK QueryKline错误码：", error)


#批量下载K线如何编码
# 1. 获取当天代码表
code_table_df, error = tgw.QueryCodeTable(return_df_format=True)
# 2. 按照沪深分组代码表
code_sh_list, code_sz_list = get_code_list(code_table_df)
# 3. 根据代码表批量下载K线
# 定义查询日K线的信息
req_kline = tgw.ReqKline()
req_kline.cq_flag = 0
req_kline.auto_complete = 1
req_kline.cyc_type = tgw.MDDatatype.k1KLine
req_kline.begin_date = 20230101
req_kline.end_date = 20230110
req_kline.begin_time = 930
req_kline.end_time = 1700
req_kline.market_type = tgw.MarketType.kSZSE
for code in code_sz_list[:2]:#此处仅演示两只证券下载K线
    req_kline.security_code = code
    df, error = tgw.QueryKline(req_kline, return_df_format=return_DF)
    if df is not None and return_DF == True:
        df.to_csv(root + '1MinKline_' + code + '.csv', encoding='gbk', index=False)
    elif df is not None and return_DF == False:
        dfJson = pd.DataFrame(df)
        dfJson.to_csv(root + '1MinKline_' + code + '.csv', encoding='gbk', index=False)
    else:
        print(f'{code} QueryKline error:{error}')


# 批量下载资讯数据示例
try:
    code_list = {'000001.SZ','600000.SH'}
    for onecode in code_list:
        taskid = tgw.GetTaskID()
        tgw.SetThirdInfoParam(taskid, "function_id", "A010050004")
        tgw.SetThirdInfoParam(taskid, "start_date", '19900101')
        tgw.SetThirdInfoParam(taskid, "end_date", '20991231')
        tgw.SetThirdInfoParam(taskid, "market_code", onecode)
        df, error = tgw.QueryThirdInfo(taskid,return_df_format=return_DF)
        if df is not None and return_DF == True:
            df.to_csv(root+'Balance_'+onecode+'.csv', encoding='gbk', index=False)
        elif df is not None and return_DF == False:
            dfJson = pd.DataFrame(df)
            dfJson.to_csv(root+'Balance_'+onecode+'.csv', encoding='gbk', index=False)
        else:
            print(f'{onecode} QueryThirdInfo A010050004 error:{error}')
except Exception as error:
    print("An error occurred:", type(error).__name__)

#释放相关资源
tgw.Close()


