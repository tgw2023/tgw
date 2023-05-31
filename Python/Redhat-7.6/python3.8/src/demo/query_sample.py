import tgw
import csv
import time
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
success = tgw.Login(cfg, tgw.ApiMode.kColocationMode, './')#托管机房模式初始化，可指定证书文件地址
# success = tgw.Login(cfg, tgw.ApiMode.kInternetMode, './') #互联网模式初始化，可指定证书文件地址
if not success:
    print("login fail")
    exit(0)

root = './'
return_DF = False

# 查询快照
req_tick = tgw.ReqDefault()
req_tick.market_type = tgw.MarketType.kSZSE
req_tick.date = 20230517
req_tick.begin_time = 93000000
req_tick.end_time = 170000000
req_tick.security_code = "000001"
# 异步方式 查询快照数据
# df , err = tgw.QuerySnapshot(req_tick, query_spi=OnResponse, return_df_format=True)
# time.sleep(10)
# 同步方式 查询快照数据
df, error = tgw.QuerySnapshot(req_tick,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'Snapshot.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'Snapshot.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)

# 同步方式 查询逐笔委托
req_tick_order = tgw.ReqDefault()
req_tick_order.begin_time = 93000000
req_tick_order.date = 20230517
req_tick_order.end_time = 170000000
req_tick_order.security_code = "000001"
req_tick_order.market_type = tgw.MarketType.kSZSE
df, error = tgw.QueryTickOrder(req_tick_order,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'TickOrder.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'TickOrder.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)

# 同步方式 查询逐笔成交
req_tick_exec = tgw.ReqDefault()
req_tick_exec.begin_time = 93000000
req_tick_exec.date = 20230517
req_tick_exec.end_time = 170000000
req_tick_exec.security_code = "000001"
req_tick_exec.market_type = tgw.MarketType.kSZSE
df,error = tgw.QueryTickExecution(req_tick_exec,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'TickExecution.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'TickExecution.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)

# 同步方式 查询委托队列
req_tick_ordqueue = tgw.ReqDefault()
req_tick_ordqueue.begin_time = 93000000
req_tick_ordqueue.date = 20230517
req_tick_ordqueue.end_time = 170000000
req_tick_ordqueue.security_code = "000001"
req_tick_ordqueue.market_type = tgw.MarketType.kSZSE
df, error = tgw.QueryOrderQueue(req_tick_ordqueue,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'OrderQueue.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'OrderQueue.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)


# 同步方式 k线查询
req_kline = tgw.ReqKline()
req_kline.security_code = "000001"
req_kline.market_type = tgw.MarketType.kSZSE
req_kline.cq_flag = 0
req_kline.auto_complete = 1
req_kline.cyc_type = tgw.MDDatatype.k1KLine
req_kline.begin_date = 20230517
req_kline.end_date = 20230517
req_kline.begin_time = 930
req_kline.end_time = 1700
df, error = tgw.QueryKline(req_kline,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'Kline.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'Kline.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)

# 同步方式 三方资讯
taskid = tgw.GetTaskID()
tgw.SetThirdInfoParam(taskid,"function_id","A010060002")
tgw.SetThirdInfoParam(taskid,"market_code","000001.SZ")
tgw.SetThirdInfoParam(taskid,"start_date","20221101")
tgw.SetThirdInfoParam(taskid,"end_date","20221129")
df, error = tgw.QueryThirdInfo(taskid,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'ThirdInfo.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'ThirdInfo.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)


# 同步方式 查询因子
req_factor = tgw.ReqFactor()
req_factor.task_id = tgw.GetTaskID()
req_factor.factor_type = "SpecialFactor"
req_factor.factor_sub_type = "Default"
req_factor.factor_name = "market_match"
req_factor.begin_date = 20230412
req_factor.end_date = 20230412
req_factor.begin_time = 93000000
req_factor.end_time = 103000000
req_factor.security_code = "*"
req_factor.market = 0
req_factor.category = 0
req_factor.offset = 0
req_factor.count = 100
df, error = tgw.QueryFactor(req_factor)
if len(error) == 0:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'Factor.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)


# 同步方式 查询证券信息列表
req_items = tgw.Tools_CreateSubCodeTableItem(2) #获取两个请求结构的空间
item1 = tgw.SubCodeTableItem()
item1.market = tgw.MarketType.kSZSE
item1.security_code = "000001"
tgw.Tools_SetSubCodeTableItem(req_items, 0, item1) #为第一个结构赋值
item2 = tgw.SubCodeTableItem()
item2.market = tgw.MarketType.kSSE
item2.security_code = "600000"
tgw.Tools_SetSubCodeTableItem(req_items, 1, item2) #为第二个结构赋值
df, error = tgw.QuerySecuritiesInfo(req_items,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'SecuritiesInfo.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'SecuritiesInfo.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)

# 同步方式 查询代码列表信息
df, error = tgw.QueryCodeTable(return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'CodeTable.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'CodeTable.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)

# 同步方式 查询ETF基础信息和成分股信息
security_cfg = tgw.SubCodeTableItem()
security_cfg.market = tgw.MarketType.kNone
security_cfg.security_code = "510050"
df,error = tgw.QueryETFInfo(security_cfg,return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    for j in df:
        j[0].to_csv(root+'ETFInfo'+j[0].loc[0,'security_code']+'.csv', index=False)
        j[1].to_csv(root+'ETFConstitu'+j[0].loc[0,'security_code']+'.csv', index=False)
elif len(error) == 0 and return_DF == False:
    for j in df:
        file = open(root+'ETFInfo'+j[0]['security_code']+'.csv', 'a', encoding='utf-8', newline='')
        csvWriter = csv.DictWriter(file, fieldnames=list(j[0].keys()))
        csvWriter.writeheader()
        csvWriter.writerow(j[0])
        file.close()
        lineNum=0
        for consti in j[1]:
            if lineNum == 0:
                file = open(root+'ETFConstitu'+j[0]['security_code']+'.csv', 'a', encoding='utf-8', newline='')
                csvWriter = csv.DictWriter(file, fieldnames=list(consti.keys()))
                csvWriter.writeheader()
            csvWriter.writerow(consti)
            lineNum += 1
        file.close()
else:
    print(error)

# 同步方式 查询复权因子表
df, error = tgw.QueryExFactorTable('000001',return_df_format=return_DF)
if len(error) == 0 and return_DF == True:
    df.to_csv(root+'ExFactorTable.csv', index=False)
elif len(error) == 0 and return_DF == False:
    lineNum = 0
    for j in df:
        if lineNum == 0:
            file = open(root + 'ExFactorTable.csv', 'a', encoding='utf-8', newline='')
            csvWriter = csv.DictWriter(file, fieldnames=list(j.keys()))
            csvWriter.writeheader()
        csvWriter.writerow(j)
        lineNum += 1
    file.close()
else:
    print(error)

time.sleep(20)
time.sleep(60)
#释放相关资源
tgw.Close()


