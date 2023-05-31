import tgw
import time
import queue
import threading
import signal


# 实现日志回调，打印相关登录信息或者错误信息
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


# 实现推送回调
class DataHandler(tgw.IPushSpi):
    def __init__(self) -> None:
        super().__init__()
    def OnMDSnapshot(self, data, err):
        if not data is None:
            # print(data)
            pass
        else:
            print(err)

    def OnMDIndexSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDOptionSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDHKTSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)
    def OnMDAfterHourFixedPriceSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDCSIIndexSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)
    
    def OnMDCnIndexSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDHKTRealtimeLimit(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDHKTProductStatus(self, data, err):
        if not data is None:
            print(data)
        else:
            print(err)
    
    def OnMDHKTVCM(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDFutureSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnKLine(self, data, kline_type, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnSnapshotDerive(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnFactor(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDOrderBook(self, data, err):
        if not data is None:
            pass
        else:
            print(err)

    def OnMDOrderBookSnapshot(self, data, err):
        if not data is None:
            pass
        else:
            print(err)


def Quit(signum, frame):
    tgw.Close()
    exit(0)

signal.signal(signal.SIGINT, Quit)

# 第一步：注册日志回调，保证有日志输出
log_spi = MyLogSpi()
tgw.SetLogSpi(log_spi)

# 第二步，登录
cfg = tgw.Cfg()
cfg.server_vip = "127.0.0.1"
cfg.server_port = 8000
cfg.username = "****"    # 账号
cfg.password = "****"    # 密码
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


data_hander = DataHandler()

# 订阅因子数据
sub_factor_item = tgw.SubFactorItem()
sub_factor_item.factor_type = "all"
sub_factor_item.factor_sub_type = "all"
sub_factor_item.factor_name = "all"
success = tgw.SubFactor(sub_factor_item, data_hander)
if success != tgw.ErrorCode.kSuccess:
    print(tgw.GetErrorMsg(success))

# 订阅实时行情
sub_item = tgw.SubscribeItem()
sub_item.security_code = ""
sub_item.market = tgw.MarketType.kNone
data_hander.SetDfFormat(False)
success = tgw.Subscribe(sub_item, data_hander)
if success != tgw.ErrorCode.kSuccess:
    print(tgw.GetErrorMsg(success))

#订阅订单簿数据
sub_derived_items = []
sub_derived_item = tgw.SubscribeDerivedDataItem()
sub_derived_item.market = tgw.MarketType.kSZSE
sub_derived_item.security_code = "000001"
sub_derived_items.append(sub_derived_item)
sub_derived_item = tgw.SubscribeDerivedDataItem()
sub_derived_item.market = tgw.MarketType.kSSE
sub_derived_item.security_code = "600000"
sub_derived_items.append(sub_derived_item)
data_hander.SetDfFormat(False)
err_code = tgw.SubscribeDerivedData(tgw.SubscribeType.kSet,tgw.SubscribeDerivedDataType.kOrderBookSnapshot,sub_derived_items,push_spi=data_hander)
success = tgw.SubscribeDerivedData(tgw.SubscribeType.kSet, tgw.SubscribeDerivedDataType.kOrderBook, sub_derived_items, data_hander)
if success != tgw.ErrorCode.kSuccess:
    print(tgw.GetErrorMsg(success))



# 订阅全市场全品种000001代码行情
sub_item = tgw.SubscribeItem()
sub_item.market = tgw.MarketType.kNone
sub_item.flag = tgw.SubscribeDataType.kNone
sub_item.category_type = tgw.VarietyCategory.kNone
sub_item.security_code = "000001"

my_data_handler = DataHandler() # 新创建spi
err_code = tgw.Subscribe(sub_item, push_spi = my_data_handler)
if err_code != tgw.ErrorCode.kSuccess:
    err_str = tgw.GetErrorMsg(err_code)
    print(err_str)

# 订阅全市场全品种00001代码行情
sub_item = tgw.SubscribeItem()
sub_item.market = tgw.MarketType.kNone
sub_item.flag = tgw.SubscribeDataType.kNone
sub_item.category_type = tgw.VarietyCategory.kNone
sub_item.security_code = "00001"
# 回调只要注册一次即可，本次调用无需再注册
err_code = tgw.Subscribe(sub_item)
if err_code != tgw.ErrorCode.kSuccess:
    err_str = tgw.GetErrorMsg(err_code)
    print(err_str)


# 订阅全市场全品种399001代码行情
sub_item = tgw.SubscribeItem()
sub_item.market = tgw.MarketType.kNone
sub_item.flag = tgw.SubscribeDataType.kNone
sub_item.category_type = tgw.VarietyCategory.kNone
sub_item.security_code = "399001"
# 回调只要注册一次即可，本次调用无需再注册
err_code = tgw.Subscribe(sub_item)
if err_code != tgw.ErrorCode.kSuccess:
    err_str = tgw.GetErrorMsg(err_code)
    print(err_str)

# 订阅全市场全品种90001093代码行情
sub_item = tgw.SubscribeItem()
sub_item.market = tgw.MarketType.kNone
sub_item.flag = tgw.SubscribeDataType.kNone
sub_item.category_type = tgw.VarietyCategory.kNone
sub_item.security_code = "90001093"
# 回调只要注册一次即可，本次调用无需再注册
err_code = tgw.Subscribe(sub_item)
if err_code != tgw.ErrorCode.kSuccess:
    err_str = tgw.GetErrorMsg(err_code)
    print(err_str)


while True:
    time.sleep(10)