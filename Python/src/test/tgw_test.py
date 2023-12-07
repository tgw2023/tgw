# -*- coding: utf-8 -*-
import os
import sys
from tgw import tgw
import time
import signal
import json
from tgw_output_file import TgwOutPutFile
from tgw_commom import *


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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDIndexSnapshot(self, data, cnt):
        print("Receive MDIndexSnapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDIndexSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDOptionSnapshot(self, data, cnt):
        print("Receive MDOptionSnapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDOptionSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTSnapshot(self, data, cnt):
        print("Receive MDHKTSnapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDHKTSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDAfterHourFixedPriceSnapshot(self, data, cnt):
        print("Receive MDAfterHourFixedPriceSnapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDAfterHourFixedPriceSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDCSIIndexSnapshot(self, data, cnt):
        print("Receive MDCSIIndexSnapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDCSIIndexSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDCnIndexSnapshot(self, data, cnt):
        print("Receive MDCnIndexSnapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDCnIndexSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTRealtimeLimit(self, data, cnt):
        print("Receive MDHKTRealtimeLimit Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMHKTRealLimitToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTProductStatus(self, data, cnt):
        print("Receive MDHKTProductStatus Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDHKTProduStatusToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDHKTVCM(self, data, cnt):
        print("Receive MDHKTVCM Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDHKTVCMToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)

    def OnMDFutureSnapshot(self, data, cnt):
        print("Receive MDFutureSnapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(data, i)
            push_csv_writer.PushMDFutureSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(data)


    def OnKLine(self, kline, cnt, kline_type):
        print("Receive KLine Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(kline, i)
            push_csv_writer.PushMDKlineToCsv(data_item, kline_type)
        tgw.IGMDApi_FreeMemory(kline)
    
    def OnSnapshotDerive(self, snapshot_derive, cnt):
        print("Receive MDSnapshotDerive Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(snapshot_derive, i)
            push_csv_writer.PushMDSnapshotDeriveToCsv(data_item)
        tgw.IGMDApi_FreeMemory(snapshot_derive)
    
    def OnFactor(self, factor):
        print("Receive Factor Info: ")
        data_item = tgw.Tools_GetDataByIndex(factor, 0)
        push_csv_writer.PushMFactorToCsv(data_item)
        tgw.IGMDApi_FreeMemory(factor)

    def OnMDOrderBookSnapshot(self, order_book_snapshot, cnt):
        print("Receive MDOrderBookSnapshot Info: ")
        #序列化输出数据
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(order_book_snapshot, i)
            push_csv_writer.PushMDOrderBookSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(order_book_snapshot)

    def OnMDOrderBook(self, order_book):
        print("Receive MDOrderBook Info: ")
        #数据获取使用示例
        try:
            cnt = tgw.Tools_GetDataSize(order_book)
            for i in range(cnt):
                data = tgw.Tools_GetDataByIndex(order_book, i)
                push_csv_writer.PushMDOrderBookToCsv(data)
        except Exception as error:
            print (error)
            pass

#回放spi
class IReplayApp(tgw.IGMDHistorySpi):
    def OnMDSnapshot(self, task_id, snapshots, cnt):
        print("Receive stock snapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(snapshots, i)
            replay_csv_writer.ReplayMDStockSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDTickExecution(self, task_id, ticks, cnt):
        print("Receive MDTickExecution Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(ticks, i)
            replay_csv_writer.ReplayMDTickExecutionToCsv(data_item)
        tgw.IGMDApi_FreeMemory(ticks)

    def OnMDKline(self, task_id, klines, cnt, kline_type):
        print("Receive OnMDKline Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(klines, i)
            replay_csv_writer.ReplayMDKlineToCsv(data_item, kline_type)
        tgw.IGMDApi_FreeMemory(klines)
        
    def OnRspTaskStatus(self, task_id, task_status):
        print("task_id is: ", task_status.task_id)
        print("status is: ", task_status.status)
        print("error_code is: ", task_status.error_code)

#快照查询spi
class IQuerySnapshotSpi(tgw.IGMDSnapshotSpi):
    def OnMDSnapshotL1(self, snapshots, cnt):
        print("Receive stock snapshot l1 Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(snapshots, i)
            query_csv_writer.QueryMDStockSnapshotL1ToCsv(data_item)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDSnapshotL2(self, snapshots, cnt):
        print("Receive stock snapshot l2 Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(snapshots, i)
            query_csv_writer.QueryMDStockSnapshotL2ToCsv(data_item)
        tgw.IGMDApi_FreeMemory(snapshots)

    def OnMDIndexSnapshot(self, index_snapshots, cnt):
        print("Receive index snapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(index_snapshots, i)
            query_csv_writer.QueryMDIndexSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(index_snapshots)

    def OnMDHKTSnapshot(self, hk_snapshots, cnt):
        print("Receive hk snapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(hk_snapshots, i)
            query_csv_writer.QueryMDHKTSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(hk_snapshots)

    def OnMDOptionSnapshot(self, opt_snapshots, cnt):
        print("Receive option snapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(opt_snapshots, i)
            query_csv_writer.QueryMDOptionSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(opt_snapshots)

    def OnMDFutureSnapshot(self, future_ticks, cnt):
        print("Receive future snapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(future_ticks, i)
            query_csv_writer.QueryMDFutureSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(future_ticks)

    def OnMDHKExOrderSnapshot(self, order_snapshot, cnt):
        print("Receive hkex order snapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(order_snapshot, i)
            query_csv_writer.QueryMDOrderSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(order_snapshot)

    def OnMDHKExOrderBrokerSnapshot(self, order_broker_snapshot, cnt):
        print("Receive hkex order broker snapshot Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(order_broker_snapshot, i)
            query_csv_writer.QueryMDOrderBrokerSnapshotToCsv(data_item)
        tgw.IGMDApi_FreeMemory(order_broker_snapshot)

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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(tick_orders, i)
            query_csv_writer.QueryMDTickOrderToCsv(data_item)
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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(tick_execs, i)
            query_csv_writer.QueryMDTickExecutionToCsv(data_item)
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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(order_queues, i)
            query_csv_writer.QueryMDOrderQueueToCsv(data_item)
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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(klines, i)
            query_csv_writer.QueryMDKlineToCsv(data_item, kline_type)
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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(code_tables, i)
            query_csv_writer.QueryMDCodeTableToCsv(data_item)
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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(code_tables, i)
            query_csv_writer.QueryMDSecuritiesInfoToCsv(data_item)
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

# ETF信息查询spi
class IQueryETFInfoSpi(tgw.IGMDETFInfoSpi):
    def OnMDETFInfo(self, etf_info, cnt):
        print("Receive QueryETFInfoSpi Info: ")
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(etf_info, i)
            query_csv_writer.QueryMDETFInfoToCsv(data_item)
        tgw.IGMDApi_FreeMemory(etf_info)

    def OnStatus(self, status):
        print("Receive QueryETFInfoSpi Status : ")
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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(ex_factor_tables, i)
            query_csv_writer.QueryMDExFactorTableTosv(data_item)
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
        for i in range(cnt):
            data_item = tgw.Tools_GetDataByIndex(factors, i)
            query_csv_writer.QueryMDFactorToCsv(data_item)
        tgw.Tools_FreeMemory(factors, cnt)
    def OnStatus(self, status):
        print("Receive QueryFactorSpi Status : ")
        print("  task_id  =  "     , status.rsp_status.task_id)
        print("  error_code  =  "     , status.error_code)
        print("  error_msg_len  =  "  , status.error_msg_len)
        print("  error_msg  =  "      , status.error_msg)
        tgw.IGMDApi_FreeMemory(status)

class IQueryThirdInfoSpi(tgw.IGMDThirdInfoSpi):
    def OnThirdInfo(self, data, cnt):
        print("Receive QueryThirdInfoSpi Info: ")
        for i in range(cnt):
            sub_data = tgw.Tools_GetDataByIndex(data, i)
            query_csv_writer.QueryMDThirdInfoDataToCsv(sub_data)
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
        self.path = ""
        self.api_mode = 1
        self.enable_order_book = 0
        self.entry_size = 10
        self.order_queue_size = 10
        self.order_book_output_internal = 10000

class SubDerivedItem:
    def __init__(self):
        self.subscribe_type = 1
        self.derived_data_type = 0
        self.market_type = 101
        self.security_code = "000001"

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
        self.data_type = 0

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
sub_derived_vec = []
query_defualt_vec = []
query_kline_vec = []
query_secur_info_vec = []
query_etf_info_vec = []
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
        global sub_derived_vec
        global query_defualt_vec
        global query_kline_vec
        global query_secur_info_vec
        global query_etf_info_vec
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
        js_cfg.path = str(a['Path'])
        js_cfg.api_mode = a['ApiMode']
        js_cfg.enable_order_book = a['EnableOrderBook']
        js_cfg.entry_size = a['EntrySize']
        js_cfg.order_queue_size = a['OrderQueueSize']
        js_cfg.order_book_output_internal = a['OrderBookOutputInternal']
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
            try:
                cfg = tgw.SubscribeItem()
                cfg.market = GetMarkert(it["market_type"])
                cfg.flag = GetSubType(it["data_type"])
                cfg.category_type = GetCategory(it["category_type"])
                if (it["security_code"] == "All"):
                    cfg.security_code = ""
                else:
                    cfg.security_code = it["security_code"]
                sub_vec.append(cfg)
            except Exception as error:
                print("Subscribe exception error: ", error)

        for it in a["SubFactor"]:
            if it["Enable"] == False:
                continue
            try:
                item = tgw.SubFactorItem()
                item.factor_name = it["factor_name"]
                item.factor_sub_type = it["factor_sub_type"]
                item.factor_type = it["factor_type"]
                item.security_code = it["security_code"]
                item.market = GetMarkert(it["market"])
                item.category = GetCategory(it["category"])
                sub_fac_vec.append(item)
            except Exception as error:
                print("SubFactor exception error: ", error)

        for it in a["SubDerivedData"]:
            if it["Enable"] == False:
                continue
            try:
                tmp_sub_derived_item = SubDerivedItem()
                tmp_sub_derived_item.market_type = GetMarkert(it["market_type"])
                tmp_sub_derived_item.security_code = it["security_code"]
                tmp_sub_derived_item.subscribe_type = it["subscribe_type"]
                tmp_sub_derived_item.derived_data_type = it["derived_data_type"]
                sub_derived_vec.append(tmp_sub_derived_item)
            except Exception as error:
                print("SubDerivedData exception error: ", error)

        for it in a["QueryDefault"]:
            if it["Enable"] == False:
                continue
            try: 
                item = QueryDefault()
                item.type = it["type"]
                item.security_code = it["security_code"]
                item.date = it["date"]
                item.begin_time = it["begin_time"]
                item.end_time = it["end_time"]
                item.data_type = it["data_type"]
                query_defualt_vec.append(item)
            except Exception as error:
                print("QueryDefault exception error: ", error)

        for it in a["QueryKLine"]:
            if it["Enable"] == False:
                continue
            try:
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
            except Exception as error:
                print("QueryKLine exception error: ", error)
         
        for it in a['QuerySecurInfo']:
            if it["Enable"] == False:
                continue
            try:
                query_secur_info_vec.append(it["security_code"])
            except Exception as error:
                print("QuerySecurInfo exception error: ", error)

        for it in a['QueryETFInfo']:
            if it["Enable"] == False:
                continue
            try:
                query_etf_info_vec.append(it["security_code"])
            except Exception as error:
                print("QueryETFInfo exception error: ", error)

        for it in a['QueryExFactorTable']:
            if it["Enable"] == False:
                continue
            try:
                query_ex_factor_vec.append(it["security_code"])
            except Exception as error:
                print("QueryExFactorTable exception error: ", error)

        for it in a["QueryFactor"]:
            if it["Enable"] == False:
                continue
            try:
                item = tgw.ReqFactor()
                item.task_id = tgw.IGMDApi_GetTaskID()
                item.factor_name = it["factor_name"]
                item.factor_sub_type = it["factor_sub_type"]
                item.factor_type = it["factor_type"]
                item.begin_date = it["begin_date"]
                item.end_date = it["end_date"]
                item.begin_time = it["begin_time"]
                item.end_time = it["end_time"]
                item.security_code = it["security_code"]
                item.market = it["market"]
                item.category = it["category"]
                if  "count" in it:
                    item.count = it["count"]
                query_factor_vec.append(item)
            except Exception as error:
                print("QueryFactor exception error: ", error)

        is_query_codetable = a["QueryCodeTable"]["Enable"]

        if (a["QueryThirdInfo"]["Enable"] == True):
            try:
                for i in a["QueryThirdInfo"]["item"]:
                    item = QueryThirdInfoItem()
                    item.key = i["key"]
                    item.value = i["value"]
                    query_thirdinfo_vec.append(item)
            except Exception as error:
                print("QueryThirdInfo exception error: ", error)        

        for it in a["ReplaySnapshot"]:
            if it["Enable"] == False:
                continue
            try:
                item = ReplayDefualt()
                item.begin_date = it["begin_date"]
                item.end_date = it["end_date"]
                item.begin_time = it["begin_time"]
                item.end_time = it["end_time"]
                item.security_code = it["security_code"]
                replay_snapshot.append(item)
            except Exception as error:
                print("ReplaySnapshot exception error: ", error)

        for it in a["ReplayTickExection"]:
            if it["Enable"] == False:
                continue
            try:
                item = ReplayDefualt()
                item.begin_date = it["begin_date"]
                item.end_date = it["end_date"]
                item.begin_time = it["begin_time"]
                item.end_time = it["end_time"]
                item.security_code = it["security_code"]
                replay_tick_exec.append(item)
            except Exception as error:
                print("ReplayTickExection exception error: ", error)

        for it in a["ReplayKLine"]:
            if it["Enable"] == False:
                continue
            try:
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
            except Exception as error:
                print("ReplayKLine exception error: ", error)

    except Exception as e:
        print("exception error: ", e)

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
spi_etf_info = IQueryETFInfoSpi()
spi_ex_factor = IQueryExFactorSpi()
spi_factor = IQueryFactorSpi()
spi_third_info = IQueryThirdInfoSpi()
spi_replay = IReplayApp()

query_csv_writer = None
push_csv_writer = None
replay_csv_writer = None

def DealSub():
    global sub_vec
    for i in sub_vec:
        tgw.IGMDApi_Subscribe(i, 1)
    
    for i in sub_fac_vec:
        ret = tgw.IGMDApi_SubFactor(i, 1)

    for i in sub_derived_vec:
        tmp_sub_derived = tgw.SubscribeDerivedDataItem()
        tmp_sub_derived.market = i.market_type
        tmp_sub_derived.security_code = i.security_code
        ret = tgw.IGMDApi_SubscribeDerivedData(i.subscribe_type, i.derived_data_type, tmp_sub_derived, 1)

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
            req_tick.data_type = i.data_type #0标识快照，1港股委托挂单，2港股经纪商席位
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

    for i in query_etf_info_vec:
        #查询证券代码信息
        item = tgw.SubCodeTableItem()
        item.market = GetMarkert(i.split('.')[1])
        item.security_code = i.split('.')[0]
        tgw.IGMDApi_QueryETFInfo(spi_etf_info, item, 1)
            
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

    # 落地文件初始化
    global query_csv_writer, push_csv_writer, replay_csv_writer
    query_csv_writer = TgwOutPutFile(js_cfg.csv_path + "/query")
    push_csv_writer = TgwOutPutFile(js_cfg.csv_path + "/push")
    replay_csv_writer = TgwOutPutFile(js_cfg.csv_path + "/replay")

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
    cfg.coloca_cfg.enable_order_book = js_cfg.enable_order_book
    cfg.coloca_cfg.entry_size = js_cfg.entry_size
    cfg.coloca_cfg.order_queue_size = js_cfg.order_queue_size
    cfg.coloca_cfg.order_book_deliver_interval_microsecond = js_cfg.order_book_output_internal

    if (tgw.IGMDApi_Init(spi, cfg, js_cfg.api_mode, js_cfg.path) != tgw.ErrorCode.kSuccess):
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