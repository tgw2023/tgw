
#pragma once
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
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
    char factor_type[64];                             // 因子父类型(英文)
    char factor_sub_type[64];                         // 因子子类型(英文)
    char factor_name[64];				              // 因子名称(英文)
};

/**
* @brief        K线查询 接口默认请求参数
* @attention    托管机房模式和互联网模式共用结构
**/
struct ReqKline 
{
    char security_code[ConstField::kQuerySecurityCodeLen];            // 证券代码
    uint8_t market_type;                                              // 市场类型
    uint8_t cq_flag;                                                  // 除权标志（0:不复权;1:向前复权;2:向后复权; 默认0）
    uint32_t cq_date;                                                 // 除权日期（yyyMMdd）
    uint32_t qj_flag;                                                 // 全价标志（债券）（0：净价，1：全价）
    uint16_t cyc_type;                                                // 数据周期（参考tgw_datatype.h中的MDDatatype描述）
    uint32_t cyc_def;                                                 // 周期数量
    uint8_t auto_complete;                                            // 自动补全（0:不补齐，1：补齐 默1）
    uint32_t begin_date;                                              // 开始日期（yyyyMMdd）
    uint32_t end_date;                                                // 结束日期（yyyyMMdd）
    uint32_t begin_time;                                              // 开始时间（默认：HHmm， 支持HHmmssSSS）
    uint32_t end_time;                                                // 结束时间（默认：HHmm， 支持HHmmssSSS）
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
    char     factor_type[64];          // 因子父类型(英文)
    char     factor_sub_type[64];      // 因子子类型(英文)
    char     factor_name[64];		   // 因子名称(英文)
    uint32_t begin_date;               // 开始日期（yyyyMMdd）
    uint32_t end_date;                 // 结束日期（yyyyMMdd）
    uint32_t begin_time;               // 开始时间（HHmmssSSS）
    uint32_t end_time;                 // 结束时间（HHmmssSSS）
    char     Key1[64];                 // 预留字段Key1
    char     Key2[64];                 // 预留字段Key2
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
    char    trading_phase_code[ConstField::kTradingPhaseCodeLen];// 产品实时阶段及标志（仅深圳有效）
    int64_t pre_close_index;                                    // 前收盘指数N18(6)，实际值需除以1000000
    int64_t open_index;                                         // 今开盘指数N18(6)，实际值需除以1000000
    int64_t high_index;                                         // 最高指数N18(6)，实际值需除以1000000
    int64_t low_index;                                          // 最低指数N18(6)，实际值需除以1000000
    int64_t last_index;                                         // 最新指数N18(6)，实际值需除以1000000
    int64_t close_index;                                        // 收盘指数（仅上海有效），实际值需除以1000000
    int64_t total_volume_trade;                                 // 参与计算相应指数的交易数量N18(2)，实际值需除以100(上交所:手, 深交所:张)
    int64_t total_value_trade;                                  // 参与计算相应指数的成交金额N18(2)，实际值需除以100000
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
 * @attention   托管机房模式结构
 **/
struct MDTickExecution
{
    int32_t market_type;                                                // 市场类型
    char    security_code[ConstField::kSecurityCodeLen];                // 证券代码
    int64_t exec_time;                                                  // 时间(YYYYMMDDHHMMSSsss)
    int32_t channel_no;                                                 // 频道号
    int64_t appl_seq_num;                                               // 频道编号
    int64_t exec_price;                                                 // 成交价格(类型:价格)
    int64_t exec_volume;                                                // 成交数量(类型:数量)
    int64_t value_trade;                                                // 成交金额(类型:金额)
    int64_t bid_appl_seq_num;                                           // 买方委托索引
    int64_t offer_appl_seq_num;                                         // 卖方委托索引
    uint8_t side;                                                       // 买卖方向(仅上海有效 B-外盘,主动买 S-内盘,主动卖 N-未知)
    uint8_t exec_type;                                                  // 成交类型(深圳: 4-撤销 F-成交, 上海: F-成交)
    char    md_stream_id[ConstField::kMDStreamIDMaxLen];                // 行情类别(仅深圳有效)
    int64_t biz_index;                                                  // 业务序号
    uint8_t variety_category;                                           // 品种类别(此字段暂不可用)
};

/**
 * @brief       查询 逐笔委托数据结构
 * @attention   托管机房模式结构
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
 * @attention   托管机房模式结构
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
 * @attention   互联网模式结构
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
    int64_t pre_close_price;                                                // 昨收价(类型:价格)
    char underlying_security_id[ConstField::kSecurityCodeLen];              // 标的代码 (仅期权/权证/期货期权有效)
    char    contract_type[ConstField::kMaxTypesLen];                        // 合约类别 (仅期权/期货期权有效)
    int64_t exercise_price;                                                 // 行权价(仅期权/期货期权有效,类型:价格)
    uint32_t expire_date;                                                   // 到期日 (仅期权/期货期权有效)
    int64_t high_limited;                                                   // 涨停价(类型:价格)
    int64_t low_limited;                                                    // 跌停价(类型:价格)
    char security_status[ConstField::kCodeTableSecurityStatusMaxLen];       // 产品状态标志
    //************************************产品状态标志*************************************************************
    //1:停牌,2:除权,3:除息,4:风险警示,5:退市整理期,6:上市首日,7:公司再融资,8:恢复上市首日,9:网络投票,10:增发股份上市
    //11:合约调整,12:暂停上市后协议转让,13:实施双转单调整,14:特定债券转让,15:上市初期,16:退市整理期首日
    int64_t price_tick;                                                     // 最小价格变动单位(类型:价格)
    int64_t buy_qty_unit;                                                   // 限价买数量单位(类型:数量)
    int64_t sell_qty_unit;                                                  // 限价卖数量单位(类型:数量)
    int64_t market_buy_qty_unit;                                            // 市价买数量单位(类型:数量)
    int64_t market_sell_qty_unit;                                           // 市价卖数量单位(类型:数量)
    int64_t buy_qty_lower_limit;                                            // 限价买数量下限(类型:数量)
    int64_t buy_qty_upper_limit;                                            // 限价买数量上限(类型:数量)
    int64_t sell_qty_lower_limit;                                           // 限价卖数量下限(类型:数量)
    int64_t sell_qty_upper_limit;                                           // 限价卖数量上限(类型:数量)
    int64_t market_buy_qty_lower_limit;                                     // 市价买数量下限 (类型:数量)
    int64_t market_buy_qty_upper_limit;                                     // 市价买数量上限 (类型:数量)
    int64_t market_sell_qty_lower_limit;                                    // 市价卖数量下限 (类型:数量)
    int64_t market_sell_qty_upper_limit;                                    // 市价卖数量上限 (类型:数量)
    uint32_t list_day;                                                      // 上市日期
    int64_t par_value;                                                      // 面值(类型:价格)
    int64_t outstanding_share;                                              // 总发行量(上交所不支持,类型:数量)
    int64_t public_float_share_quantity;                                    // 流通股数(上交所不支持,类型:数量)
    int64_t contract_multiplier;                                            // 对回购标准券折算率(类型:比例)
    char regular_share[ConstField::RegularShare];                           // 对应回购标准券(仅深交所)
    int64_t interest;                                                       // 应计利息(类型:汇率)
    int64_t coupon_rate;                                                    // 票面年利率(类型:比例)
    char product_code[ConstField::kFutureSecurityCodeLen];                   // 期货品种产品代码(仅期货期权有效)
    uint32_t delivery_year;                                                 // 交割年份(仅期货期权有效)
    uint32_t delivery_month;                                                // 交割月份(仅期货期权有效)
    uint32_t create_date;                                                   // 创建日期(仅期货期权有效)
    uint32_t start_deliv_date;                                              // 开始交割日(仅期货期权有效)
    uint32_t end_deliv_date;                                                // 结束交割日(仅期货期权有效)
    uint32_t position_type;                                                 // 持仓类型(仅期货期权有效)
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
* @brief        加工因子查询状态应答结构
* @attention    托管机房模式和互联网模式共用结构
**/
struct RspFactorStatus 
{
    char factor_type[64];                         // 因子父类型(英文)
    char factor_sub_type[64];                     // 因子子类型(英文)
    char factor_name[64];		                  // 因子名称(英文)
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
    RspFactorStatus rsp_factor_status;            // 加工因子查询状态
    RspSecuritiesInfoStatus rsp_stockinfo_status; // 证券代码信息查询状态
    RspThirdInfoStatus rsp_thirdinfo_status;      // 三方资讯查询状态
};

}; // end of tgw
}; // end of galaxy

#pragma pack(pop)