
#pragma once
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include "tgw_datatype.h"

#pragma pack(push)
#pragma pack(1)

namespace galaxy { namespace tgw {

/**
* @brief 托管机房模式配置
**/
struct ColocaCfg
{
    //--------------------------------全局配置信息----------------------------------------------------
    uint64_t    channel_mode;              // 通道模式的集合，请参考 ChannelMode，该配置为各通道模式的集合

    //-------------------------------QTCP查询通道配置-------------------------------------------------
    uint16_t    qtcp_channel_thread;       // tcp查询通道数据消费线程数，默认开启2个线程
    uint16_t    qtcp_req_time_out;         // tcp查询通道数据请求检查超时时间(单位为分钟)，默认为10分钟
    uint16_t    qtcp_max_req_cnt;          // tcp查询通道实时请求最大数，默认1000

    //-------------------------------委托簿配置------------------------------------------------------
    uint8_t     enable_order_book;                                  // 0: 不启用委托簿, 2：服务端主动推送委托簿数据
    uint16_t    entry_size;                                         // 委托簿档位
    uint8_t     order_queue_size;                                   // 每个价位委托揭示笔数,最高50
    uint32_t    order_book_deliver_interval_microsecond;            // 委托簿递交时间间隔(微秒级)
    ColocaCfg()
    {
        qtcp_channel_thread = 3;
        qtcp_req_time_out = 10;
        qtcp_max_req_cnt = 1000;
        enable_order_book = OrderBookType::kNone;
        entry_size        = 10;
        order_queue_size  = 0;
        order_book_deliver_interval_microsecond = 0;
    }
};

/**
* @brief        API配置
* @attention    托管机房模式和互联网模式共用结构
**/
struct Cfg
{
    //-------------------------------Nginx 虚拟ip地址，port端口配置------------------------------------
    char        server_vip[ConstField::kIPMaxLen];      // 虚拟ip地址
    uint16_t    server_port;                       	    // 虚拟端口
    //-------------------------------用户名和密码配置--------------------------------------------------
    char        username[ConstField::kUsernameLen];     // 用户名
    char        password[ConstField::kPasswordLen];     // 用户密码, 明文填入，密文使用

    ColocaCfg   coloca_cfg;     // 托管机房配置（此配置在选择托管机房模式才能生效）
};

/**
* @brief 修改密码接口
**/
struct UpdatePassWordReq
{
    char username[ConstField::kUsernameLen];          // 用户名
    char old_password[ConstField::kPasswordLen];      // 用户旧密码
    char new_password[ConstField::kPasswordLen];      // 用户新密码
};

/**
* @brief        订阅或取消订阅数据项定义
* @attention    托管机房模式和互联网模式共用结构
**/
struct SubscribeItem
{
    uint8_t market;                                                // 市场类型，参考 MarketType, 为0表示订阅所有支持的市场
    uint64_t flag;                                                 // 各数据类型的集合，为0表示订阅所有支持的数据类型,参tgw_datatype.h中的SubscribeDataType
    char security_code[ConstField::kFutureSecurityCodeLen];        // 证券代码，为空表示订阅所有代码
    uint8_t category_type;                                         // 品种类别，参考 VarietyCategory, 为0表示订阅所有支持的品种，仅该参数仅互联网有效
};

/**
* @brief        加工因子订阅数据项定义
* @attention    支持全订阅，全订阅时，入参需设置为 "all"，仅支持以下全订阅方式："all all all"、"xxx all all"、"xxx xxx all"、"xxx xxx xxx"
*               托管机房模式和互联网模式共用结构
**/
struct SubFactorItem
{
    char factor_type[64];              // 因子父类型(英文)
    char factor_sub_type[64];          // 因子子类型(英文)
    char factor_name[64];			   // 因子名称(英文)
    char security_code[32];            // 证券代码
    uint16_t market;                   // 市场类型
    uint16_t category;                 // 品种类别
    SubFactorItem()
    {
        strncpy(security_code, "*", 32);
        market = 0;
        category = 0;
    }
};

/**
 * @name 订阅委托簿数据项定义
 * @{ */
struct SubscribeOrderBookItem
{
    int32_t market;                                     // 市场类型,参考 MarketType, 委托簿支持市场范围[kSSE/kSZSE],其余市场暂时不支持
    uint64_t flag;                                      // 各数据类型的集合,参考 SubscribeOrderBookDataType
    char security_code[ConstField::kSecurityCodeLen];   // 证券代码,仅支持单独订阅代码,订阅代码不能为空(服务端委托簿订阅有上限设置,订阅代码总数超过上限会导致订阅失败)
};
/**  @} */

/**
 * @name 订阅行情衍生数据项定义
 * @{ */
struct SubscribeDerivedDataItem
{
    int32_t market;                                     // 市场类型,参考 MarketType, 行情衍生数据支持市场范围[kSSE/kSZSE],其余市场暂时不支持
    char security_code[ConstField::kSecurityCodeLen];   // 证券代码(注意:不支持代码为空)
};
/**  @} */

/**
* @brief        K线查询 接口默认请求参数
* @attention    托管机房模式和互联网模式共用结构
**/
struct ReqKline 
{
    char security_code[ConstField::kQuerySecurityCodeLen];            // 证券代码
    uint8_t market_type;                                              // 市场类型
    uint8_t cq_flag;                                                  // 除权标志（0:不复权;1:向前复权;2:向后复权; 默认0）
    uint32_t cq_date;                                                 // 除权日期（yyyMMdd）（暂不支持）
    uint32_t qj_flag;                                                 // 全价标志（债券）（0：净价，1：全价）（暂不支持）
    uint16_t cyc_type;                                                // 数据周期（参考tgw_datatype.h中的MDDatatype描述）
    uint32_t cyc_def;                                                 // 周期数量（暂不支持）
    uint8_t auto_complete;                                            // 自动补全（0:不补齐，1：补齐 默1）
    uint32_t begin_date;                                              // 开始日期（yyyyMMdd）
    uint32_t end_date;                                                // 结束日期（yyyyMMdd）
    uint32_t begin_time;                                              // 开始时间（默认：HHmm， 支持HHmmssSSS）
    uint32_t end_time;                                                // 结束时间（默认：HHmm， 支持HHmmssSSS）
    ReqKline()
    {
        cq_flag = 0;
        auto_complete = 1;
    }
};

/** 
* @brief        查询 快照请求参数
* @attention    托管机房模式和互联网模式共用结构
**/
struct ReqDefault 
{
    char security_code[ConstField::kQuerySecurityCodeLen];  // 证券代码
    uint8_t market_type;                                    // 市场类型
    uint32_t date;                                          // 日期（必须为yyyyMMdd）
    //************************************开始时间、结束时间 取值说明***************************************************************
    // 毫秒(HHmmssSSS)查询，开始时间和结束时间需同时为HHmmssSSS;
    // 示例如下：
    // 开始（结束）时间HHmmssSSS输入示例：930（表示0点0分0秒930毫秒）、1031（表示0点0分1秒31毫秒）
    // 93000000（表示9点30分0秒0毫秒）、103001100（表示10点30分1秒100毫秒）
    uint32_t begin_time;                                    // 开始时间（HHmmssSSS）
    uint32_t end_time;                                      // 结束时间（HHmmssSSS）
    uint16_t data_type;                                     // (该字段仅在QuerySnapshot接口调用生效)默认0标识快照，1标识香港市场委托挂单，2标识经纪商席位数据，其它数字无效
};

/**
* @brief        历史回放请求item
* @attention    仅托管机房适用结构
**/
struct ReqHistoryItem
{
    uint8_t market;                                             // 市场类型，参考 MarketType
    char security_code[ConstField::kHistorySecurityCodeLen];    // 证券代码，代码不能为空
};

/**
* @brief        查询 代码表查询请求结构
* @attention    托管机房模式和互联网模式共用结构
**/
struct SubCodeTableItem
{
    int32_t market;                                                     // 市场类型,参考 MarketType, 为kNone表示查询所有支持的市场(代码表目前只支持上交所、深交所与北交所)
    char security_code[ConstField::kFutureSecurityCodeLen];             // 证券代码,为空表示查询所有代码
};

/**
* @brief        查询 加工因子请求参数
* @attention    托管机房模式和互联网模式共用结构
**/
struct ReqFactor
{
    int64_t task_id;                   // 任务id，对应GetTaskID接口产生的唯一id
    char     factor_type[64];          // 因子父类型(英文)
    char     factor_sub_type[64];      // 因子子类型(英文)
    char     factor_name[64];		   // 因子名称(英文)
    uint32_t begin_date;               // 开始日期（yyyyMMdd）
    uint32_t end_date;                 // 结束日期（yyyyMMdd）
    uint32_t begin_time;               // 开始时间（HHmmssSSS）
    uint32_t end_time;                 // 结束时间（HHmmssSSS）
    char security_code[32];            // 证券代码（为空表示查旧表，为*表示新表全代码，其他正常按照代码下发）
    uint16_t market;                   // 市场类型
    uint16_t category;                 // 品种类别
    int32_t count;                    // 默认1000
    char     key1[64];                 // 预留字段key1
    char     key2[64];                 // 预留字段key2
    ReqFactor()
    {
        count = 1000;
    }
};

/**
* @brief        回放 k线请求数据
* @attention    仅托管机房适用结构
**/
struct ReqReplayKline 
{
    uint8_t cq_flag;                                         // 除权标志（0:不复权;1:向前复权;2:向后复权; 默认0）
    uint32_t cq_date;                                        // 除权日期（yyyMMdd）
    uint32_t qj_flag;                                        // 全价标志（债券）（0：净价，1：全价）
    uint16_t cyc_type;                                       // 数据周期，参照tgw_datatype.h中的MDDatatype（不支持周月季年k）
    uint32_t cyc_def;                                        // 周期数量（暂不使用）
    uint8_t auto_complete;                                   // 自动补全（0:不补齐，1：补齐 默1）
    uint32_t begin_date;                                     // 开始日期（yyyyMMdd）
    uint32_t end_date;                                       // 结束日期（yyyyMMdd）
    uint32_t begin_time;                                     // 开始时间（HHmm）
    uint32_t end_time;                                       // 结束时间（HHmm）
    uint16_t replay_speed;                                   // 返回倍速（暂不可用）
    int64_t task_id;                             			 // 任务id(任务编号，例如:1) 调用GetTaskId获取
    ReqHistoryItem* req_items;                               // 请求数组item头指针,不得为空
    uint32_t req_item_cnt;                                   // 请求回放代码数量
    ReqReplayKline()
    {
        cq_flag = 0;
        auto_complete = 1;
        replay_speed = 0;
    }
};

/**
* @brief        回放 逐笔成交、现货快照
* @attention    仅托管机房适用结构
**/
struct ReqReplay 
{
    uint16_t md_data_type;                                   // 回放数据类型,参照tgw_datatype.h中的MDDatatype
    uint32_t begin_date;                                     // 开始日期（yyyyMMdd）
    uint32_t end_date;                                       // 结束日期（yyyyMMdd）
    uint32_t begin_time;                                     // 开始时间（HHmmssSSS）
    uint32_t end_time;                                       // 结束时间（HHmmssSSS）
    uint16_t replay_speed;                                   // 返回倍速（暂不可用）
    int64_t task_id;                             			 // 任务id(任务编号，例如:1) 调用GetTaskId获取
    ReqHistoryItem* req_items;                               // 请求数组item头指针,不得为空
    uint32_t req_item_cnt;                                   // 请求回放代码数量
}; 

/**
 * @brief        登陆成功时返回数据信息
 * @attention    托管机房模式和互联网模式共用结构
 **/
struct LogonResponse
{
    uint16_t api_mode;       // 1：托管机房  2：互联网
    uint32_t logon_msg_len;  // 登录返回信息长度
    char* logon_json;        // 登录返回信息，格式为json
};

/**
 * @brief       数据推送、查询、回放 K线数据信息结构定义
 * @attention   托管机房模式和互联网模式共用结构
 **/
struct MDKLine
{
    uint8_t market_type;                                    // 市场类型
    char security_code[ConstField::kPushSecurityCodeLen];   // 证券代码
    int64_t orig_time;                                      // 时间（YYYYMMDDHHMMSSsss)
    int64_t kline_time;                                     // k线时间
    int64_t open_price;                                     // 开盘价，实际值需除以1000000
    int64_t high_price;                                     // 最高价，实际值需除以1000000
    int64_t low_price;                                      // 最低价，实际值需除以1000000
    int64_t close_price;                                    // 最新价，实际值需除以1000000
    int64_t volume_trade;                                   // 成交量，无倍数放大
    int64_t value_trade;                                    // 成交金额，无倍数放大
    uint8_t variety_category;                               // 品种类别
};

/**
 * @brief       现货衍生数据
 * @attention   托管机房模式和互联网模式共用结构
 **/
struct MDSnapshotDerive
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 证券代码
    int64_t orig_time;                                                // 时间（为YYYYMMDDHHMMSSsss）
    uint64_t average_price;                                           // 均价，实际值需除以1000000
    uint64_t circulation_value;                                       // 流通市值，实际值需除以1000000
    uint64_t total_value;                                             // 总市值，实际值需除以1000000
    uint64_t initiative_buy_volume;                                   // 外盘，实际值需除以100
    uint64_t initiative_sell_volume;                                  // 内盘，实际值需除以100
    uint32_t turnover_rate;                                           // 换手率，实际值需除以100000
    int32_t volume_ratio;                                             // 量比，实际值需除以100000
    int32_t ask_bid_ratio;                                            // 委比，实际值需除以100000
    uint32_t amplitude;                                               // 振幅，实际值需除以100000
    int32_t PE_static;                                                // 静态市盈率，实际值需除以100
    int32_t PE_dynamic;                                               // 动态市盈率，实际值需除以100
    int32_t PE_TTM;                                                   // 最近4季度滚动市盈率，实际值需除以100
    int32_t PB;                                                       // 市净率，实际值需除以100
    int64_t entrustment_diff;                                         // 委差
    char initiative_flag;                                             // 内外盘标记(B/S)
    uint8_t variety_category;                                         // 品种类别
};

/**
 * @brief       加工因子数据结构
 * @attention   托管机房模式和互联网模式共用结构
 **/
struct Factor
{
    uint32_t data_size;     // json数据的大小
    char* json_buf;         // json结构
};

/**
 * @brief       快照数据
 * @attention   互联网模式结构
 **/
struct MDSnapshotL1
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 证券代码
    uint8_t variety_category;                                         // 品种类别（参照描述）
    int64_t orig_time;                                                // 交易所行情数据时间（YYYYMMDDHHMMSSsss）
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];     // 交易阶段代码
    //************************************上海现货行情交易状态***************************************************************
    //该字段为8位字符数组,左起每位表示特定的含义,无定义则填空格。
    //第0位:‘S’表示启动(开市前)时段,‘C’表示集合竞价时段,‘T’表示连续交易时段,
    //‘E’表示闭市时段 ,‘P’表示临时停牌,
    //‘M’表示可恢复交易的熔断(盘中集合竞价),‘N’表示不可恢复交易的熔断(暂停交易至闭市)
    //‘U’表示收盘集合竞价
    //第1位:‘0’表示此产品不可正常交易,‘1’表示此产品可正常交易。
    //第2位:‘0’表示未上市,‘1’表示已上市
    //第3位:‘0’表示此产品在当前时段不接受进行新订单申报,‘1’ 表示此产品在当前时段可接受进行新订单申报。

    //************************************深圳现货行情交易状态***************************************************************
    //第 0位:‘S’= 启动(开市前)‘O’= 开盘集合竞价‘T’= 连续竞价‘B’= 休市‘C’= 收盘集合竞价‘E’= 已闭市‘H’= 临时停牌‘A’= 盘后交易‘V’=波动性中断
    //第 1位:‘0’= 正常状态 ‘1’= 全天停牌

    //************************************北交所行情交易状态***************************************************************
    //个位数存放收市行情标志(0:非收市行情;1:收市行情;2:盘后行情)
    //十位数存放正式行情与测试行情标志(0:正式行情;1:测试行情)

    //************************************港股股票行情交易状态***************************************************************
    // ‘1’表示正常交易，‘2’表示停牌，‘3’表示复牌
    int64_t pre_close_price;                                          // 昨收价，实际值需除以1000000
    int64_t open_price;                                               // 开盘价，实际值需除以1000000
    int64_t high_price;                                               // 最高价，实际值需除以1000000
    int64_t low_price;                                                // 最低价，实际值需除以1000000
    int64_t last_price;                                               // 最新价，实际值需除以1000000
    int64_t close_price;                                              // 收盘价，实际值需除以1000000（北交所为0）
    int64_t bid_price[ConstField::kPositionLevelLen];                 // 申买价，实际值需除以1000000
    int64_t bid_volume[ConstField::kPositionLevelLen];                // 申买量，实际值需除以100
    int64_t offer_price[ConstField::kPositionLevelLen];               // 申卖价，实际值需除以1000000
    int64_t offer_volume[ConstField::kPositionLevelLen];              // 申卖量，实际值需除以100
    int64_t num_trades;                                               // 成交笔数
    int64_t total_volume_trade;                                       // 成交总量，实际值需除以100
    int64_t total_value_trade;                                        // 成交总金额，实际值需除以100000
    int64_t IOPV;                                                     // IOPV净值估产（仅基金品种有效），实际值需除以1000000，北交所为0
    int64_t high_limited;                                             // 涨停价，实际值需除以1000000
    int64_t low_limited;                                              // 跌停价，实际值需除以1000000
};

/** 
 * @brief       指数快照数据结构
 * @attention   托管机房模式和互联网模式共用结构
 **/
struct MDIndexSnapshot
{
    uint8_t market_type;                                        // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];        // 证券代码
    int64_t orig_time;                                          // 交易所行情数据时间（YYYYMMDDHHMMSSsss)
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];// 产品实时阶段及标志（深圳,港股有效）
    //************************************深圳指数快照交易状态***************************************************************
    //第 0位：‘S’= 启动（开市前）‘O’= 开盘集合竞价‘T’= 连续竞价‘B’= 休市‘C’= 收盘集合竞价‘E’= 已闭市‘H’= 临时停牌‘A’= 盘后交易‘V’=波动性中断
    //第 1位：‘0’= 正常状态 ‘1’= 全天停牌
    //************************************港股指数快照交易状态***************************************************************
    //'C'=收市价 'I'=Indicative指示 'O'=指数开盘 'P'=昨收价格 'R'=预备开盘 'S'=止损指数 'T'=指数现价
    int64_t pre_close_index;                                    // 前收盘指数N18(6)，实际值需除以1000000
    int64_t open_index;                                         // 今开盘指数N18(6)，实际值需除以1000000
    int64_t high_index;                                         // 最高指数N18(6)，实际值需除以1000000
    int64_t low_index;                                          // 最低指数N18(6)，实际值需除以1000000
    int64_t last_index;                                         // 最新指数N18(6)，实际值需除以1000000
    int64_t close_index;                                        // 收盘指数（仅上海有效），实际值需除以1000000
    int64_t total_volume_trade;                                 // 参与计算相应指数的交易数量N18(2)，实际值需除以100(上交所:手, 深交所:张)
    int64_t total_value_trade;                                  // 参与计算相应指数的成交金额N18(2)，实际值需除以100000
    uint8_t variety_category;                                   // 品种类别
};

/** 
 * @brief       期权快照数据结构
 * @attention   托管机房模式和互联网模式共用结构
 **/
struct MDOptionSnapshot
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 期权代码
    int64_t orig_time;                                                // 交易所行情数据时间（YYYYMMDDHHMMSSsss)
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];     // 产品实时阶段及标志
    int64_t total_long_position;                                      // 总持仓量，实际值需除以100
    int64_t total_volume_trade;                                       // 总成交数，实际值需除以100
    int64_t total_value_trade;                                        // 总成交额，实际值需除以100000
    int64_t pre_settle_price;                                         // 昨结算价（仅上海有效），实际值需除以1000000
    int64_t pre_close_price;                                          // 昨收盘价，实际值需除以1000000
    int64_t open_price;                                               // 今开盘价，实际值需除以1000000
    int64_t auction_price;                                            // 动态参考价 (波动性中断参考价,仅上海有效)，实际值需除以1000000
    int64_t auction_volume;                                           // 虚拟匹配数量(仅上海有效)，实际值需除以100
    int64_t high_price;                                               // 最高价，实际值需除以1000000
    int64_t low_price;                                                // 最低价，实际值需除以1000000
    int64_t last_price;                                               // 最新价，实际值需除以1000000
    int64_t close_price;                                              // 今收盘价，实际值需除以1000000
    int64_t high_limited;                                             // 涨停价，实际值需除以1000000
    int64_t low_limited;                                              // 跌停价，实际值需除以1000000
    int64_t bid_price[5];                                             // 申买价，实际值需除以1000000
    int64_t bid_volume[5];                                            // 申买量，实际值需除以100
    int64_t offer_price[5];                                           // 申卖价，实际值需除以1000000
    int64_t offer_volume[5];                                          // 申卖量，实际值需除以100
    int64_t settle_price;                                             // 今日结算价（仅上海有效），实际值需除以1000000
    int64_t ref_price;                                                // 参考价(仅深圳有效)，实际值需除以1000000
    char    contract_type;                                            // 合约类别
    int32_t expire_date;                                              // 到期日
    char    underlying_security_code[ConstField::kSecurityCodeLen];   // 标的代码
    int64_t exercise_price;                                           // 行权价，实际值需除以1000000
    uint8_t variety_category;                                         // 品种类别
};

/**
 * @brief       港股通快照数据结构
 * @attention   托管机房模式和互联网模式共用结构
 **/
struct MDHKTSnapshot
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 港股代码
    int64_t orig_time;                                                // 交易所行情数据时间（YYYYMMDDHHMMSSsss)
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];     // 产品实时阶段及标志
    int64_t total_volume_trade;                                       // 总成交数，实际值需除以100
    int64_t total_value_trade;                                        // 总成交额，实际值需除以100000
    int64_t pre_close_price;                                          // 昨收价，实际值需除以1000000
    int64_t nominal_price;                                            // 按盘价，实际值需除以1000000
    int64_t high_price;                                               // 最高价，实际值需除以1000000
    int64_t low_price;                                                // 最低价，实际值需除以1000000
    int64_t last_price;                                               // 最新价，实际值需除以1000000
    int64_t bid_price[5];                                             // 申买价,(正常情况下为一档，集中竞价阶段可能有两档)实际值需除以1000000
    int64_t bid_volume[5];                                            // 申买量,(正常情况下为一档，集中竞价阶段可能有两档)实际值需除以100
    int64_t offer_price[5];                                           // 申卖价,(正常情况下为一档，集中竞价阶段可能有两档)实际值需除以1000000
    int64_t offer_volume[5];                                          // 申买量,(正常情况下为一档，集中竞价阶段可能有两档)实际值需除以100
    int64_t ref_price;                                                // 参考价
    int64_t high_limited;                                             // 冷静期价格上限
    int64_t low_limited;                                              // 冷静期价格下限
    int64_t bid_price_limit_up;                                       // 买盘上限价，实际值需除以1000000  （仅深圳有效）
    int64_t bid_price_limit_down;                                     // 买盘下限价，实际值需除以1000000  （仅深圳有效）
    int64_t offer_price_limit_up;                                     // 卖盘上限价，实际值需除以1000000  （仅深圳有效）
    int64_t offer_price_limit_down;                                   // 卖盘下限价，实际值需除以1000000  （仅深圳有效）
    uint8_t variety_category;                                         // 品种类别
};

/**
 * @brief       期货快照数据结构
 * @attention   托管机房模式和互联网共用结构
 **/
struct MDFutureSnapshot
{
    uint8_t market_type;                                                    // 市场类型
    char security_code[ConstField::kFutureSecurityCodeLen];                 // 合约代码
    int64_t orig_time;                                                      // 交易日 YYYYMMDDHHMMSSsss(ActionDay + UpdateTime + UpdateMillisec)
    int32_t action_day;                                                     // 业务日期
    int64_t last_price;                                                     // 最新价，实际值需除以1000000
    int64_t pre_settle_price;                                               // 上次结算价，实际值需除以1000000
    int64_t pre_close_price;                                                // 昨收价，实际值需除以1000000
    int64_t pre_open_interest;                                              // 昨持仓量，实际值需除以100
    int64_t open_price;                                                     // 开盘价，实际值需除以1000000
    int64_t high_price;                                                     // 最高价，实际值需除以1000000
    int64_t low_price;                                                      // 最低价，实际值需除以1000000
    int64_t total_volume_trade;                                             // 数量，实际值需除以100
    int64_t total_value_trade;                                              // 总成交金额，实际值需除以100000
    int64_t open_interest;                                                  // 持仓量，实际值需除以100
    int64_t close_price;                                                    // 今收盘，实际值需除以1000000
    int64_t settle_price;                                                   // 本次结算价，实际值需除以1000000
    int64_t high_limited;                                                   // 涨停板价，实际值需除以1000000
    int64_t low_limited;                                                    // 跌停板价，实际值需除以1000000
    int64_t pre_delta;                                                      // 昨虚实度，实际值需除以1000000
    int64_t curr_delta;                                                     // 今虚实度，实际值需除以1000000
    int64_t bid_price[5];                                                   // 申买价，实际值需除以1000000
    int64_t bid_volume[5];                                                  // 申买量，实际值需除以100
    int64_t offer_price[5];                                                 // 申卖价，实际值需除以1000000
    int64_t offer_volume[5];                                                // 申卖量，实际值需除以100
    int64_t average_price;                                                  // 当日均价，实际值需除以1000000
    int32_t trading_day;                                                    // 交易日期
    uint8_t variety_category;                                               // 品种类别
    int64_t latest_volume_trade;                                            // 最新成交量，实际值需除以100
    int64_t init_volume_trade;                                              // 初始持仓量，实际值需除以100
    int64_t change_volume_trade;                                            // 持仓量变化，实际值需除以100
    int64_t bid_imply_volume;                                               // 申买推导量，实际值需除以100
    int64_t offer_imply_volume;                                             // 申卖推导量，实际值需除以100
    int64_t total_bid_volume_trade;                                         // 总买入量，实际值需除以100
    int64_t total_ask_volume_trade;                                         // 总卖出量，实际值需除以100
    char exchange_inst_id[ConstField::kExChangeInstIDLen];                  // 合约在交易所的代码
};

/**
* @brief       港股买卖序列结构
* @attention   托管机房模式和互联网共用结构
**/
struct MDHKExListItem
{
    int64_t order_price;                  // 挂单价格，实际值需除以1000000
    int64_t order_volume;                 // 挂单数量，实际值需除以100
    int64_t num_of_orders;                // 挂单经纪席位数目
};

/**
* @brief       执行动作结构
* @attention   托管机房模式和互联网共用结构
**/
struct MDHKExOperation
{
    char operation_type[10];       // 操作类型，值为add/mod/del其中一个，约定长度为10
    int64_t order_id;              // 委托id
    char side;                     // 买卖方向，B买，S卖
    uint8_t order_type;		       // 仅add操作类型有效，'1'市价，'2'限价
    int64_t order_price;           // 仅add操作类型有效，委托价格，数值=真实值*1000
    int64_t order_volume;          // add,mod操作类型有效，单位为股
};

/**
* @brief       商业港股委托挂单结构
* @attention   托管机房模式和互联网共用结构
**/
struct MDHKExOrderSnapshot
{
    uint8_t market_type;                                                    // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];                    // 证券代码
    int64_t orig_time;                                                      // 时间（为YYYYMMDDHHMMSSsss）
    MDHKExOperation operation;												// 执行动作
    MDHKExListItem bid_list[ConstField::kHKExOrderSnapshotLevelLen];        // 买单序列 (20档)
    MDHKExListItem ask_list[ConstField::kHKExOrderSnapshotLevelLen];        // 卖单序列 (20档)
};

/**
* @brief       商业港股买卖经纪席位结构
* @attention   托管机房模式和互联网共用结构
**/
struct MDHKExDetailItem
{
    uint8_t     level;                                                      // 档位信息
    uint16_t    broker_num;                                                 // 席位号
};

/**
* @brief       商业港股经纪商席位数据结构
* @attention   托管机房模式和互联网共用结构
**/
struct MDHKExOrderBrokerSnapshot
{
    uint8_t market_type;                                                    // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];                    // 证券代码
    int64_t orig_time;                                                      // 时间（为YYYYMMDDHHMMSSsss）
    uint8_t side;                                                           // 买卖方向 'B' 买， 'S' 卖
    char    broker_flag;                                                    // 是否还有未展示完的席位排位 Y-是 N-否
    MDHKExDetailItem  detail[ConstField::kDetailLen];                       // 买卖经纪席位明细 所有档位的席位号之和最多有40个
};

/** 
 * @brief       盘后定价交易快照数据结构
 * @attention   互联网模式结构
 **/
struct MDAfterHourFixedPriceSnapshot
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 证券代码
    uint8_t variety_category;                                         // 品种类别
    int64_t orig_time;                                                // 交易所行情数据时间（为YYYYMMDDHHMMSSsss）
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];     // 交易阶段代码
    int64_t close_price;                                              // 今日收盘价（仅上海有效），实际值需除以1000000
    int64_t bid_price;                                                // 申买价，实际值需除以1000000
    int64_t bid_volume;                                               // 申买量，实际值需除以100
    int64_t offer_price;                                              // 申卖价，实际值需除以1000000
    int64_t offer_volume;                                             // 申卖量，实际值需除以100
    int64_t pre_close_price;                                          // 昨收价，实际值需除以1000000
    int64_t num_trades;                                               // 成交笔数
    int64_t total_volume_trade;                                       // 成交总量，实际值需除以100
    int64_t total_value_trade;                                        // 成交总金额，实际值需除以100000
};

/** 
 * @brief       中证指数行情数据结构
 * @attention   互联网模式结构
 **/
struct MDCSIIndexSnapshot
{
    uint8_t market_type;                                              // 市场类型
    uint8_t index_market;                                             // 指数市场
    char    security_code[ConstField::kSecurityCodeLen];              // 证券代码
    int64_t orig_time;                                                // 交易所行情数据时间（YYYYMMDDHHMMSSsss)
    int64_t last_index;                                               // 最新指数N11(4)，实际值需除以1000000
    int64_t open_index;                                               // 今开盘指数N11(4)，实际值需除以1000000
    int64_t high_index;                                               // 最高指数N11(4)，实际值需除以1000000
    int64_t low_index;                                                // 最低指数N11(4)，实际值需除以1000000
    int64_t close_index;                                              // 收盘指数，实际值需除以1000000
    int64_t pre_close_index;                                          // 前收盘指数N11(4)，实际值需除以1000000
    int64_t change;                                                   // 涨跌N11(4)，实际值需除以1000000
    int64_t ratio_of_change;                                          // 涨跌幅N11(4)，实际值需除以1000000
    int64_t total_volume_trade;                                       // 成交量N11(4)，实际值需除以100
    int64_t total_value_trade;                                        // 成交金额N16(5)，实际值需除以100000 (单位为万元)
    int64_t exchange_rate;                                            // 汇率N12(8)，实际值需除以100000000
    char    currency_symbol;                                          // 币种标志（0-人民币 1-港币 2-美元 3-台币 4-日元）
    uint8_t variety_category;                                         // 品种类别
};

/** 
 * @brief       国证指数快照数据结构
 * @attention   互联网模式结构
 **/
struct MDCnIndexSnapshot
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 证券代码
    int64_t orig_time;                                                // 交易所行情数据时间（YYYYMMDDHHMMSSsss)
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];     // 产品实时阶段及标志
    int64_t pre_close_index;                                          // 前收盘指数N18(6)，实际值需除以1000000
    int64_t open_index;                                               // 今开盘指数N18(6)，实际值需除以1000000
    int64_t high_index;                                               // 最高指数N18(6)，实际值需除以1000000
    int64_t low_index;                                                // 最低指数N18(6)，实际值需除以1000000
    int64_t last_index;                                               // 最新指数N18(6)，实际值需除以1000000
    int64_t close_index;                                              // 收盘指数，实际值需除以1000000
    int64_t total_volume_trade;                                       // 参与计算相应指数的交易数量N18(2)，实际值需除以100
    int64_t total_value_trade;                                        // 参与计算相应指数的成交金额N18(2)，实际值需除以100000
    uint8_t variety_category;                                         // 品种类别
};

/** 
 * @brief       港股通实时额度数据结构
 * @attention   互联网模式结构
 **/
struct MDHKTRealtimeLimit
{
    uint8_t market_type;                                              // 市场类型
    int64_t orig_time;                                                // 交易所行情数据时间（YYYYMMDDHHMMSSsss)
    int64_t threshold_amount;                                         // 每日初始额度，单位人民币元，实际值需除以100000
    int64_t pos_amt;                                                  // 日中剩余额度，单位人民币元，实际值需除以100000
    char    amount_status;                                            // 额度状态(1-额度用完或其他原因全市场禁止买入 2-额度可用)
    char    mkt_status[ConstField::kTradingStatusLen];                // 上交所港股通市场状态(上交所独有，来源于上交所文件行情)
    uint8_t variety_category;                                         // 品种类别
};

/** 
 * @brief        推送港股通产品状态数据结构
 * @attention    互联网模式结构
 **/
struct MDHKTProductStatus
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 证券代码
    int64_t orig_time;                                                // 交易所行情数据时间(YYYYMMDDHHMMSSsss)
    char    trading_status1[ConstField::kTradingStatusLen];           // 证券交易状态（整手订单）
    char    trading_status2[ConstField::kTradingStatusLen];           // 证券交易状态（零股订单）
    uint8_t variety_category;                                         // 品种类别
};

/** 
 * @brief       港股VCM数据结构
 * @attention   互联网模式结构
 **/
struct MDHKTVCM
{
    uint8_t market_type;                                              // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];              // 港股代码
    int64_t orig_time;                                                // 交易所行情数据时间（YYYYMMDDHHMMSSsss)
    int64_t start_time;                                               // 市调机制开始时间
    int64_t end_time;                                                 // 市调机制结束时间
    int64_t ref_price;                                                // 市调机制参考价格，实际值需除以1000000
    int64_t low_price;                                                // 市调机制最低价格，实际值需除以1000000
    int64_t high_price;                                               // 市调机制最高价格，实际值需除以1000000
    uint8_t variety_category;                                         // 品种类别
};

/**
 * @brief       查询 现货快照数据结构
 * @attention   托管机房模式结构
 **/
struct MDSnapshotL2
{
    uint8_t market_type;                                           // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];           // 证券代码
    int64_t orig_time;                                             // 时间（为YYYYMMDDHHMMSSsss）
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];  // 交易阶段代码
    //************************************上海现货行情交易状态***************************************************************
    //该字段为8位字符数组,左起每位表示特定的含义,无定义则填空格。
    //第0位:‘S’表示启动(开市前)时段,‘C’表示集合竞价时段,‘T’表示连续交易时段,
    //‘E’表示闭市时段 ,‘P’表示临时停牌,
    //‘M’表示可恢复交易的熔断(盘中集合竞价),‘N’表示不可恢复交易的熔断(暂停交易至闭市)
    //‘U’表示收盘集合竞价
    //第1位:‘0’表示此产品不可正常交易,‘1’表示此产品可正常交易。
    //第2位:‘0’表示未上市,‘1’表示已上市
    //第3位:‘0’表示此产品在当前时段不接受进行新订单申报,‘1’ 表示此产品在当前时段可接受进行新订单申报。

    //************************************深圳现货行情交易状态***************************************************************
    //第 0位:‘S’= 启动(开市前)‘O’= 开盘集合竞价‘T’= 连续竞价‘B’= 休市‘C’= 收盘集合竞价‘E’= 已闭市‘H’= 临时停牌‘A’= 盘后交易‘V’=波动性中断
    //第 1位:‘0’= 正常状态 ‘1’= 全天停牌

    
    //个位数存放收市行情标志(0:非收市行情;1:收市行情;2:盘后行情)
    //十位数存放正式行情与测试行情标志(0:正式行情;1:测试行情)

    //************************************港股股票行情交易状态***************************************************************
    // ‘1’表示正常交易，‘2’表示停牌，‘3’表示复牌
    int64_t pre_close_price;                                       // 昨收价，实际值需除以1000000  
    int64_t open_price;                                            // 开盘价，实际值需除以1000000 
    int64_t high_price;                                            // 最高价，实际值需除以1000000 
    int64_t low_price;                                             // 最低价，实际值需除以1000000 
    int64_t last_price;                                            // 最新价，实际值需除以1000000 
    int64_t close_price;                                           // 收盘价 （仅上海有效），实际值需除以1000000 
    int64_t bid_price[ConstField::kPositionLevelLen];              // 申买价，实际值需除以1000000 
    int64_t bid_volume[ConstField::kPositionLevelLen];             // 申买量，实际值需除以100
    int64_t offer_price[ConstField::kPositionLevelLen];            // 申卖价，实际值需除以1000000 
    int64_t offer_volume[ConstField::kPositionLevelLen];           // 申卖量，实际值需除以100
    int64_t num_trades;                                            // 成交笔数
    int64_t total_volume_trade;                                    // 成交总量，实际值需除以100
    int64_t total_value_trade;                                     // 成交总金额，实际值需除以100000
    int64_t total_bid_volume;                                      // 委托买入总量，实际值需除以100
    int64_t total_offer_volume;                                    // 委托卖出总量，实际值需除以100
    int64_t weighted_avg_bid_price;                                // 加权平均为委买价格，实际值需除以1000000
    int64_t weighted_avg_offer_price;                              // 加权平均为委卖价格，实际值需除以1000000
    int64_t IOPV;                                                  // IOPV净值估产，实际值需除以1000000
    int64_t yield_to_maturity;                                     // 到期收益率，实际值需除以1000
    int64_t high_limited;                                          // 涨停价，实际值需除以1000000
    int64_t low_limited;                                           // 跌停价，实际值需除以1000000
    int64_t price_earning_ratio1;                                  // 市盈率1，实际值需除以1000000
    int64_t price_earning_ratio2;                                  // 市盈率2，实际值需除以1000000
    int64_t change1;                                               // 升跌1（对比昨收价），实际值需除以1000000
    int64_t change2;                                               // 升跌2（对比上一笔），实际值需除以1000000
};

/**
 * @brief       现货逐笔成交数据结构
 * @attention   托管机房模式和互联网共用结构
 **/
struct MDTickExecution
{
    int32_t market_type;                                                // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];                // 证券代码
    int64_t exec_time;                                                  // 时间(YYYYMMDDHHMMSSsss)
    int32_t channel_no;                                                 // 频道号
    int64_t appl_seq_num;                                               // 频道编号
    int64_t exec_price;                                                 // 成交价格(实际值需除以1000000)
    int64_t exec_volume;                                                // 成交数量(实际值需除以100)
    int64_t value_trade;                                                // 成交金额(类型:金额)
    int64_t bid_appl_seq_num;                                           // 买方委托索引
    int64_t offer_appl_seq_num;                                         // 卖方委托索引
    //************************************上海市场买卖方向***************************************************************
    // 'B'=外盘,主动买 'S'=内盘,主动卖 'N'=未知
    //************************************港股市场买卖方向***************************************************************
    // 'B'=主动买入 '-'=中性盘 'S'=主动卖出
    uint8_t side;                                                       // 买卖方向
    //************************************上海市场成交类型***************************************************************
    // 'F'=成交
    //************************************深圳市场成交类型***************************************************************
    // '4'=撤销 'F'=成交
    //************************************港股市场成交类型***************************************************************
    // ''=自动对盘 'P'=开市前成交盘 'M'=非自动对盘 'Y'=同一证券商自动对盘 'X'=同一证券商非自动对盘 'D'=碎股交易 'U'=竞价交易 'Z'=海外交易
    uint8_t exec_type;                                                  // 成交类型
    char    md_stream_id[ConstField::kMDStreamIDMaxLen];                // 行情类别(仅深圳有效)
    int64_t biz_index;                                                  // 业务序号
    uint8_t variety_category;                                           // 品种类别(此字段暂不可用)
    char cancel_flag;													// 撤单标识（仅港股有效）Y是,N否
};

/**
 * @brief       查询 逐笔委托数据结构
 * @attention   托管机房模式和互联网共用结构
 **/
struct MDTickOrder
{
    uint8_t market_type;                                    // 市场类型
    char security_code[ConstField::kSecurityCodeLen];       // 证券代码
    int64_t appl_seq_num;                                   // 消息记录号
    int32_t channel_no;                                     // 频道编号
    int64_t order_time;                                     // 委托时间 （YYYYMMDDHHMMSSsss）
    int64_t order_price;                                    // 委托价格
    int64_t order_volume;                                   // 委托数量
    uint8_t side;                                           // 买卖方向
    uint8_t order_type;                                     // 订单类别
    char md_stream_id[ConstField::kMDStreamIDLen];          // 行情类别
    char product_status[ConstField::kTradingPhaseCodeLen];  // 产品状态(仅上海有效)
    int64_t orig_order_no;                                  // 原始订单号
    int64_t biz_index;                                      // 业务序号
};

/**
 * @brief       查询 委托队列数据结构
 * @attention   托管机房模式结构
 **/
struct MDOrderQueue
{
    uint8_t market_type;                                   // 市场类型
    char security_code[ConstField::kSecurityCodeLen];      // 证券代码
    int64_t order_time;                                    // 委托时间 YYYYMMDDHHMMSSsss
    uint8_t side;                                          // 买卖方向
    int64_t order_price;                                   // 委托价格
    int64_t order_volume;                                  // 委托数量
    int32_t num_of_orders;                                 // 总委托笔数
    int32_t items;                                         // 明细个数
    int64_t volume[50];                                    // 订单明细
    int32_t channel_no;                                    // 频道代码
    char md_stream_id[ConstField::kMDStreamIDLen];         // 行情类别
};

/**
 * @brief       查询 代码表数据结构
 * @attention   托管机房模式和互联网共用结构
 **/
struct MDCodeTable
{
    char security_code[ConstField::kSecurityCodeLen];        // 交易所证券代码
    char symbol[ConstField::kSecuritySymbolLen];             // 证券简称
    char english_name[ConstField::kSecurityEnglishNameLen];  // 英文简称
    uint8_t market_type;                                     // 市场类型
    char security_type[ConstField::kSecurityTypeLen];        // 证券类别
    char currency[ConstField::kCurrencyLen];                 // 币种
};

/**
 * @brief       查询 复权因子表数据结构
 * @attention   托管机房模式结构
 **/
struct MDExFactorTable
{
    char inner_code[ConstField::kSecurityCodeLen];           // 证券内部代码
    char security_code[ConstField::kSecurityCodeLen];        // 证券代码
    uint32_t ex_date;                                        // 除权除息日（为yyyyMMdd）
    double ex_factor;                                        // 复权因子 N38(15)
    double cum_factor;                                       // 累计复权因子 N38(15)
};

/**
 * @brief       查询 个股信息数据结构
 * @attention   托管机房模式结构
 **/
struct MDStockInfo
{
    char security_code[ConstField::kSecurityCodeLen];       // 交易所证券代码
    char symbol[ConstField::kSecuritySymbolLen];            // 证券简称			
    uint8_t market_type;                                    // 市场类型
    char security_type[ConstField::kSecurityTypeLen];       // 证券类别
    char currency[ConstField::kCurrencyLen];                // 币种
    char security_status[ConstField::kSecurityStatusLen];   // 证券状态 kSecurityStatusLen=24             
    uint64_t pre_close_price;                               // 昨收价
    uint64_t total_shares;                                  // 总股本
    uint64_t flow_shares;                                   // 流通股本
    uint8_t noprofit;                                       // 是否盈利 Y：是，未盈利  N：否，已盈利
    uint8_t weighted_voting_rights;                         // 是否存在投票权差异 Y.是 N.否
    uint8_t registration_flag;                              // 是否注册制 Y.是 N.否
    double  eps;                                            // 每股收益 N18(6)
    double  eps_cell;                                       // 预计每股收益 N18(6)
    double  net_profit_ttm;                                 // 净利润（TTM） N18(6)
    double  net_profit;                                     // 净利润 N18(6)
    double  net_asset;                                      // 净资产 N18(6)
    double  net_profit_recent_annual;                       // 净利润 N18(6)
    double  net_profit_first_quarter;                       // 净资产 N18(6)
};

/**
 * @brief       查询 代码表数据结构
 * @attention   托管机房模式和互联网共用结构
 **/
struct MDCodeTableRecord
{
    char security_code[ConstField::kFutureSecurityCodeLen];                 // 证券代码
    uint8_t market_type;                                                    // 证券市场
    char symbol[ConstField::kSymbolLen];                                    // 简称
    char english_name[ConstField::kSecurityAbbreviationLen];                // 英文名
    char security_type[ConstField::kMaxTypesLen];                           // 证券子类别
    char    currency[ConstField::kTypesLen];                                // 币种(CNY:人民币,HKD:港币,USD:美元,AUD:澳币,CAD:加币,JPY:日圆,SGD:新加坡币,GBP:英镑,EUR:欧元,TWD:新台币,Other:其他)
    uint8_t variety_category;                                               // 证券类别
    int64_t pre_close_price;                                                // 昨收价(实际值需除以1000000)
    char underlying_security_id[ConstField::kSecurityCodeLen];              // 标的代码 (仅期权/权证/期货期权有效)
    char    contract_type[ConstField::kMaxTypesLen];                        // 合约类别 (仅期权/期货期权有效)
    int64_t exercise_price;                                                 // 行权价(仅期权/期货期权有效,实际值需除以1000000)
    uint32_t expire_date;                                                   // 到期日 (仅期权/期货期权有效)
    int64_t high_limited;                                                   // 涨停价(实际值需除以1000000)
    int64_t low_limited;                                                    // 跌停价(实际值需除以1000000)
    char security_status[ConstField::kCodeTableSecurityStatusMaxLen];       // 产品状态标志
    //************************************产品状态标志*************************************************************
    //1:停牌,2:除权,3:除息,4:风险警示,5:退市整理期,6:上市首日,7:公司再融资,8:恢复上市首日,9:网络投票,10:增发股份上市
    //11:合约调整,12:暂停上市后协议转让,13:实施双转单调整,14:特定债券转让,15:上市初期,16:退市整理期首日
    int64_t price_tick;                                                     // 最小价格变动单位(实际值需除以1000000)
    int64_t buy_qty_unit;                                                   // 限价买数量单位(实际值需除以100)
    int64_t sell_qty_unit;                                                  // 限价卖数量单位(实际值需除以100)
    int64_t market_buy_qty_unit;                                            // 市价买数量单位(实际值需除以100)
    int64_t market_sell_qty_unit;                                           // 市价卖数量单位(实际值需除以100)
    int64_t buy_qty_lower_limit;                                            // 限价买数量下限(实际值需除以100)
    int64_t buy_qty_upper_limit;                                            // 限价买数量上限(实际值需除以100)
    int64_t sell_qty_lower_limit;                                           // 限价卖数量下限(实际值需除以100)
    int64_t sell_qty_upper_limit;                                           // 限价卖数量上限(实际值需除以100)
    int64_t market_buy_qty_lower_limit;                                     // 市价买数量下限 (实际值需除以100)
    int64_t market_buy_qty_upper_limit;                                     // 市价买数量上限 (实际值需除以100)
    int64_t market_sell_qty_lower_limit;                                    // 市价卖数量下限 (实际值需除以100)
    int64_t market_sell_qty_upper_limit;                                    // 市价卖数量上限 (实际值需除以100)
    uint32_t list_day;                                                      // 上市日期
    int64_t par_value;                                                      // 面值(实际值需除以1000000)
    int64_t outstanding_share;                                              // 总发行量(上交所不支持,实际值需除以100)
    int64_t public_float_share_quantity;                                    // 流通股数(上交所不支持,实际值需除以100)
    int64_t contract_multiplier;                                            // 对回购标准券折算率(实际值需除以100000)
    char regular_share[ConstField::RegularShare];                           // 对应回购标准券(仅深交所)
    int64_t interest;                                                       // 应计利息(实际值需除以100000000)
    int64_t coupon_rate;                                                    // 票面年利率(实际值需除以1000000)
    char product_code[ConstField::kFutureSecurityCodeLen];                   // 期货品种产品代码(仅期货期权有效)
    uint32_t delivery_year;                                                 // 交割年份(仅期货期权有效)
    uint32_t delivery_month;                                                // 交割月份(仅期货期权有效)
    uint32_t create_date;                                                   // 创建日期(仅期货期权有效)
    uint32_t start_deliv_date;                                              // 开始交割日(仅期货期权有效)
    uint32_t end_deliv_date;                                                // 结束交割日(仅期货期权有效)
    uint32_t position_type;                                                 // 持仓类型(仅期货期权有效)
};

/**
 * @name 成分股结构定义
 **/
struct ConstituentStockInfo
{
    char security_code[ConstField::kConsSecurityCodeLen];                               //成份证券代码
    uint8_t market_type;                                                                //成份证券所属市场(仅深圳有效,参考 MarketType)
    char underlying_symbol[ConstField::kSymbolETFLen];                                  //成份证券简称
    int64_t component_share;                                                            //成份证券数量(实际值需除以100)
    char substitute_flag;                                                               //现金替代标志
    //************************************深圳现金替代标志***************************************************************
    //0=禁止现金替代(必须有证券),1=可以进行现金替代(先用证券,证券不足时差额部分用现金替代),2=必须用现金替代
    //************************************上海现金替代标志***************************************************************
    //ETF 公告文件 1.0 版格式
    //0 –沪市不可被替代, 1 – 沪市可以被替代, 2 – 沪市必须被替代, 3 – 深市退补现金替代, 4 – 深市必须现金替代
    //5 – 非沪深市场成份证券退补现金替代(不适用于跨沪深港 ETF 产品), 6 – 非沪深市场成份证券必须现金替代(不适用于跨沪深港 ETF 产品)
    //ETF 公告文件 2.1 版格式
    //0 –沪市不可被替代, 1 – 沪市可以被替代, 2 – 沪市必须被替代, 3 – 深市退补现金替代, 4 – 深市必须现金替代
    //5 – 非沪深市场成份证券退补现金替代(不适用于跨沪深港 ETF 产品), 6 – 非沪深市场成份证券必须现金替代(不适用于跨沪深港 ETF 产品)
    //7 – 港市退补现金替代(仅适用于跨沪深港ETF产品), 8 – 港市必须现金替代(仅适用于跨沪深港ETF产品)
    int64_t premium_ratio;                                                              //溢价比例(实际值需除以1000000)
    int64_t discount_ratio;                                                             //折价比例(实际值需除以1000000)
    int64_t creation_cash_substitute;                                                   //申购替代金额(仅深圳有效,实际值需除以100000)
    int64_t redemption_cash_substitute;                                                 //赎回替代金额(仅深圳有效,实际值需除以100000)
    int64_t substitution_cash_amount;                                                   //替代总金额(仅上海有效,实际值需除以100000)
    char underlying_security_id[ConstField::KUnderlyingSecurityID];                     //成份证券所属市场ID(仅对跨市场债券(银行间)ETF启用)
    char buy_or_sell_to_open;                                                           //期权期货买入开仓或卖出开仓(暂时未启用,取值为空)
    char reserved[ConstField::KReserved];                                               //预留字段(暂时未启用,取值为空)
};

/**
* @brief ETF代码表数据
* @attention   托管机房模式和互联网共用结构
**/
struct MDETFCodeTableRecord
{
    char security_code[ConstField::kSecurityCodeLen] ;                                  //证券代码
    int64_t creation_redemption_unit;                                                   //每个篮子对应的ETF份数(实际值需除以100)
    int64_t max_cash_ratio;                                                             //最大现金替代比例(实际值需除以1000000)
    char publish;                                                                       //是否发布 IOPV,Y=是, N=否
    char creation;                                                                      //是否允许申购,Y=是, N=否(仅深圳有效)
    char redemption;                                                                    //是否允许赎回,Y=是, N=否(仅深圳有效)
    char creation_redemption_switch;                                                    //申购赎回切换(仅上海有效,0 - 不允许申购/赎回, 1 - 申购和赎回皆允许, 2 - 仅允许申购, 3 - 仅允许赎回)
    int64_t record_num;                                                                 //深市成份证券数目(实际值需除以100)
    int64_t total_record_num;                                                           //所有成份证券数量(实际值需除以100)
    int64_t estimate_cash_component;                                                    //预估现金差额(实际值需除以100000)
    int64_t trading_day;                                                                //当前交易日(格式:YYYYMMDD)
    int64_t pre_trading_day;                                                            //前一交易日(格式:YYYYMMDD)
    int64_t cash_component;                                                             //前一日现金差额(实际值需除以100000)
    int64_t nav_per_cu;                                                                 //前一日最小申赎单位净值(实际值需除以1000000)
    int64_t nav;                                                                        //前一日基金份额净值(实际值需除以1000000)
    uint8_t market_type;                                                                //证券所属市场(参考 MarketType)
    char symbol[ConstField::kSymbolETFLen];                                             //基金名称(仅深圳有效)
    char fund_management_company[ConstField::kManagmentETFLen];                         //基金公司名称(仅深圳有效)
    char underlying_security_id[ConstField::kSecurityCodeLen];                          //拟合指数代码(仅深圳有效)
    char underlying_security_id_source[ConstField::KUnderlyingSecurityIDSource];        //拟合指数代码源(仅深圳有效)
    int64_t dividend_per_cu;                                                            //红利金额(实际值需除以100000)
    int64_t creation_limit;                                                             //累计申购总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    int64_t redemption_limit;                                                           //累计赎回总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    int64_t creation_limit_per_user;                                                    //单个账户累计申购总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    int64_t redemption_limit_per_user;                                                  //单个账户累计赎回总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    int64_t net_creation_limit;                                                         //净申购总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    int64_t net_redemption_limit;                                                       //净赎回总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    int64_t net_creation_limit_per_user;                                                //单个账户净申购总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    int64_t net_redemption_limit_per_user;                                              //单个账户净赎回总额限制,为 0 表示没有限制(仅深圳有效,实际值需除以100)
    char all_cash_flag;                                                                 //是否支持全现金申赎(暂时未启用,取值为空)
    char all_cash_amount[ConstField::AllCashAmount];                                    //全现金替代的总金额(暂时未启用,取值为空)
    char all_cash_premium_rate[ConstField::AllCashAremiumRate];                         //全现金替代的申购溢价比例(暂时未启用,取值为空)
    char all_cash_discount_rate[ConstField::AllCashDiscountRate];                       //全现金替代的赎回折价比例(暂时未启用,取值为空)
    char rtgs_flag;                                                                     //是否支持RTGS(暂时未启用,取值为空)
    char reserved[ConstField::KReserved];                                               //预留字段(暂时未启用,取值为空)
    std::vector<ConstituentStockInfo> constituent_stock_infos;                          //成分股信息
};


/**
* @brief        三方资讯数据
* @attention    托管机房模式和互联网模式共用结构
**/
struct ThirdInfoData
{
    uint64_t task_id;       // 任务id
    uint64_t data_size;     // 数据大小
    char*    json_data;     // 数据json串
};

/**
* @brief        回放任务状态应答结构
* @attention    托管机房模式结构
**/
struct RspTaskStatus 
{
    int64_t task_id;                              // 任务id(任务编号，例如:1)
    int16_t status;                               // 状态值(详细参考tgw_datatype.h头文件中HistoryTaskStatus)
    int16_t process_rate;                         // 进度（暂不支持）
    int16_t error_code;                           // 状态为失败的错误码(详细参考tgw_datatype.h头文件中HistoryErrorCode)
    int16_t error_msg_len;                        // 错误消息长度
    char* error_msg;                              // 错误消息首地址
}; 

/**
* @brief        （快照、逐笔成交、逐笔委托、委托队列、k线）查询状态应答结构
* @attention    托管机房模式和互联网模式共用结构
**/
struct RspUnionStatus 
{
    uint16_t req_type;                                      // 请求类型(详细参考tgw_datatype.h头文件中MDDatatype,仅k线需要)
    uint8_t market_type;                                    // 市场（参照tgw_datatype.h中的MarketType)
    char security_code[ConstField::kFutureSecurityCodeLen]; // 证券代码(000001)
};

/**
* @brief        通用状态应答结构
* @attention    托管机房模式和互联网模式共用结构
**/
struct StatusInfo
{
    int64_t task_id;                             // 任务id, 格式为MMDDHHmmSS+序列号（1~1000000）
};

/**
* @brief        证券代码信息 查询状态应答结构
* @attention    托管机房模式和互联网模式共用结构
**/
struct RspSecuritiesInfoStatus
{
    uint32_t code_table_item_cnt;                 // SubCodeTableItem总个数
    SubCodeTableItem*  codes;                     // SubCodeTableItem数组地址
};

/**
* @brief         三方资讯查询状态应答结构
* @attention    托管机房模式和互联网模式共用结构
**/
struct RspThirdInfoStatus 
{
    int64_t task_id;                             // 任务id, 格式为MMDDHHmmSS+序列号（1~1000000）
};

/**
* @brief        查询状态应答结构
* @attention    托管机房模式和互联网模式共用结构
**/
struct RspQueryStatus
{
    int32_t error_code;                           // 状态为失败的错误码(详细参考tgw_datatype.h头文件中ErrorCode)
    int16_t error_msg_len;                        // 错误消息长度
    char* error_msg;                              // 错误消息首地址
    RspUnionStatus rsp_union_status;              // 快照、逐笔成交、逐笔委托、委托队列、k线、复权因子、代码表查询状态（具体类型通过req_type区分）
    StatusInfo rsp_status;                        // 通用查询状态（当前加工因子）
    RspSecuritiesInfoStatus rsp_stockinfo_status; // 证券代码信息查询状态(含ETFInfo)
    RspThirdInfoStatus rsp_thirdinfo_status;      // 三方资讯查询状态
};

struct MDOrderBookItem
{
    int64_t price;                                                          // 价格，实际值需除以1000000
    int64_t volume;                                                         // 总数量，实际值需除以100
    int64_t order_queue_size;                                               // 委托队列大小
    int64_t order_queue[50];                                                // 委托队列数量, 最多揭示50笔
};

/**
* @name MDOrderBook 委托簿
* @{ */
struct MDOrderBook
{
    int32_t channel_no;                                                     // 频道号
    int32_t market_type;                                                    // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];                    // 证券代码
    int64_t last_tick_time;                                                 // 最新逐笔生成时间
    int64_t last_snapshot_time;                                             // 最新快照生成时间(固定为0,无实际意义)
    int64_t last_tick_seq;                                                  // 最新逐笔序列号
    std::vector<MDOrderBookItem> bid_order_book;                            // 买委托簿
    std::vector<MDOrderBookItem> offer_order_book;                          // 卖委托簿
    int64_t total_num_trades;                                               // 基于委托簿演算的成交总笔数
    int64_t total_volume_trade;                                             // 基于委托簿演算的成交总量，实际值需除以100
    int64_t total_value_trade;                                              // 基于委托簿演算的成交总金额，实际值需除以100000
    int64_t last_price;                                                     // 基于委托簿演算的最新价，实际值需除以1000000
};
/**  @} */

/**
* @name MDOrderBookSnapshot 委托簿快照数据
* @{ */
struct MDOrderBookSnapshot
{
    uint8_t	market_type;                                        // 市场类型,参考公共数据字典市场类型(MarketType)
    uint8_t	variety_category;                                   // 品种类别,参照公共数据字典品种类型(VarietyCategory)
    char	security_code[ConstField::kSecurityCodeLen];        // 证券代码
    int64_t	last_tick_seq;                                      // 构建快照的最新逐笔记录号
    int32_t	channel_no;                                         // 构建快照的逐笔原始频道编号
    int64_t	orig_time;                                          // 基于委托簿演算的行情快照时间(最新逐笔记录号对应的逐笔时间)(为YYYYMMDDHHMMSSsss)
    int64_t	last_price;                                         // 基于委托簿演算的最新价，实际值需除以1000000
    int64_t	total_num_trades;                                   // 基于委托簿演算的成交总笔数
    int64_t	total_volume_trade;                                 // 基于委托簿演算的成交总量，实际值需除以100
    int64_t	total_value_trade;                                  // 基于委托簿演算的成交总金额，实际值需除以100000
    int64_t	total_bid_volume;                                   // 基于委托簿演算的委托买入总量，实际值需除以100
    int64_t	total_offer_volume;                                 // 基于委托簿演算的委托卖出总量，实际值需除以100
    int64_t	num_bid_orders;                                     // 基于委托簿演算的买方委托价位数
    int64_t	num_offer_orders;                                   // 基于委托簿演算的卖方委托价位数
    int64_t	bid_price[ConstField::kPositionLevelLen];           // 申买价，实际值需除以1000000
    int64_t	bid_volume[ConstField::kPositionLevelLen];          // 申买量，实际值需除以100
    int64_t	offer_price[ConstField::kPositionLevelLen];         // 申卖价，实际值需除以1000000
    int64_t	offer_volume[ConstField::kPositionLevelLen];        // 申卖量，实际值需除以100
};
/**  @} */

}; // end of tgw
}; // end of galaxy

#pragma pack(pop)