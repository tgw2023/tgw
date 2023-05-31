import tgw
import threading
import signal
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



g_wait_event = threading.Event()
# K线回放处理函数
def OnResponseKline(task_id, result, err):
    if not result is None:
        print("Kline:",result)
    else:
        print(err)
# 快照数据回放处理函数
def OnResponseSnapshot(task_id, result, err):
    if not result is None:
        print("Snapshot:",result)
    else:
        print(err)
# 逐笔成交数据回放处理函数
def OnResponseTickExec(task_id, result, err):
    if not result is None:
        print("TickExecution:",result)
    else:
        print(err)

def Quit(signum, frame):
    tgw.Close()
    exit(0)
signal.signal(signal.SIGINT, Quit)

# 第一步：设置日志spi，保证有日志输出
log_spi = MyLogSpi()
tgw.SetLogSpi(log_spi)

# # 第二步，登录
cfg = tgw.Cfg()
cfg.server_vip = "127.0.0.1"
cfg.server_port = 8000
cfg.username = "****"    # 账号
cfg.password = "****"    # 密码

cfg.coloca_cfg.channel_mode = tgw.ColocatChannelMode.kRTCP # tcp查询模式
cfg.coloca_cfg.qtcp_channel_thread = 2
cfg.coloca_cfg.qtcp_max_req_cnt = 1000

try:
    success = tgw.Login(cfg, tgw.ApiMode.kColocationMode)
    if not success:
        print("login fail")
        exit(0)
except Exception as e:
    print(e)

root = './'
return_DF = True

# 回放快照
replay_cfg = tgw.ReplayCfg()
replay_cfg.begin_date = 20230519
replay_cfg.end_date = 20230519
replay_cfg.begin_time = 90000000
replay_cfg.end_time = 103100000
replay_cfg.task_id = tgw.GetTaskID()
replay_cfg.req_codes = [(tgw.MarketType.kSSE, "600000"), (tgw.MarketType.kSSE, "000001")]
replay_cfg.md_data_type = tgw.MDDatatype.kSnapshot
ret = tgw.ReplayRequest(replay_cfg, OnResponseSnapshot,return_df_format=return_DF)
if ret == tgw.ErrorCode.kSuccess:
    pass
else:
    print(tgw.GetErrorMsg(ret))


# 回放逐笔成交
replay_cfg = tgw.ReplayCfg()
replay_cfg.begin_date = 20230519
replay_cfg.end_date = 20230519
replay_cfg.begin_time = 90000000
replay_cfg.end_time = 103100000
replay_cfg.task_id = tgw.GetTaskID()
replay_cfg.req_codes = [(tgw.MarketType.kSSE, "600000"), (tgw.MarketType.kSSE, "501048")]
replay_cfg.md_data_type = tgw.MDDatatype.kTickExecution
ret = tgw.ReplayRequest(replay_cfg, OnResponseTickExec,return_df_format=return_DF)
if ret == tgw.ErrorCode.kSuccess:
    pass
else:
    print(tgw.GetErrorMsg(ret))


# 回放k线
replay_cfg = tgw.ReplayCfg()
replay_cfg.cq_flag = 0
replay_cfg.cyc_type = tgw.MDDatatype.k1KLine
replay_cfg.auto_complete = 1
replay_cfg.begin_date = 20230519
replay_cfg.end_date = 20230519
replay_cfg.begin_time = 930
replay_cfg.end_time = 1532
replay_cfg.task_id = tgw.GetTaskID()
replay_cfg.req_codes = [(tgw.MarketType.kSZSE, "000001"), (tgw.MarketType.kSSE, "600000")]
ret = tgw.ReplayKline(replay_cfg, OnResponseKline, return_df_format=return_DF)
if ret == tgw.ErrorCode.kSuccess:
    pass
else:
    print(tgw.GetErrorMsg(ret))


g_wait_event.wait()

#释放相关资源
tgw.Close()


