# coding=utf-8
import sys
from tgw import tgw


# 获取数组指定下标元素
def get_tgw_intdata_by_index(list, index):
    return str(tgw.Tools_GetInt64DataByIndex(list, index))

# 将数组元素组合字符串
def get_tgw_list_to_str(list, list_size, get_sig_data_func):
    if(list_size < 1):
        return ''
    
    out_str = ''
    for i in range(list_size):
        out_str += get_sig_data_func(list, i) + '|'
    return out_str[:len(out_str) -1] 

def SerializeMDOrderBookItem(data):
    try:
        tmp_order_queue = get_tgw_list_to_str(data.order_queue, 50, get_tgw_intdata_by_index)
        data_str = str(data.price) + "->" + str(data.volume) + "->" + str(data.order_queue_size) + "->" + str(tmp_order_queue)
        return data_str
    except Exception as error:
        print('SerializeMDOrderBookItem exception:' + str(error))

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

