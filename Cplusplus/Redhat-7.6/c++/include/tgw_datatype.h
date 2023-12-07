#pragma once

#include <stdint.h>

namespace galaxy { namespace tgw {

/**
* @brief        数据长度定义
* @attention    托管机房模式和互联网模式适用
**/
class ConstField
{
public:
    static const uint32_t kIPMaxLen                      = 24;       // IP地址的最大长度
    static const uint32_t kUMSItemLen                    = 10;       // 服务项信息的最大个数
    static const uint32_t kUsernameLen                   = 32;       // 用户名的最大长度
    static const uint32_t kPasswordLen                   = 64;       // 用户名密码的最大长度    
    static const uint32_t kSecurityCodeLen               = 16;       // 证券代码最大长度
    static const uint32_t kHistorySecurityCodeLen        = 32;       // 历史回放和查询证券代码最大长度
    static const uint32_t kPushSecurityCodeLen           = 32;       // 实时推送证券代码最大长度
    static const uint32_t kSecurityNameLen               = 32;       // 证券名称最大长度
    static const uint32_t kTradingPhaseCodeLen           = 8;        // 交易状态标志
    static const uint32_t kExChangeInstIDLen             = 31;       // 合约在交易所代码
    static const uint32_t kPositionLevelLen              = 10;       // 行情档位
    static const uint32_t kMDStreamIDLen                 = 6;        // 行情类别
    static const uint32_t kSecurityStatusLen             = 24;       // 证券状态最大长度
    static const uint32_t kSecuritySymbolLen             = 32;       // 证券简称最大长度
    static const uint32_t kSecurityEnglishNameLen        = 128;      // 证券英文简称最大长度
    static const uint32_t kSecurityTypeLen               = 10;       // 证券类别长度
    static const uint32_t kCurrencyLen                   = 4;        // 币种长度
    static const uint32_t kVolumeTradeLen                = 24;       // 成交量长度
    static const uint32_t kValueTradeLen                 = 24;       // 交易额长度
    static const uint32_t kFutureSecurityCodeLen         = 32;       // 期货代码最大长度
    static const uint32_t kMDStreamIDMaxLen              = 6;        // 行情类别字段最大长度
    static const uint32_t kDataPermission                = 128;      // 数据权限最大长度
    static const uint32_t kTokenMaxLen                   = 128;      // token的最大长度
    static const uint32_t kQuerySecurityCodeLen          = 38;       // 查询状态回调代码最大长度
    static const uint32_t kTradingStatusLen              = 8;        // 证券交易状态档位
    static const uint32_t kSymbolLen                     = 128;      // 证券简称最大长度（包括中文简称）
    static const uint32_t kSecurityAbbreviationLen       = 64;       // 证券简称最大长度
    static const uint32_t kMaxTypesLen                   = 16;       // 证券类型最大长度
    static const uint32_t kTypesLen                      = 8;        // 
    static const uint32_t kCodeTableSecurityStatusMaxLen = 16;       // 代码表证券状态字符最大长度
    static const uint32_t RegularShare                   = 9;        // 对应回购标准券长度
    static const uint32_t kConsSecurityCodeLen           = 32;       // 成份证券代码长度
    static const uint32_t kSymbolETFLen                  = 128;      // 基金名称长度
    static const uint32_t KUnderlyingSecurityID          = 4;        // 成分股所属市场ID长度
    static const uint32_t KReserved                      = 30;       // 预留字段长度
    static const uint32_t kManagmentETFLen               = 128;      // 基金公司名称长度
    static const uint32_t KUnderlyingSecurityIDSource    = 4;        // 拟合指数代码源长度
    static const uint32_t AllCashAmount                  = 12;       // 全现金替代的总金额长度
    static const uint32_t AllCashAremiumRate             = 7;        // 全现金替代的申购溢价比例长度
    static const uint32_t AllCashDiscountRate            = 7;        // 全现金替代的赎回折价比例长度
    static const uint16_t DefaultMaxOBSubNum                    = 500;    //委托簿默认最大订阅数量
    static const uint16_t DefaultMaxOBSnapshotSubNum            = 3000;   //委托簿快照默认最大订阅数量
    static const uint16_t DefaultMaxOBOrderQueueSize            = 50;     //每一档委托队列数量上限
    static const uint16_t DefaultMaxOBEntrySize                 = 20;     //委托簿档位数量上限
    static const uint16_t DefaultMaxOBDeliverIntervalMs         = 50;     //委托簿最小推送间隔
    static const uint16_t DefaultMinOBSnapshotDeliverIntervalMs = 10;     //委托簿快照最小推送间隔
    static const uint32_t kDetailLen                    = 40;       // 港股经纪明细数组长度
    static const uint32_t kHKExOrderSnapshotLevelLen    = 20;       // 港股委托挂单买单序列档位长度
};

/**
* @brief        市场类型定义
* @attention    托管机房模式和互联网模式适用
**/
class MarketType
{
public:
    enum
    {
        kNone       = 0,            // 表示全市场  
        kNEEQ       = 2,            // 北交所
        kSHFE       = 3,            // 上期所 
        kCFFEX      = 4,            // 中金所
        kDCE        = 5,            // 大商所 
        kCZCE       = 6,            // 郑商所 
        kINE        = 7,            // 上海国际能源交易中心
        kSSE        = 101,          // 上交所 
        kSZSE       = 102,          // 深交所 
        kHKEx       = 103,          // 港交所 
        kBK         = 201,          // 板块
        kMax        = 255           // 市场类型最大值
    };
};

/**
* @brief        日志输出级别定义
* @attention    托管机房模式和互联网模式适用
**/
class LogLevel
{
public:
    enum
    {
        kTrace = 0, 
        kDebug = 1, 
        kInfo  = 2, 
        kWarn  = 3, 
        kError = 4, 
        kFatal = 5
    };
};

/**
* @brief        事件级别定义
* @attention    托管机房模式适用
**/
class EventLevel
{
public:
    enum
    {
        kInfo  = 1,             // 普通事件
        kWarn  = 2,             // 告警事件
        kError = 3              // 错误事件，比较严重，需要介入处理
    };
};

/**
* @brief        错误代码定义
* @attention    托管机房模式和互联网模式适用
**/
class ErrorCode
{
public:
    enum
    {
        kFailure                    = -100,  // 失败
        kUnInited                   = -99,   // 未初始化
        kNullSpi                    = -98,   // 空指针
        kParamIllegal               = -97,   // 参数非法
        kNetError                   = -96,   // 网络异常
        kPermissionError            = -95,   // 数据无权限
        kLogonFailed                = -94,   // 未登录
        kAllocateMemoryFailed       = -93,   // 分配内存失败
        kChannelError               = -92,   // 通道错误
        kOverLoad                   = -91,   // hqs任务队列溢出
        kLogoned                    = -90,   // 账号已登录
        kHqsError                   = -89,   // HQS系统错误
        kNonQueryTimePeriod         = -88,   // 非查询时间段(非查询时间段不支持查询)
        kDbAndCodeTableNoCode       = -87,   // 数据库和代码表中没有指定的代码
        kIllegalMode                = -86,   // api模式非法
        kThreadBusy                 = -85,   // 超过最大可用线程资源
        kParseDataError             = -84,   // 数据解析出错
        kTimeout                    = -83,   // 获取数据超时
        kFlowOverLimit              = -82,   // 周流量耗尽
        kCodeTableCacheNotAvailable = -81,   // 代码表缓存不可用
        kOverMaxSubLimit            = -80,   // 超过最大订阅限制
        kLostConnection             = -79,   // 丢失连接
        kOverMaxQueryLimit          = -78,   // 超过最大查询数（含代码表）
        kFunctionIdNull             = -77,   // 三方资讯查询未设置功能号
        kDataEmpty                  = -76,   // 数据为空
        kUserNotExist               = -75,   // 用户不存在
        kVerifyFailure              = -74,   // 账号/密码错误
        kApiInterfaceUsing          = -73,   // api接口不能同时多次调用
        kTaskIdRepeat               = -70,   // 任务id重复

        kSuccess                    = 0      // 成功
    };
};

/**
* @brief        事件代码定义
* @attention    托管机房模式适用
**/
class EventCode
{
public:
    enum
    {
        /*--------------------------与UMS会话层事件信息----------------------*/
        kUMSConnectSuccess                  = 1,            // 连接UMS成功
        kUMSConnectFailed,                                  // 连接UMS失败
        kUMSLogonSuccess,                                   // 登录UMS成功
        kUMSLogonFailed,                                    // 登录UMS失败
        kUMSHeartbeatTimeout,                               // 与UMS心跳超时

        /*------------------------TCP连接相关事件------------------------*/
        kChannelTCPInitSuccess,								// TCP方式开启成功
        kChannelTCPInitFailed,								// TCP方式开启失败
        kChannelTCPConnectSuccess,				            // TCP方式连接成功
        kChannelTCPConnectFailed,				            // TCP方式连接失败
        kChannelTCPLogonSuccess,				            // TCP方式登录成功
        kChannelTCPLogonFailed,								// TCP方式登录失败
        kChannelTCPSessionClosed,				            // TCP方式连接断开
        kChannelTCPHeartbeatTimeout,					    // TCP方式会话心跳失败

        /*------------------------AES 服务端委托薄相关事件-----------------*/
        kOrderBookRejonConnectFailed,                       //连接上游aes组件失败
        kIncompleteData,                                    // 服务端委托簿以recover 方式重启，数据有可能不完整
        kDerivedDataLogonSuccess,                           // 行情衍生数据服务端登陆成功
        kDerivedDataLogonFailed,                            // 行情衍生数据服务端登陆失败 
    };
};

/**
* @brief        API通道模式
* @attention    托管机房模式和互联网模式适用
**/
class ApiMode
{
public:
    static const uint16_t kColocationMode   = 1;     // 托管机房模式 
    static const uint16_t kInternetMode     = 2;     // 互联网模式
};

/**
* @brief        托管机房模式下的通道选择
* @attention    托管机房模式适用
**/
class ColocatChannelMode
{
public:
    static const uint64_t kTCP  = 0x0000000200000000;    // TCP推送 获取数据
    static const uint64_t kQTCP = 0x0000000800000000;    // TCP查询 获取数据
    static const uint64_t kRTCP = 0x0000001000000000;    // TCP回放 获取数据
};

/**
* @brief        订阅数据类型
* @attention    托管机房模式和互联网模式适用
**/
class SubscribeDataType
{
public:
    static const uint32_t kNone                 = 0;    // 订阅全部数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k1MinKline            = 1;    // 订阅1分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k3MinKline            = 2;    // 订阅3分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k5MinKline            = 3;    // 订阅5分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k10MinKline           = 4;    // 订阅10分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k15MinKline           = 5;    // 订阅15分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k30MinKline           = 6;    // 订阅30分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k60MinKline           = 7;    // 订阅60分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t k120MinKline          = 8;    // 订阅120分钟k线数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t kSnapshotDerive       = 9;    // 订阅快照衍生数据（适用模式：托管机房模式、互联网模式）
    static const uint32_t kSnapshot             = 10;   // 订阅现货快照数据（适用模式：互联网模式）
    static const uint32_t kOptionSnapshot       = 11;   // 订阅期权快照数据（适用模式：互联网模式）
    static const uint32_t kHKTSnapshot          = 12;   // 订阅港股快照数据（适用模式：互联网模式）
    static const uint32_t kIndexSnapshot        = 13;   // 订阅指数快照数据（适用模式：互联网模式）
    static const uint32_t kAfterHourFixedPriceSnapshot = 14;   // 订阅盘后快照数据（适用模式：互联网模式）
    static const uint32_t kCSIIndexSnapshot     = 15;   // 订阅中证指数数据（适用模式：互联网模式）
    static const uint32_t kCnIndexSnapshot      = 16;   // 订阅国证指数快照数据（适用模式：互联网模式）
    static const uint32_t kHKTRealtimeLimit     = 17;   // 订阅港股通实时额度数据（适用模式：互联网模式）
    static const uint32_t kHKTProductStatus     = 18;   // 订阅港股通产品状态数据（适用模式：互联网模式）
    static const uint32_t kHKTVCM               = 19;   // 订阅港股VCM数据（适用模式：互联网模式）
    static const uint32_t kFutureSnapshot       = 20;   // 订阅期货数据（适用模式：互联网模式）
};

/**
* @brief        数据类型
* @attention    托管机房模式和互联网模式适用
**/
class MDDatatype
{
public:
    enum
    {
        k1KLine                = 10000,       // 1分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        k3KLine                = 10001,       // 3分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        k5KLine                = 10002,       // 5分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        k10KLine               = 10003,       // 10分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        k15KLine               = 10004,       // 15分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        k30KLine               = 10005,       // 30分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        k60KLine               = 10006,       // 60分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        k120KLine              = 10007,       // 120分钟K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        kDayKline              = 10008,       // 日K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        kWeekKline             = 10009,       // 周K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        kMonthKline            = 10010,       // 月K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        kSeasonKline           = 10011,       // 季K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        kYearKline             = 10012,       // 年K线（适用模式：托管机房模式、互联网模式）（托管机房适用通道：查询通道、回放通道）
        kTickExecution         = 10013,       // 逐笔成交（适用模式：托管机房模式）（托管机房适用通道：回放通道）
        kSnapshot              = 10014        // 快照（适用模式：托管机房模式）（托管机房适用通道：回放通道，当前仅现货类型）
    };
};

/**
* @brief        品种类型定义
* @attention    托管机房模式和互联网模式适用
**/
class VarietyCategory {
public:
    static const uint8_t kNone                                 = 0;   // None,表示全品种
    static const uint8_t kStock                                = 1;   // 股票
    static const uint8_t kFund                                 = 2;   // 基金
    static const uint8_t kBond                                 = 3;   // 债券
    static const uint8_t kOption                               = 4;   // 期权
    static const uint8_t kIndex                                = 5;   // 指数
    static const uint8_t kHKT                                  = 6;   // 港股通
    static const uint8_t kFutureOption                         = 7;   // 期货期权
    static const uint8_t kCFETSRMB                             = 8;   // 银行间本币交易产品
    static const uint8_t kHKEx                                 = 9;   // 港股
    static const uint8_t kOthers                               = 255; // 其他
};

/**
* @brief        历史回放任务状态
* @attention    托管机房模式适用
**/
class HistoryTaskStatus 
{
public:
    static const int16_t kSuccess                               = 0;          // 任务成功完成
    static const int16_t kFailed                                = 1;          // 任务执行失败
    static const int16_t kTaskCancel                            = 2;          // 任务取消
    static const int16_t kTaskWaiting                           = 3;          // 任务执行中
    static const int16_t kTaskTimeOut                           = 4;          // 回放任务超时
};

/**
* @brief        托管机房账户数据权限
* @attention    托管机房模式适用
**/
class ColocationDataPermission
{
public:
    enum 
    {
        k1MinKline                      = 1,         // 1分钟k线权限
        k3MinKline                      = 2,         // 3分钟k线权限
        k5MinKline                      = 3,         // 5分钟k线权限
        k10MinKline                     = 4,         // 10分钟k线权限
        k15MinKline                     = 5,         // 15分钟k线权限
        k30MinKline                     = 6,         // 30分钟k线权限
        k60MinKline                     = 7,         // 60分钟k线权限
        k120MinKline                    = 8,         // 120分钟k线权限
        kDayKline                       = 9,         // 日k线权限
        kWeekKline                      = 10,        // 周k线权限
        kMonthKline                     = 11,        // 月k线权限
        kSeasonKline                    = 12,        // 季k线权限
        kYearKline                      = 13,        // 年k线权限
        kSnapshotDerive                 = 14,        // 现货衍生快照
        kTick                           = 15,        // 逐笔（逐笔成交+逐笔委托）
        kOrderQueue                     = 16,        // 委托队列
        kStockSnapshotL2                = 17,        // 现货L2快照
        kIndexSnapshotL2                = 18,        // 指数L2快照
        kOptionSnapshot                 = 19,        // 期权快照
        kHKTSnapshot                    = 20,        // 港股快照
        kFutureTickL1                   = 21,        // 期货L1快照
        kFutureTickL2                   = 22,        // 期货L2快照
        kCodeTable                      = 23,        // 证券代码表权限
        kSecurityInfo                   = 24,        // 证券基本信息权限
        kExFactorTable                  = 25,        // 复权因子表
        kStockSnapshotL1                = 26,        // 现货L1快照(目前仅包含北交所)
        kIndexSnapshotL1                = 27,        // 指数L1快照(目前仅包含北交所)
    };
};

/**
* @brief        互联网账户数据权限
* @attention    互联网模式适用
**/
class InternetDataPermission
{
public:
    enum 
    {
        kSnapshotDerive                 = 2,          // 衍生数据权限
        kStockSnapshot                  = 3,          // 现货快照相关权限(含北交所现货)
        kIndexSnapshot                  = 4,          // 指数快照相关(含国证指数及北交所指数)权限
        kHKTSnapshot                    = 6,          // 港股通(港股通快照，产品状态，实时额度，VCM)相关权限
        kOptionSnapshot                 = 7,          // 期权权限
        kFutureSnapshot                 = 11,         // 期货权限
        kCSIIndexSnapshot               = 12,         // 中证指数权限
        kAfterHourFixedPriceSnapshot    = 13,         // 盘后定价行情快照相关权限
        k1MinKline                      = 16,         // 1分钟k线权限
        k3MinKline                      = 17,         // 3分钟k线权限
        k5MinKline                      = 18,         // 5分钟k线权限
        k10MinKline                     = 19,         // 10分钟k线权限
        k15MinKline                     = 20,         // 15分钟k线权限
        k30MinKline                     = 21,         // 30分钟k线权限
        k60MinKline                     = 22,         // 60分钟k线权限
        k120MinKline                    = 23,         // 120分钟k线权限
        kDayKline                       = 24,         // 日k线权限
        kWeekKline                      = 25,         // 周k线权限
        kMonthKline                     = 26,         // 月k线权限
        kSeasonKline                    = 27,         // 季k线权限
        kYearKline                      = 28,         // 年k线权限
        kHKExSnapshot                   = 29,         // 港股商业行情快照（港股商业股票、指数快照、经纪商数据、港股商业委托挂单）
        kHKExTickExcution               = 30,         // 港股商业行情逐笔
        kExFactor                       = 31,         // 复权因子权限
        kCodeTable                      = 32,         // 证券代码表权限
        kSecurityInfo                   = 33          // 证券基本信息权限(含etf的的权限)
    };
};

//委托簿数据类型
class SubscribeOrderBookDataType
{
public:
    static const uint64_t kNone                 = 0x000000000000;   // 订阅全部委托簿数据类型(kOrderBook,kOrderBookSnapshot)
    static const uint64_t kOrderBook            = 0x000000000001;   // 订阅委托簿数据
    static const uint64_t kOrderBookSnapshot    = 0x000000000002;   // 订阅委托簿快照数据
};

class OrderBookType {
public:
    /**
     * @brief 委托簿构建类型定义
     */
    static const uint8_t kNone                  = 0;   // 不开启委托簿
    static const uint8_t kServerOrderBook       = 2;   // 服务端远程TCP方式推送委托簿数据
};

class SubscribeType
{
public:
    enum
    {
        kSet,                                          // 重新设置订阅(先取消所有旧订阅信息, 然后增加新订阅信息)
        kAdd,                                          // 增加订阅
        kDel,                                          // 删除订阅
        kCancelAll                                     // 取消所有订阅
    };
};

class SubscribeDerivedDataType
{
public:
    static const uint32_t kOrderBook            = 1;    // 订阅委托簿数据
    static const uint32_t kOrderBookSnapshot    = 2;    // 订阅委托簿快照数据
};

}; // end of tgw
}; // end of galaxy
