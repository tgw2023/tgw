# -*- coding: utf-8 -*-
import os
from re import S
import sys
from tgw import tgw
import time
import signal
import json



class IAMDSpiApp(tgw.IGMDSpi):
    def OnLog(self, level, log, len):
        print("TGW log: ", "level: ",level, end='')
        print("     log:   ",log)
        
    def OnLogon(self, data):
        print("TGW Logon information:  : ")
        print("api_mode : ", data.api_mode)
        print("logon json : ", data.logon_json)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDSnapshot(self, data, cnt):
        print("Receive MDSnapshot Info: ")
        tgw.Tools_WriteStockSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDIndexSnapshot(self, data, cnt):
        print("Receive MDIndexSnapshot Info: ")
        tgw.Tools_WriteIndexSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDOptionSnapshot(self, data, cnt):
        print("Receive MDOptionSnapshot Info: ")
        tgw.Tools_WriteOptionSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTSnapshot(self, data, cnt):
        print("Receive MDHKTSnapshot Info: ")
        tgw.Tools_WriteHKTSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDAfterHourFixedPriceSnapshot(self, data, cnt):
        print("Receive MDAfterHourFixedPriceSnapshot Info: ")
        tgw.Tools_WriteAfterHourFixPriceSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDCSIIndexSnapshot(self, data, cnt):
        print("Receive MDCSIIndexSnapshot Info: ")
        tgw.Tools_WriteCSIIndexSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDCnIndexSnapshot(self, data, cnt):
        print("Receive MDCnIndexSnapshot Info: ")
        tgw.Tools_WriteCnIndexSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTRealtimeLimit(self, data, cnt):
        print("Receive MDHKTRealtimeLimit Info: ")
        tgw.Tools_WriteHKTRealLimit(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTProductStatus(self, data, cnt):
        print("Receive MDHKTProductStatus Info: ")
        tgw.Tools_WriteHKTProduStatus(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTVCM(self, data, cnt):
        print("Receive MDHKTVCM Info: ")
        tgw.Tools_WriteHKTVCM(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDFutureSnapshot(self, data, cnt):
        print("Receive MDFutureSnapshot Info: ")
        tgw.Tools_WriteFutureSnapshot(data, cnt)
        tgw.IGMDApi_FreeMemory(data)


    def OnKLine(self, kline, cnt, kline_type):
        print("Receive KLine Info: ")
        tgw.Tools_WriteKline(kline, cnt, kline_type)
        tgw.IGMDApi_FreeMemory(kline)
    
    def OnSnapshotDerive(self, snapshot_derive, cnt):
        print("Receive MDSnapshotDerive Info: ")
        tgw.Tools_WriteSnapshotDerive(snapshot_derive, cnt)
        tgw.IGMDApi_FreeMemory(snapshot_derive)
    
    def OnFactor(self, factor):
        print("Receive Factor Info: ")
        tgw.Tools_WriteFactor(factor)
        tgw.IGMDApi_FreeMemory(factor)

#回放spi
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

#快照查询spi
class IQuerySnapshotSpi(tgw.IGMDSnapshotSpi):
    def OnMDSnapshotL1(self, snapshots, cnt):
        print("Receive stock snapshot l1 Info: ")
        tgw.Tools_WriteQueryStockSnapshot(snapshots, cnt)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDSnapshotL2(self, snapshots, cnt):
        print("Receive stock snapshot l2 Info: ")
        tgw.Tools_WriteQueryStockSnapshot(snapshots, cnt)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDIndexSnapshot(self, index_snapshots, cnt):
        print("Receive index snapshot Info: ")
        tgw.Tools_WriteQueryIndexSnapshot(index_snapshots, cnt)
        tgw.IGMDApi_FreeMemory(index_snapshots)

    def OnMDHKTSnapshot(self, hk_snapshots, cnt):
        print("Receive hk snapshot Info: ")
        tgw.Tools_WriteQueryHKTSnapshot(hk_snapshots, cnt)
        tgw.IGMDApi_FreeMemory(hk_snapshots)

    def OnMDOptionSnapshot(self, opt_snapshots, cnt):
        print("Receive option snapshot Info: ")
        tgw.Tools_WriteQueryOptionSnapshot(opt_snapshots, cnt)
        tgw.IGMDApi_FreeMemory(opt_snapshots)

    def OnMDFutureSnapshot(self, future_ticks, cnt):
        print("Receive future snapshot Info: ")
        tgw.Tools_WriteQueryFutureSnapshot(future_ticks, cnt)
        tgw.IGMDApi_FreeMemory(future_ticks)

    def OnStatus(self, status):
        print("Receive QuerySnapshotSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  req_type  =  "     , status.rsp_union_status.req_type)
        print("  security_code  =  "  , status.rsp_union_status.security_code)
        print("  market_type  =  "  , status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)

#逐笔委托查询spi
class IQueryTickOrderSpi(tgw.IGMDTickOrderSpi):
    def OnMDTickOrder(self, tick_orders, cnt):
        print("Receive QueryTickOrderSpi Info: ")
        tgw.Tools_WriteQueryTickOrder(tick_orders, cnt)
        tgw.IGMDApi_FreeMemory(tick_orders)

    def OnStatus(self, status):
        print("Receive QueryTickOrderSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  req_type  =  "     , status.rsp_union_status.req_type)
        print("  security_code  =  "  , status.rsp_union_status.security_code)
        print("  market_type  =  "  , status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)

#逐笔成交spi
class IQueryTickExecutionSpi(tgw.IGMDTickExecutionSpi):
    def OnMDTickExecution(self, tick_execs, cnt):
        print("Receive QueryTickExecutionSpi Info: ")
        tgw.Tools_WriteQueryTickExecution(tick_execs, cnt)
        tgw.IGMDApi_FreeMemory(tick_execs)

    def OnStatus(self, status):
        print("Receive QueryTickExecutionSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  req_type  =  "     , status.rsp_union_status.req_type)
        print("  security_code  =  "  , status.rsp_union_status.security_code)
        print("  market_type  =  "  , status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)

#委托队列spi
class IQueryOrderQueueSpi(tgw.IGMDOrderQueueSpi):
    def OnMDOrderQueue(self, order_queues, cnt):
        print("Receive QueryOrderQueueSpi Info: ")
        tgw.Tools_WriteQueryOrderQueue(order_queues, cnt)
        tgw.IGMDApi_FreeMemory(order_queues)

    def OnStatus(self, status):
        print("Receive QueryOrderQueueSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  req_type  =  "     , status.rsp_union_status.req_type)
        print("  security_code  =  "  , status.rsp_union_status.security_code)
        print("  market_type  =  "  , status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)

# k线查询spi
class IQueryKlineSpi(tgw.IGMDKlineSpi):
    def OnMDKLine(self, klines, cnt, kline_type):
        print("Receive QueryKlineSpi Info: ")
        tgw.Tools_WriteQueryKline(klines, cnt, kline_type)
        tgw.IGMDApi_FreeMemory(klines)

    def OnStatus(self, status):
        print("Receive QueryKlineSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  req_type  =  "     , status.rsp_union_status.req_type)
        print("  security_code  =  "  , status.rsp_union_status.security_code)
        print("  market_type  =  "  , status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)

# 代码表查询spi
class IQueryCodeTableSpi(tgw.IGMDCodeTableSpi):
    def OnMDCodeTable(self, code_tables, cnt):
        print("Receive QueryCodeTableSpi Info: ")
        tgw.Tools_WriteQueryCodeTable(code_tables, cnt)
        tgw.IGMDApi_FreeMemory(code_tables)

    def OnStatus(self, status):
        print("Receive QueryCodeTableSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  req_type  =  "     , status.rsp_union_status.req_type)
        print("  security_code  =  "  , status.rsp_union_status.security_code)
        print("  market_type  =  "  , status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)

# 证券代码信息查询spi
class IQuerySecuritiesInfoSpi(tgw.IGMDSecuritiesInfoSpi):
    def OnMDSecuritiesInfo(self, code_tables, cnt):
        print("Receive QuerySecuritiesInfoSpi Info: ")
        tgw.Tools_WriteQuerySecurInfo(code_tables, cnt)
        tgw.IGMDApi_FreeMemory(code_tables)

    def OnStatus(self, status):
        print("Receive QuerySecuritiesInfoSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)

        for i in range(status.rsp_stockinfo_status.code_table_item_cnt):
            item = tgw.Tools_GetSubCodeTableItemByIndex(status.rsp_stockinfo_status.codes, i)
            print("  security_code  =  "  , item.security_code)
            print("  market_type  =  "  , item.market)
        tgw.IGMDApi_FreeMemory(status)

# 复权因子表信息查询spi
class IQueryExFactorSpi(tgw.IGMDExFactorSpi):
    def OnMDExFactor(self, ex_factor_tables, cnt):
        print("Receive QueryExFactorSpi Info: ")
        tgw.Tools_WriteQueryExFactor(ex_factor_tables, cnt)
        tgw.IGMDApi_FreeMemory(ex_factor_tables)

    def OnStatus(self, status):
        print("Receive QueryExFactorSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  req_type  =  "     , status.rsp_union_status.req_type)
        print("  security_code  =  "  , status.rsp_union_status.security_code)
        print("  market_type  =  "  , status.rsp_union_status.market_type)
        tgw.IGMDApi_FreeMemory(status)

# 加工因子查询spi
class IQueryFactorSpi(tgw.IGMDFactorSpi):
    def OnFactor(self, factors, cnt):
        print("Receive QueryFactorSpi Info: ")
        tgw.Tools_WriteQueryFactor(factors, cnt)
        tgw.Tools_FreeMemory(factors, cnt)
    def OnStatus(self, status):
        print("Receive QueryFactorSpi Status : ")
        print("  factor_type  =  "     , status.rsp_factor_status.factor_type)
        print("  factor_sub_type  =  "  , status.rsp_factor_status.factor_sub_type)
        print("  factor_name  =  "  , status.rsp_factor_status.factor_name)
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        tgw.IGMDApi_FreeMemory(status)

class IQueryThirdInfoSpi(tgw.IGMDThirdInfoSpi):
    def OnThirdInfo(self, data, cnt):
        print("Receive QueryThirdInfoSpi Info: ")
        tgw.Tools_WriteQueryThirdInfo(data, cnt)
        tgw.IGMDApi_FreeMemory(data)

    def OnStatus(self, status):
        print("Receive QueryThirdInfoSpi Status : ")
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        print("  task_id  =  "     , status.rsp_thirdinfo_status.task_id)
        tgw.IGMDApi_FreeMemory(status)

class JsCfg:
    def __init__(self):
        self.ip = ""
        self.port = 0
        self.username = ""
        self.password = ""
        self.qtcp_threads = 2
        self.qtcp_req_timeout = 1
        self.qtcp_max_cnt = 100
        self.port = 0
        self.mode = []
        self.csv_path = "./"
        self.api_mode = 1

class UpadatePasswordCfg:
    def __init__(self):
        self.enable = False
        self.username = ""
        self.old_password = ""
        self.new_password = ""

class QueryDefault:
    def __init__(self):
        self.type = ""
        self.security_code = ""
        self.date = ""
        self.begin_time = ""
        self.end_time = ""

class QueryThirdInfoItem:
    def __init__(self):
        self.key = ""
        self.value = ""


class QueryKLine:
    def __init__(self):
        self.type = ""
        self.auto_complete = ""
        self.cq_flag = ""
        self.security_code = ""
        self.begin_date = ""
        self.end_date = ""
        self.begin_time = ""
        self.end_time = ""


class ReplayKLine:
    def __init__(self):
        self.type = ""
        self.auto_complete = ""
        self.cq_flag = ""
        self.security_code = []
        self.begin_date = ""
        self.end_date = ""
        self.begin_time = ""
        self.end_time = ""

class ReplayDefualt:
    def __init__(self):
        self.security_code = []
        self.begin_date = ""
        self.end_date = ""
        self.begin_time = ""
        self.end_time = ""


js_cfg = JsCfg()
update_password = UpadatePasswordCfg()
sub_vec = []
sub_fac_vec = []
query_defualt_vec = []
query_kline_vec = []
query_secur_info_vec = []
query_ex_factor_vec = []
query_factor_vec = []
query_thirdinfo_vec = []
is_query_codetable = False
replay_kline = []
replay_tick_exec = []
replay_snapshot = []

def ParseConfig():
    with open('./etc/test.json','rb+') as f:
        a = json.load(f)
    try:
        global js_cfg
        global update_password
        global sub_vec
        global sub_fac_vec
        global query_defualt_vec
        global query_kline_vec
        global query_secur_info_vec
        global query_ex_factor_vec
        global query_factor_vec
        global is_query_codetable
        global query_thirdinfo_vec

        js_cfg.ip = str(a['ServerVip'])
        js_cfg.port = a['ServerPort']
        js_cfg.username = str(a['UserName'])
        js_cfg.password = str(a['Password'])
        js_cfg.qtcp_max_cnt = a['ColocQTcpMaxReqCnt']
        js_cfg.qtcp_threads = a['ColocQTcpChannelThread']
        js_cfg.qtcp_req_timeout = a['ColocQTcpReqTimeOut']
        js_cfg.csv_path = str(a['CsvFileDir'])
        js_cfg.api_mode = a['ApiMode']
        for i in a['ColocChannelMode']:
            js_cfg.mode.append(i)

        # 获取修改密码的配置
        update_password.enable = a['UpdatePassWord']['Enable']
        update_password.username = a['UpdatePassWord']['Username']
        update_password.old_password = a['UpdatePassWord']['OldPassword']
        update_password.new_password = a['UpdatePassWord']['NewPassword']

        for it in a['Subscribe']:
            if it["Enable"] == False:
                continue
            cfg = tgw.SubscribeItem()
            cfg.market = GetMarkert(it["market_type"])
            cfg.flag = GetSubType(it["data_type"])
            cfg.category_type = GetCategory(it["category_type"])
            if (it["security_code"] == "All"):
                cfg.security_code = ""
            else:
                cfg.security_code = it["security_code"]
            sub_vec.append(cfg)

        for it in a["SubFactor"]:
            if it["Enable"] == False:
                continue
            item = tgw.SubFactorItem()
            item.factor_name = it["factor_name"]
            item.factor_sub_type = it["factor_sub_type"]
            item.factor_type = it["factor_type"]
            sub_fac_vec.append(item)
        
        for it in a["QueryDefault"]:
            if it["Enable"] == False:
                continue
            item = QueryDefault()
            item.type = it["type"]
            item.security_code = it["security_code"]
            item.date = it["date"]
            item.begin_time = it["begin_time"]
            item.end_time = it["end_time"]
            query_defualt_vec.append(item)
        
        for it in a["QueryKLine"]:
            if it["Enable"] == False:
                continue
            
            item = tgw.ReqKline()
            item.cyc_type = GetKlineType(it["type"]) 
            item.auto_complete = it["auto_complete"]
            item.cq_flag = GetCqFlag(it["cq_flag"])
            item.security_code = it["security_code"].split('.')[0]
            item.market_type = GetMarkert(it["security_code"].split('.')[1])
            item.begin_date = it["begin_date"]
            item.end_date = it["end_date"]
            item.begin_time = it["begin_time"]
            item.end_time = it["end_time"]
            query_kline_vec.append(item)

         
        for it in a['QuerySecurInfo']:
            if it["Enable"] == False:
                continue
            query_secur_info_vec.append(it["security_code"])

        for it in a['QueryExFactorTable']:
            if it["Enable"] == False:
                continue
            query_ex_factor_vec.append(it["security_code"])
        
        for it in a["QueryFactor"]:
            if it["Enable"] == False:
                continue
            item = tgw.ReqFactor() 
            item.factor_name = it["factor_name"]
            item.factor_sub_type = it["factor_sub_type"]
            item.factor_type = it["factor_type"]
            item.begin_date = it["begin_date"]
            item.end_date = it["end_date"]
            item.begin_time = it["begin_time"]
            item.end_time = it["end_time"]
            query_factor_vec.append(item)

        is_query_codetable = a["QueryCodeTable"]["Enable"]

        if (a["QueryThirdInfo"]["Enable"] == True):
            for i in a["QueryThirdInfo"]["item"]:
                item = QueryThirdInfoItem()
                item.key = i["key"]
                item.value = i["value"]
                query_thirdinfo_vec.append(item)
        

        for it in a["ReplaySnapshot"]:
            if it["Enable"] == False:
                continue
            item = ReplayDefualt()
            item.begin_date = it["begin_date"]
            item.end_date = it["end_date"]
            item.begin_time = it["begin_time"]
            item.end_time = it["end_time"]
            item.security_code = it["security_code"]
            replay_snapshot.append(item)

        for it in a["ReplayTickExection"]:
            if it["Enable"] == False:
                continue
            item = ReplayDefualt()
            item.begin_date = it["begin_date"]
            item.end_date = it["end_date"]
            item.begin_time = it["begin_time"]
            item.end_time = it["end_time"]
            item.security_code = it["security_code"]
            replay_tick_exec.append(item)
        
        for it in a["ReplayKLine"]:
            if it["Enable"] == False:
                continue
            item = QueryKLine()
            item.type = it["type"]
            item.auto_complete = it["auto_complete"]
            item.cq_flag = it["cq_flag"]
            item.security_code = it["security_code"]
            item.begin_date = it["begin_date"]
            item.end_date = it["end_date"]
            item.begin_time = it["begin_time"]
            item.end_time = it["end_time"]
            replay_kline.append(item)
    except Exception as e:
        print(e)

g_is_running = True
cfg = tgw.Cfg()
spi = IAMDSpiApp()
spi_kline = IQueryKlineSpi()
spi_snap = IQuerySnapshotSpi()
spi_tick_order = IQueryTickOrderSpi()
spi_tick_exec = IQueryTickExecutionSpi()
spi_order_queue = IQueryOrderQueueSpi()
spi_code_table = IQueryCodeTableSpi()
spi_secur_info = IQuerySecuritiesInfoSpi()
spi_ex_factor = IQueryExFactorSpi()
spi_factor = IQueryFactorSpi()
spi_third_info = IQueryThirdInfoSpi()
spi_replay = IReplayApp()


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

def DealSub():
    global sub_vec
    for i in sub_vec:
        tgw.IGMDApi_Subscribe(i, 1)
    
    for i in sub_fac_vec:
        ret = tgw.IGMDApi_SubFactor(i, 1)

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
    #更新密码
    if update_password.enable == True:
        if (len(update_password.username) > 31):
            print("UpdatePassWord failed, param lenth of username is not support, now lenth: ", len(update_password.username))
            return
        if (len(update_password.old_password) > 63):
            print("UpdatePassWord failed, param lenth of old_password is not support, now lenth: ", len(update_password.old_password))
            return
        if (len(update_password.new_password) > 63):
            print("UpdatePassWord failed, param lenth of new_password is not support, now lenth: ", len(update_password.new_password))
            return
        up_password_req = tgw.UpdatePassWordReq()
        up_password_req.username = update_password.username
        up_password_req.old_password = update_password.old_password
        up_password_req.new_password = update_password.new_password
        ec = tgw.IGMDApi_UpdatePassWord(up_password_req)
        if ec != tgw.ErrorCode.kSuccess:
            print("UpdatePassWord failed, error code is : ", ec)
        else:
            print("UpdatePassWord success")

def DealQuery():
    # 查询k线
    for i in query_kline_vec:
        ret = tgw.IGMDApi_QueryKline(spi_kline, i)
    for i in query_defualt_vec:
        if i.type == "GetSnapshot":
            #查询快照
            req_tick = tgw.ReqDefault()
            req_tick.begin_time = i.begin_time
            req_tick.date = i.date
            req_tick.end_time = i.end_time
            req_tick.security_code = i.security_code.split('.')[0]
            req_tick.market_type = GetMarkert(i.security_code.split('.')[1])
            tgw.IGMDApi_QuerySnapshot(spi_snap, req_tick)
        elif i.type == "GetOrder":
            #查询逐笔委托
            req_tick_order = tgw.ReqDefault()
            req_tick_order.begin_time = i.begin_time
            req_tick_order.date = i.date
            req_tick_order.end_time = i.end_time

            req_tick_order.security_code = i.security_code.split('.')[0]
            req_tick_order.market_type = GetMarkert(i.security_code.split('.')[1])
            tgw.IGMDApi_QueryTickOrder(spi_tick_order, req_tick_order)
        elif i.type == "GetTickExecution":
            #查询逐笔成交
            req_tick_execution = tgw.ReqDefault()
            req_tick_execution.begin_time = i.begin_time
            req_tick_execution.date = i.date
            req_tick_execution.end_time = i.end_time
            req_tick_execution.security_code = i.security_code.split('.')[0]
            req_tick_execution.market_type = GetMarkert(i.security_code.split('.')[1]) 
            tgw.IGMDApi_QueryTickExecution(spi_tick_exec, req_tick_execution)
        elif i.type == "GetOrderQueue":
            #查询委托队列
            req_order_queue = tgw.ReqDefault()
            req_order_queue.begin_time = i.begin_time
            req_order_queue.date = i.date
            req_order_queue.end_time = i.end_time
            req_order_queue.security_code = i.security_code.split('.')[0]
            req_order_queue.market_type = GetMarkert(i.security_code.split('.')[1])
            tgw.IGMDApi_QueryOrderQueue(spi_order_queue, req_order_queue)
    global is_query_codetable
    if is_query_codetable == True:
        # 查询代码表
        tgw.IGMDApi_QueryCodeTable(spi_code_table)  
    for i in query_secur_info_vec:
        #查询证券代码信息
        item = tgw.SubCodeTableItem()
        item.market = GetMarkert(i.split('.')[1])
        item.security_code = i.split('.')[0]
        tgw.IGMDApi_QuerySecuritiesInfo(spi_secur_info, item, 1)
            
    for i in query_ex_factor_vec:
        #查询复权因子信息表
        code2 = i
        tgw.IGMDApi_QueryExFactorTable(spi_ex_factor, code2)

    for i in query_factor_vec:
        #查询因子         
        tgw.IGMDApi_QueryFactor(spi_factor, i)

    #查询三方咨询
    task_id = tgw.IGMDApi_GetTaskID()
    for i in query_thirdinfo_vec:
        tgw.IGMDApi_SetThirdInfoParam(task_id, i.key, i.value)
    if (len(query_thirdinfo_vec) != 0):
        tgw.IGMDApi_QueryThirdInfo(spi_third_info, task_id)

def DealReplay():
    
    #回放逐笔成交
    for it in replay_tick_exec:
        req_replay = tgw.ReqReplay()
        req_replay.begin_date = it.begin_date
        req_replay.end_date = it.end_date
        req_replay.begin_time = it.begin_time
        req_replay.end_time = it.end_time
        req_replay.task_id = tgw.IGMDApi_GetTaskID()

        req_replay.req_item_cnt = len(it.security_code)
        req_replay.req_items = tgw.Tools_CreateReqHistoryItem(len(it.security_code))
        i = 0
        for code in it.security_code:
            history_item = tgw.ReqHistoryItem()
            history_item.market = GetMarkert(code.split('.')[1])
            history_item.security_code = code.split('.')[0]
            tgw.Tools_SetReqHistoryItem(req_replay.req_items, i, history_item)
            i = i+1
        req_replay.md_data_type = tgw.MDDatatype.kTickExecution
        tgw.IGMDApi_ReplayRequest(spi_replay, req_replay)
    
    #回放快照
    for it in replay_snapshot:
        req_replay2 = tgw.ReqReplay()
        req_replay2.begin_date = it.begin_date
        req_replay2.end_date = it.end_date
        req_replay2.begin_time = it.begin_time
        req_replay2.end_time = it.end_time
        req_replay2.task_id = tgw.IGMDApi_GetTaskID()

        req_replay2.req_item_cnt = len(it.security_code)
        req_replay2.req_items = tgw.Tools_CreateReqHistoryItem(len(it.security_code))
        j = 0
        for code in it.security_code:
            history_item2 = tgw.ReqHistoryItem()
            history_item2.market = GetMarkert(code.split('.')[1])
            history_item2.security_code = code.split('.')[0]
            tgw.Tools_SetReqHistoryItem(req_replay2.req_items, j, history_item2)
            j = j+1
        req_replay2.md_data_type = tgw.MDDatatype.kSnapshot
        tgw.IGMDApi_ReplayRequest(spi_replay, req_replay2)

    #回放k线
    for it in replay_kline:
        replay_k = tgw.ReqReplayKline()
        replay_k.begin_date = it.begin_date
        replay_k.begin_time = it.begin_time 
        replay_k.cq_flag = GetCqFlag(it.cq_flag)
        replay_k.cyc_type = GetKlineType(it.type)
        replay_k.auto_complete = it.auto_complete
        replay_k.end_date = it.end_date
        replay_k.end_time = it.end_time
        replay_k.task_id = tgw.IGMDApi_GetTaskID()
        replay_k.req_item_cnt = len(it.security_code)
        replay_k.req_items = tgw.Tools_CreateReqHistoryItem(len(it.security_code))
        k = 0
        for code in it.security_code:
            history_item3 = tgw.ReqHistoryItem()
            history_item3.market = GetMarkert(code.split('.')[1])
            history_item3.security_code = code.split('.')[0]
            tgw.Tools_SetReqHistoryItem(replay_k.req_items, k, history_item3)
            k = k+1
        tgw.IGMDApi_ReplayKline(spi_replay, replay_k)


def GetChannelMode():
    ret_mode = 0
    for i in js_cfg.mode:
        if i == "QTCP":
            ret_mode = ret_mode | tgw.ColocatChannelMode.kQTCP
        elif i == "TCP":
            ret_mode = ret_mode | tgw.ColocatChannelMode.kTCP
        elif i == "RTCP":
            ret_mode = ret_mode | tgw.ColocatChannelMode.kRTCP
    return ret_mode

def Init():
    tgw.Tools_Init(js_cfg.csv_path)
    # 准备tgw配置
    cfg.server_vip = js_cfg.ip
    cfg.server_port = js_cfg.port

    #登录账号配置
    cfg.username = js_cfg.username    # 账号
    cfg.password = js_cfg.password    # 密码
    cfg.coloca_cfg.channel_mode = GetChannelMode()
    
    cfg.coloca_cfg.qtcp_channel_thread = js_cfg.qtcp_threads
    cfg.coloca_cfg.qtcp_max_req_cnt = js_cfg.qtcp_max_cnt
    cfg.coloca_cfg.qtcp_req_time_out = js_cfg.qtcp_req_timeout

    if (tgw.IGMDApi_Init(spi, cfg, js_cfg.api_mode) != tgw.ErrorCode.kSuccess):
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
    ParseConfig()
    Init()
    time.sleep(2)
    HandleUpdatePassword()
    DealQuery()
    DealSub()
    DealReplay()
    while True:
        try:
            if g_is_running != True:
                break
        except Exception as e:
            print(str(e))
        time.sleep(1)

    tgw.IGMDApi_Release()