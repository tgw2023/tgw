# -*- coding: utf-8 -*-
from tgw import tgw
import time
import signal


# 订阅spi
class IAMDSpiApp(tgw.IGMDSpi):
    def OnLog(self, level, log, len):
        print("TGW log: ", "level: ", level, end='')
        print("     log:   ", log)

    def OnLogon(self, data):
        print("TGW Logon information:  : ")
        print("api_mode : ", data.api_mode)
        print("logon json : ", data.logon_json)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDSnapshot(self, data, cnt):
        print("Receive MDSnapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))

        # print(tgw.Tools_GetInt64DataByIndex(data.bid_price, 0)) #取出委托档位买一档价格(最多十档)
        # print(tgw.Tools_GetInt64DataByIndex(data.bid_volume, 0)) #取出委托档位买一档的委托量(最多十档)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDIndexSnapshot(self, data, cnt):
        print("Receive MDIndexSnapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnMDOptionSnapshot(self, data, cnt):
        print("Receive MDOptionSnapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
            # print(tgw.Tools_GetInt64DataByIndex(data.bid_price, 0)) #取出委托档位买一档价格(最多五档)
            # print(tgw.Tools_GetInt64DataByIndex(data.bid_volume, 0)) #取出委托档位买一档的委托量(最多五档)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTSnapshot(self, data, cnt):
        print("Receive MDHKTSnapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
            # print(tgw.Tools_GetInt64DataByIndex(data.bid_price, 0)) #取出委托档位买一档价格(最多五档)
            # print(tgw.Tools_GetInt64DataByIndex(data.bid_volume, 0)) #取出委托档位买一档的委托量(最多五档)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDAfterHourFixedPriceSnapshot(self, data, cnt):
        print("Receive MDAfterHourFixedPriceSnapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnMDCSIIndexSnapshot(self, data, cnt):
        print("Receive MDCSIIndexSnapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnMDCnIndexSnapshot(self, data, cnt):
        print("Receive MDCnIndexSnapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTRealtimeLimit(self, data, cnt):
        print("Receive MDHKTRealtimeLimit Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTProductStatus(self, data, cnt):
        print("Receive MDHKTProductStatus Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTVCM(self, data, cnt):
        print("Receive MDHKTVCM Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnMDFutureSnapshot(self, data, cnt):
        print("Receive MDHKTVCM Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(data, i)))
        tgw.IGMDApi_FreeMemory(data)

    def OnKLine(self, kline, cnt, kline_type):
        print("Receive KLine Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(kline, i)))
        tgw.IGMDApi_FreeMemory(kline)

    def OnSnapshotDerive(self, snapshot_derive, cnt):
        print("Receive MDSnapshotDerive Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(snapshot_derive, i)))
        tgw.IGMDApi_FreeMemory(snapshot_derive)

    def OnFactor(self, factor):
        print("Receive Factor Info: ")
        print(" json_buf is: ", factor.json_buf)
        print(" data_size is: ", factor.data_size)
        tgw.IGMDApi_FreeMemory(factor)


# 回放spi
class IReplayApp(tgw.IGMDHistorySpi):
    def OnMDSnapshot(self, task_id, snapshots, cnt):
        print("Receive stock snapshot Info: ")
        tgw.Tools_WriteReplaySnapshot(snapshots, cnt)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDTickExecution(self, task_id, ticks, cnt):
        print("Receive MDTickExecution Info: ")
        tgw.Tools_WriteReplayTickExecution(ticks, cnt)
        tgw.IGMDApi_FreeMemory(ticks)

    def OnMDKline(self, task_id, klines, cnt, kline_type):
        print("Receive OnMDKline Info: ")
        tgw.Tools_WriteReplayKline(klines, cnt, kline_type)
        tgw.IGMDApi_FreeMemory(klines)

    def OnRspTaskStatus(self, task_id, task_status):
        print("task_id is: ", task_status.task_id)
        print("status is: ", task_status.status)
        print("error_code is: ", task_status.error_code)


# 快照查询spi
class IQuerySnapshotSpi(tgw.IGMDSnapshotSpi):
    def OnMDSnapshotL1(self, snapshots, cnt):
        print("Receive stock snapshot l1 Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(snapshots, i)))
            # print(tgw.Tools_GetInt64DataByIndex(snapshots.bid_price, 0)) #取出委托档位买一档价格(最多五档)
            # print(tgw.Tools_GetInt64DataByIndex(snapshots.bid_volume, 0)) #取出委托档位买一档的委托量(最多五档)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDSnapshotL2(self, snapshots, cnt):
        print("Receive stock snapshot l2 Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(snapshots, i)))
            # print(tgw.Tools_GetInt64DataByIndex(snapshots.bid_price, 0)) #取出委托档位买一档价格(最多十档)
            # print(tgw.Tools_GetInt64DataByIndex(snapshots.bid_volume, 0)) #取出委托档位买一档的委托量(最多十档)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDIndexSnapshot(self, index_snapshots, cnt):
        print("Receive index snapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(index_snapshots, i)))
        tgw.IGMDApi_FreeMemory(index_snapshots)

    def OnMDHKTSnapshot(self, hk_snapshots, cnt):
        print("Receive hk snapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(hk_snapshots, i)))
            # print(tgw.Tools_GetInt64DataByIndex(hk_snapshots.bid_price, 0)) #取出委托档位买一档价格(最多五档)
            # print(tgw.Tools_GetInt64DataByIndex(hk_snapshots.bid_volume, 0)) #取出委托档位买一档的委托量(最多五档)
        tgw.IGMDApi_FreeMemory(hk_snapshots)

    def OnMDOptionSnapshot(self, opt_snapshots, cnt):
        print("Receive option snapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(opt_snapshots, i)))
            # print(tgw.Tools_GetInt64DataByIndex(opt_snapshots.bid_price, 0)) #取出委托档位买一档价格(最多五档)
            # print(tgw.Tools_GetInt64DataByIndex(opt_snapshots.bid_volume, 0)) #取出委托档位买一档的委托量(最多五档)
        tgw.IGMDApi_FreeMemory(opt_snapshots)

    def OnMDFutureSnapshot(self, future_ticks, cnt):
        print("Receive future snapshot Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(future_ticks, i)))
            # print(tgw.Tools_GetInt64DataByIndex(future_ticks.bid_price, 0)) #取出委托档位买一档价格(最多五档)
            # print(tgw.Tools_GetInt64DataByIndex(future_ticks.bid_volume, 0)) #取出委托档位买一档的委托量(最多五档)
        tgw.IGMDApi_FreeMemory(future_ticks)

    def OnStatus(self, status):
        print("Receive QuerySnapshotSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  req_type  =  ", status.rsp_union_status.req_type)
        print("  security_code  =  ", status.rsp_union_status.security_code)
        print("  market_type  =  ", status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)


# 逐笔委托查询spi
class IQueryTickOrderSpi(tgw.IGMDTickOrderSpi):
    def OnMDTickOrder(self, tick_orders, cnt):
        print("Receive QueryTickOrderSpi Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(tick_orders, i)))
        tgw.IGMDApi_FreeMemory(tick_orders)

    def OnStatus(self, status):
        print("Receive QueryTickOrderSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  req_type  =  ", status.rsp_union_status.req_type)
        print("  security_code  =  ", status.rsp_union_status.security_code)
        print("  market_type  =  ", status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)


# 逐笔成交spi
class IQueryTickExecutionSpi(tgw.IGMDTickExecutionSpi):
    def OnMDTickExecution(self, tick_execs, cnt):
        print("Receive QueryTickExecutionSpi Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(tick_execs, i)))
        tgw.IGMDApi_FreeMemory(tick_execs)

    def OnStatus(self, status):
        print("Receive QueryTickExecutionSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  req_type  =  ", status.rsp_union_status.req_type)
        print("  security_code  =  ", status.rsp_union_status.security_code)
        print("  market_type  =  ", status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)


# 委托队列spi
class IQueryOrderQueueSpi(tgw.IGMDOrderQueueSpi):
    def OnMDOrderQueue(self, order_queues, cnt):
        print("Receive QueryOrderQueueSpi Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(order_queues, i)))
            # print(tgw.Tools_GetInt64DataByIndex(data.volume, 0)) #取出订单明细一档(最多五十档)
        tgw.IGMDApi_FreeMemory(order_queues)

    def OnStatus(self, status):
        print("Receive QueryOrderQueueSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  req_type  =  ", status.rsp_union_status.req_type)
        print("  security_code  =  ", status.rsp_union_status.security_code)
        print("  market_type  =  ", status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)


# k线查询spi
class IQueryKlineSpi(tgw.IGMDKlineSpi):
    def OnMDKLine(self, klines, cnt, kline_type):
        print("Receive QueryKlineSpi Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(klines, i)))

        tgw.IGMDApi_FreeMemory(klines)

    def OnStatus(self, status):
        print("Receive QueryKlineSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  req_type  =  ", status.rsp_union_status.req_type)
        print("  security_code  =  ", status.rsp_union_status.security_code)
        print("  market_type  =  ", status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)


# 代码表查询spi
class IQueryCodeTableSpi(tgw.IGMDCodeTableSpi):
    def OnMDCodeTable(self, code_tables, cnt):
        print("Receive QueryCodeTableSpi Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(code_tables, i)))
        tgw.IGMDApi_FreeMemory(code_tables)

    def OnStatus(self, status):
        print("Receive QueryCodeTableSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  req_type  =  ", status.rsp_union_status.req_type)
        print("  security_code  =  ", status.rsp_union_status.security_code)
        print("  market_type  =  ", status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)


# 证券代码信息查询spi
class IQuerySecuritiesInfoSpi(tgw.IGMDSecuritiesInfoSpi):
    def OnMDSecuritiesInfo(self, code_tables, cnt):
        print("Receive QuerySecuritiesInfoSpi Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(code_tables, i)))
        tgw.IGMDApi_FreeMemory(code_tables)

    def OnStatus(self, status):
        print("Receive QuerySecuritiesInfoSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)

        for i in range(status.rsp_stockinfo_status.code_table_item_cnt):
            item = tgw.Tools_GetSubCodeTableItemByIndex(status.rsp_stockinfo_status.codes, i)
            print("  security_code  =  ", item.security_code)
            print("  market_type  =  ", item.market)
        tgw.IGMDApi_FreeMemory(status)


# 复权因子表信息查询spi
class IQueryExFactorSpi(tgw.IGMDExFactorSpi):
    def OnMDExFactor(self, ex_factor_tables, cnt):
        print("Receive QueryExFactorSpi Info: ")
        # 序列化输出数据
        for i in range(cnt):
            print(tgw.Tools_Serialize(tgw.Tools_GetDataByIndex(ex_factor_tables, i)))
        tgw.IGMDApi_FreeMemory(ex_factor_tables)

    def OnStatus(self, status):
        print("Receive QueryExFactorSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  req_type  =  ", status.rsp_union_status.req_type)
        print("  security_code  =  ", status.rsp_union_status.security_code)
        print("  market_type  =  ", status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)


# 加工因子查询spi
class IQueryFactorSpi(tgw.IGMDFactorSpi):
    def OnFactor(self, factors, cnt):
        print("Receive QueryFactorSpi Info: ")
        for i in range(cnt):
            data = tgw.Tools_GetDataByIndex(factors, i)
            print(" json_buf is: ", data.json_buf)
            print(" data_size is: ", data.data_size)
        tgw.Tools_FreeMemory(factors, cnt)  # 这里的查询因子释放必须使用这个接口，否则会内存泄露

    def OnStatus(self, status):
        print("Receive QueryFactorSpi Status : ")
        print("  factor_type  =  ", status.rsp_factor_status.factor_type)
        print("  factor_sub_type  =  ", status.rsp_factor_status.factor_sub_type)
        print("  factor_name  =  ", status.rsp_factor_status.factor_name)
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        tgw.IGMDApi_FreeMemory(status)


# 资讯数据查询spi
class IQueryThirdInfoSpi(tgw.IGMDThirdInfoSpi):
    def OnThirdInfo(self, data, cnt):
        print("Receive QueryThirdInfoSpi Info: ")
        for i in range(cnt):
            print(" task_id is: ", data.task_id)
            print(" data_size is: ", data.data_size)
            print(" json_data is: ", data.json_data)
        tgw.IGMDApi_FreeMemory(data)

    def OnStatus(self, status):
        print("Receive QueryThirdInfoSpi Status : ")
        print("  error_code  =  ", status.error_code)
        print("  error_msg_len  =  ", status.error_msg_len)
        print("  error_msg  =  ", status.error_msg)
        print("  task_id  =  ", status.rsp_thirdinfo_status.task_id)
        tgw.IGMDApi_FreeMemory(status)


def GetMarkert(m):
    if m == "All":
        return tgw.MarketType.kNone
    elif m == "sz":
        return tgw.MarketType.kSZSE
    elif m == "sh":
        return tgw.MarketType.kSSE
    elif m == "shfe":
        return tgw.MarketType.kSHFE
    elif m == "cffex":
        return tgw.MarketType.kCFFEX
    elif m == "dce":
        return tgw.MarketType.kDCE
    elif m == "czce":
        return tgw.MarketType.kCZCE
    elif m == "ine":
        return tgw.MarketType.kINE
    elif m == "neeq":
        return tgw.MarketType.kNEEQ
    elif m == "bk":
        return tgw.MarketType.kBK


def GetCategory(m):
    if m == "All":
        return tgw.VarietyCategory.kNone
    elif m == "Stock":
        return tgw.VarietyCategory.kStock
    elif m == "Fund":
        return tgw.VarietyCategory.kFund
    elif m == "Bond":
        return tgw.VarietyCategory.kBond
    elif m == "Option":
        return tgw.VarietyCategory.kOption
    elif m == "Index":
        return tgw.VarietyCategory.kIndex
    elif m == "HKT":
        return tgw.VarietyCategory.kHKT
    elif m == "FutureOption":
        return tgw.VarietyCategory.kFutureOption
    elif m == "CFETSRMB":
        return tgw.VarietyCategory.kCFETSRMB
    elif m == "HKEx":
        return tgw.VarietyCategory.kHKEx
    elif m == "Others":
        return tgw.VarietyCategory.kOthers


def GetSubType(m):
    if m == "All":
        return tgw.SubscribeDataType.kNone
    elif m == "MD1MinKline":
        return tgw.SubscribeDataType.k1MinKline
    elif m == "MD3MinKline":
        return tgw.SubscribeDataType.k3MinKline
    elif m == "MD5MinKline":
        return tgw.SubscribeDataType.k5MinKline
    elif m == "MD10MinKline":
        return tgw.SubscribeDataType.k10MinKline
    elif m == "MD15MinKline":
        return tgw.SubscribeDataType.k15MinKline
    elif m == "MD30MinKline":
        return tgw.SubscribeDataType.k30MinKline
    elif m == "MD60MinKline":
        return tgw.SubscribeDataType.k60MinKline
    elif m == "MD120MinKline":
        return tgw.SubscribeDataType.k120MinKline
    elif m == "MDSnapshotDerive":
        return tgw.SubscribeDataType.kSnapshotDerive
    elif m == "MDSnapshot":
        return tgw.SubscribeDataType.kSnapshot
    elif m == "MDIndexSnapshot":
        return tgw.SubscribeDataType.kIndexSnapshot
    elif m == "MDOptionSnapshot":
        return tgw.SubscribeDataType.kOptionSnapshot
    elif m == "MDHKTSnapshot":
        return tgw.SubscribeDataType.kHKTSnapshot
    elif m == "MDAfterHourFixedPriceSnapshot":
        return tgw.SubscribeDataType.kAfterHourFixedPriceSnapshot
    elif m == "MDCSIIndexSnapshot":
        return tgw.SubscribeDataType.kCSIIndexSnapshot
    elif m == "MDCnIndexSnapshot":
        return tgw.SubscribeDataType.kCnIndexSnapshot
    elif m == "MDHKTRealtimeLimit":
        return tgw.SubscribeDataType.kHKTRealtimeLimit
    elif m == "MDHKTProductStatus":
        return tgw.SubscribeDataType.kHKTProductStatus
    elif m == "MDHKTVCM":
        return tgw.SubscribeDataType.kHKTVCM
    elif m == "MDFutureSnapshot":
        return tgw.SubscribeDataType.kFutureSnapshot


def GetCqFlag(f):
    if f == "1f":
        return 1
    elif f == "0f":
        return 0
    elif f == "2f":
        return 2
    else:
        return 0


def GetKlineType(f):
    if f == "1m":
        return tgw.MDDatatype.k1KLine
    elif f == "3m":
        return tgw.MDDatatype.k3KLine
    elif f == "5m":
        return tgw.MDDatatype.k5KLine
    elif f == "10m":
        return tgw.MDDatatype.k10KLine
    elif f == "15m":
        return tgw.MDDatatype.k15KLine
    elif f == "30m":
        return tgw.MDDatatype.k30KLine
    elif f == "60m":
        return tgw.MDDatatype.k60KLine
    elif f == "120m":
        return tgw.MDDatatype.k120KLine
    elif f == "1d":
        return tgw.MDDatatype.kDayKline
    elif f == "1w":
        return tgw.MDDatatype.kWeekKline
    elif f == "1M":
        return tgw.MDDatatype.kMonthKline
    elif f == "1s":
        return tgw.MDDatatype.kSeasonKline
    elif f == "1y":
        return tgw.MDDatatype.kYearKline


def HandleUpdatePassword():
    # 更新密码
    up_password_req = tgw.UpdatePassWordReq()
    up_password_req.username = "amd"
    up_password_req.old_password = "123456"
    up_password_req.new_password = "123"
    ec = tgw.IGMDApi_UpdatePassWord(up_password_req)
    if ec != tgw.ErrorCode.kSuccess:
        print("UpdatePassWord failed, error code is : ", ec)
    else:
        print("UpdatePassWord success")


def DealSub():
    sub_item = tgw.SubscribeItem()
    sub_item.market = GetMarkert("All")
    sub_item.flag = GetSubType("All")
    sub_item.category_type = GetCategory("All")
    sub_item.security_code = "000001"
    tgw.IGMDApi_Subscribe(sub_item, 1)  # 订阅全市场，全类型，全品种，全代码

    sub_factor_item = tgw.SubFactorItem()
    sub_factor_item.factor_type = "all"
    sub_factor_item.factor_sub_type = "all"
    sub_factor_item.factor_name = "all"

    tgw.IGMDApi_SubFactor(sub_factor_item, 1)


def DealQuery():
    # 查询k线
    req_kline = tgw.ReqKline()
    req_kline.security_code = "000001"
    req_kline.market_type = GetMarkert("sz")
    req_kline.cq_flag = 0
    req_kline.auto_complete = 1
    req_kline.cyc_type = GetKlineType("1m")
    req_kline.begin_date = 20230128
    req_kline.end_date = 20230308
    req_kline.begin_time = 930
    req_kline.end_time = 1700
    tgw.IGMDApi_QueryKline(spi_kline, req_kline)

    # 查询快照
    req_tick = tgw.ReqDefault()
    req_tick.market_type = GetMarkert("sz")
    req_tick.date = 20210611
    req_tick.begin_time = 93000000
    req_tick.end_time = 170000000
    req_tick.security_code = "000001"
    tgw.IGMDApi_QuerySnapshot(spi_snap, req_tick)

    # 查询逐笔委托
    req_tick_order = tgw.ReqDefault()
    req_tick_order.begin_time = 93000000
    req_tick_order.date = 20210611
    req_tick_order.end_time = 170000000
    req_tick_order.security_code = "000001"
    req_tick_order.market_type = GetMarkert("sz")
    tgw.IGMDApi_QueryTickOrder(spi_tick_order, req_tick_order)

    # 查询逐笔成交
    req_tick_execution = tgw.ReqDefault()
    req_tick_execution.begin_time = 93000000
    req_tick_execution.date = 20210611
    req_tick_execution.end_time = 170000000
    req_tick_execution.security_code = "000001"
    req_tick_execution.market_type = GetMarkert("sz")
    tgw.IGMDApi_QueryTickExecution(spi_tick_exec, req_tick_execution)

    # 查询委托队列
    req_order_queue = tgw.ReqDefault()
    req_order_queue.begin_time = 93000000
    req_order_queue.date = 20210611
    req_order_queue.end_time = 170000000
    req_order_queue.security_code = "000001"
    req_order_queue.market_type = GetMarkert("sz")
    tgw.IGMDApi_QueryOrderQueue(spi_order_queue, req_order_queue)

    # 查询代码表
    tgw.IGMDApi_QueryCodeTable(spi_code_table)

    # 查询证券代码信息
    item = tgw.SubCodeTableItem()
    item.market = GetMarkert("sz")
    item.security_code = "000001"
    tgw.IGMDApi_QuerySecuritiesInfo(spi_secur_info, item, 1)

    # 查询复权因子信息表
    tgw.IGMDApi_QueryExFactorTable(spi_ex_factor, "000001")

    # 查询因子
    req_factor = tgw.ReqFactor()
    req_factor.factor_type = "A"
    req_factor.factor_sub_type = "B"
    req_factor.factor_name = "C"
    req_factor.begin_date = 20210611
    req_factor.end_date = 20210611
    req_factor.begin_time = 93000000
    req_factor.end_time = 170000000
    tgw.IGMDApi_QueryFactor(spi_factor, req_factor)

    # 查询三方咨询
    task_id = tgw.IGMDApi_GetTaskID()
    tgw.IGMDApi_SetThirdInfoParam(task_id, "function_id", "01")
    tgw.IGMDApi_SetThirdInfoParam(task_id, "WD_CODE", "0000001")
    tgw.IGMDApi_QueryThirdInfo(spi_third_info, task_id)


def DealReplay():
    # 回放逐笔成交
    history_item1 = tgw.ReqHistoryItem()
    history_item1.market = tgw.MarketType.kSZSE
    history_item1.security_code = "000001"

    history_item11 = tgw.ReqHistoryItem()
    history_item11.market = tgw.MarketType.kSZSE
    history_item11.security_code = "000002"

    req_replay = tgw.ReqReplay()
    req_replay.begin_date = 20211228
    req_replay.end_date = 20211228
    req_replay.begin_time = 91500000
    req_replay.end_time = 103100000
    req_replay.task_id = tgw.IGMDApi_GetTaskID()
    # 回放两只代码
    req_replay.req_item_cnt = 2
    req_replay.req_items = tgw.Tools_CreateReqHistoryItem(2)
    tgw.Tools_SetReqHistoryItem(req_replay.req_items, 0, history_item1)
    tgw.Tools_SetReqHistoryItem(req_replay.req_items, 1, history_item11)

    req_replay.md_data_type = tgw.MDDatatype.kTickExecution
    tgw.IGMDApi_ReplayRequest(spi_replay, req_replay)

    # 回放快照
    history_item2 = tgw.ReqHistoryItem()
    history_item2.market = tgw.MarketType.kSZSE
    history_item2.security_code = "000001"

    req_replay2 = tgw.ReqReplay()
    req_replay2.begin_date = 20211228
    req_replay2.end_date = 20211228
    req_replay2.begin_time = 91500000
    req_replay2.end_time = 103100000
    req_replay2.task_id = tgw.IGMDApi_GetTaskID()
    req_replay2.req_item_cnt = 1
    req_replay2.req_items = history_item2
    req_replay2.md_data_type = tgw.MDDatatype.kSnapshot
    tgw.IGMDApi_ReplayRequest(spi_replay, req_replay2)

    # 回放k线
    history_item3 = tgw.ReqHistoryItem()
    history_item3.market = tgw.MarketType.kSZSE
    history_item3.security_code = "000001"

    req_k = tgw.ReqReplayKline()
    req_k.begin_date = 20211228
    req_k.begin_time = 930
    req_k.cq_flag = 0
    req_k.cyc_type = 1
    req_k.auto_complete = 1
    req_k.end_date = 20211228
    req_k.end_time = 1032
    req_k.task_id = tgw.IGMDApi_GetTaskID()
    req_k.req_item_cnt = 1
    req_k.req_items = history_item3
    tgw.IGMDApi_ReplayKline(spi_replay, req_k)


def GetChannelMode(mode):
    ret_mode = 0
    if mode == "QTCP":
        ret_mode = ret_mode | tgw.ColocatChannelMode.kQTCP
    elif mode == "TCP":
        ret_mode = ret_mode | tgw.ColocatChannelMode.kTCP
    elif mode == "RTCP":
        ret_mode = ret_mode | tgw.ColocatChannelMode.kRTCP
    return ret_mode


def Init():
    cfg = tgw.Cfg()

    # 服务器地址配置
    cfg.server_vip = "127.0.0.1"
    cfg.server_port = 8000
    # 用户登录账号配置
    cfg.username = "*****"  # 账号
    cfg.password = "*****"  # 密码
    # 运行模式配置
    # api_mode = tgw.ApiMode.kColocationMode # 设置api模式 托管机房模式
    api_mode = tgw.ApiMode.kInternetMode  # 设置api模式 互联网模式
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


def CtrlC(signum, frame):
    print("bey bey")
    global g_is_running
    g_is_running = False


if __name__ == "__main__":
    signal.signal(signal.SIGINT, CtrlC)
    signal.signal(signal.SIGTERM, CtrlC)

    g_is_running = True
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
    while True:
        try:
            if g_is_running != True:
                break
        except Exception as e:
            print(str(e))
        time.sleep(1)

    tgw.IGMDApi_Release()
