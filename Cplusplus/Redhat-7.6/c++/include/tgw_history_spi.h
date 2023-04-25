#pragma once

#include "tgw_export.h"
#include "tgw_struct.h"
#include "tgw_datatype.h"
#include "tgw.h"

namespace galaxy { namespace tgw {

//--------------------------------TCP回放通道 回放接口类---------------------------------------------
class IGMDHistorySpi
{
public:
    virtual ~IGMDHistorySpi() {}

    /**
     * @brief OnMDSnapshot          接收现货快照回放数据回调
     *
     * @param task_id               任务id
     * @param snapshots             现货快照数据（股票、债券、基金）
     * @param cnt                   数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              使用此接口需开启RTCP回放通道
     */
    virtual void OnMDSnapshot(int64_t task_id, MDSnapshotL2* snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(snapshots); (void)task_id; (void)cnt; }

    /**
     * @brief OnMDIndexSnapshot     接收指数快照回放数据回调（此接口暂不支持）
     *
     * @param task_id               任务id
     * @param index_snapshots       指数快照数据
     * @param cnt                   数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              使用此接口需开启RTCP回放通道
     */
    virtual void OnMDIndexSnapshot(int64_t task_id, MDIndexSnapshot* index_snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(index_snapshots); (void)task_id; (void)cnt; }

    /**
     * @brief OnMDHKSnapshot        接收港股快照回放数据回调（此接口暂不支持）
     *
     * @param task_id               任务id
     * @param hk_snapshots          港股快照数据
     * @param cnt                   数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              使用此接口需开启RTCP回放通道
     */
    virtual void OnMDHKTSnapshot(int64_t task_id, MDHKTSnapshot* hkt_snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(hkt_snapshots); (void)task_id; (void)cnt; }

    /**
     * @brief OnMDOptionSnapshot    接收期权快照回放数据回调（此接口暂不支持）
     *
     * @param task_id               任务id
     * @param opt_snapshots         期权快照数据
     * @param cnt                   数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              使用此接口需开启RTCP回放通道
     */
    virtual void OnMDOptionSnapshot(int64_t task_id, MDOptionSnapshot* opt_snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(opt_snapshots); (void)task_id; (void)cnt; }

    /**
     * @brief OnMDTickExecution     接收逐笔成交回放数据回调
     *
     * @param task_id               任务id
     * @param ticks                 逐笔成交数据
     * @param cnt                   数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              使用此接口需开启RTCP回放通道
     */
    virtual void OnMDTickExecution(int64_t task_id, MDTickExecution* ticks, uint32_t cnt)
    { IGMDApi::FreeMemory(ticks); (void)task_id; (void)cnt; }

    /**
     * @brief OnMDKline             接收K线回放数据回调
     *
     * @param task_id               任务id
     * @param klines                K线数据
     * @param cnt                   数据个数
     * @param kline_type            k线数据类型（具体数据类型参见API开发文档和tgw_datatype.h头文件）
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              使用此接口需开启RTCP回放通道
     */
    virtual void OnMDKline(int64_t task_id, MDKLine* klines, uint32_t cnt, uint16_t kline_type)
    { IGMDApi::FreeMemory(klines); (void)task_id; (void)cnt; }

    /**
     * @brief OnRspTaskStatus       应答任务状态回调
     *
     * @param task_id               任务id
     * @param task_status           任务状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              使用此接口需开启RTCP回放通道
     */
    virtual void OnRspTaskStatus(int64_t task_id, RspTaskStatus* task_status) 
    { (void)task_id; (void)task_status; }
};

//--------------------------------TCP推送通道 查询接口类---------------------------------------------
/********************快照查询Spi（现货、指数、港股通、期权、期货、互联网和托管机房模式通用spi）********************/
class IGMDSnapshotSpi
{
public:
    virtual ~IGMDSnapshotSpi(){};

    /**
     * @brief OnMDSnapshot          现货快照数据回调
     *
     * @param snapshots             现货快照数据
     * @param cnt                   现货快照数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              仅托管机房使用
     */
    virtual void OnMDSnapshotL2(MDSnapshotL2* snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(snapshots); (void)cnt; };

    /**
     * @brief OnMDSnapshot          现货快照数据回调
     *
     * @param snapshots             现货快照数据
     * @param cnt                   现货快照数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              仅互联网使用
     */
    virtual void OnMDSnapshotL1(MDSnapshotL1* snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(snapshots); (void)cnt; };

    /**
     * @brief OnMDIndexSnapshot     指数快照数据回调
     *
     * @param index_snapshots       指数快照数据
     * @param cnt                   指数快照数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDIndexSnapshot(MDIndexSnapshot* index_snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(index_snapshots); (void)cnt; };

    /**
     * @brief OnMDHKTSnapshot       港股通快照数据回调
     *
     * @param hkt_snapshots         港股通快照数据
     * @param cnt                   港股通快照数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDHKTSnapshot(MDHKTSnapshot* hkt_snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(hkt_snapshots); (void)cnt; };

    /**
     * @brief OnMDOptionSnapshot    期权快照数据回调
     *
     * @param opt_snapshots         期权快照数据
     * @param cnt                   期权快照数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDOptionSnapshot(MDOptionSnapshot* opt_snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(opt_snapshots); (void)cnt; };

    /**
     * @brief OnMDFutureSnapshot    期货快照数据回调
     *
     * @param future_snapshots      期货快照数据
     * @param cnt                   期货快照数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDFutureSnapshot(MDFutureSnapshot* future_snapshots, uint32_t cnt)
    { IGMDApi::FreeMemory(future_snapshots); (void)cnt; };

    /**
     * @brief OnStatus              快照数据状态回调
     *
     * @param status                现货快照数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************逐笔委托查询Spi（托管机房模式spi）********************/
class IGMDTickOrderSpi
{
public:
    virtual ~IGMDTickOrderSpi(){};

    /**
     * @brief OnMDTickOrder         逐笔委托数据回调
     *
     * @param tick_orders           逐笔委托数据
     * @param cnt                   逐笔委托数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDTickOrder(MDTickOrder* tick_orders, uint32_t cnt)
    { IGMDApi::FreeMemory(tick_orders); (void)cnt; };

    /**
     * @brief OnStatus              逐笔委托数据状态回调
     *
     * @param status                逐笔委托数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************逐笔成交查询Spi（托管机房模式spi）********************/
class IGMDTickExecutionSpi
{
public:
    virtual ~IGMDTickExecutionSpi(){};

    /**
     * @brief OnMDTickExecution     逐笔成交数据回调
     *
     * @param tick_execs            逐笔成交数据
     * @param cnt                   逐笔成交数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDTickExecution(MDTickExecution* tick_execs, uint32_t cnt)
    { IGMDApi::FreeMemory(tick_execs); (void)cnt; };

    /**
     * @brief OnStatus              逐笔成交数据状态回调
     *
     * @param status                逐笔成交数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************委托队列查询Spi（托管机房模式spi）********************/
class IGMDOrderQueueSpi
{
public:
    virtual ~IGMDOrderQueueSpi(){};

    /**
     * @brief OnMDOrderQueue        委托队列数据回调
     *
     * @param order_queues          委托队列数据
     * @param cnt                   委托队列数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDOrderQueue(MDOrderQueue* order_queues, uint32_t cnt)
    { IGMDApi::FreeMemory(order_queues); (void)cnt; };

    /**
     * @brief OnStatus              委托队列数据状态回调
     *
     * @param status                委托队列数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************K线Spi（互联网和托管机房模式通用spi）********************/
class IGMDKlineSpi
{
public:
    virtual ~IGMDKlineSpi(){};

    /**
     * @brief OnMDKLine             k线数据回调
     *
     * @param klines                k线数据
     * @param cnt                   k线数据个数
     * @param kline_type            k线类型
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDKLine(MDKLine* klines, uint32_t cnt, uint16_t kline_type)
    { IGMDApi::FreeMemory(klines); (void)cnt; };

    /**
     * @brief OnStatus              k线数据状态回调
     *
     * @param status                k线数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************代码表Spi（互联网和托管机房模式通用spi）********************/
class IGMDCodeTableSpi
{
public:
    virtual ~IGMDCodeTableSpi(){};

    /**
     * @brief OnMDCodeTable         代码表数据回调
     *
     * @param code_tables           代码表数据
     * @param cnt                   代码表数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDCodeTable(MDCodeTable* code_tables, uint32_t cnt)
    { IGMDApi::FreeMemory(code_tables); (void)cnt; };

    /**
     * @brief OnStatus              代码表状态回调
     *
     * @param status                代码表数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************证券代码信息查询Spi（互联网和托管机房模式通用spi）********************/
class IGMDSecuritiesInfoSpi
{
public:
    virtual ~IGMDSecuritiesInfoSpi(){};

    /**
     * @brief OnMDSecuritiesInfo    证券代码信息数据回调（从上游SFS服务端获取数据）
     *
     * @param code_tables           代码表详细信息数据
     * @param cnt                   代码表详细信息数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              支持托管机房和互联网模式
     */
    virtual void OnMDSecuritiesInfo(MDCodeTableRecord* code_tables, uint32_t cnt)
    { IGMDApi::FreeMemory(code_tables); (void)cnt; };

    /**
     * @brief OnStatus              代码表详细信息，股票信息状态回调
     *
     * @param status                代码表详细信息，股票信息数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************复权因子查询Spi（托管机房模式spi）********************/
class IGMDExFactorSpi
{
public:
    virtual ~IGMDExFactorSpi(){};

    /**
     * @brief OnMDExFactor         复权因子数据回调
     *
     * @param ex_factor_tables      复权因子数据
     * @param cnt                   复权因子数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnMDExFactor(MDExFactorTable* ex_factor_tables, uint32_t cnt)
    { IGMDApi::FreeMemory(ex_factor_tables); (void)cnt; };

    /**
     * @brief OnStatus              复权因子状态回调
     *
     * @param status                复权因子数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/******************** 加工因子查询Spi（互联网和托管机房模式通用spi）********************/
class IGMDFactorSpi
{
public:
    virtual ~IGMDFactorSpi(){};

    /**
     * @brief OnFactor              加工因子数据回调
     *
     * @param factors               加工因子数据
     * @param cnt                   加工因子数据个数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnFactor(Factor* factors, uint32_t cnt)
    {
        for (uint32_t i = 0; i < cnt; i++)
        {
            IGMDApi::FreeMemory(factors->json_buf);
        }
        IGMDApi::FreeMemory(factors);
        (void)cnt;
    };

    /**
     * @brief OnStatus              加工因子状态回调
     *
     * @param status                加工因子数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

/********************三方资讯查询Spi（互联网和托管机房模式通用spi）********************/
class IGMDThirdInfoSpi
{
public:
    virtual ~IGMDThirdInfoSpi(){};

    /**
     * @brief OnThirdInfo           三方资讯数据回调
     *
     * @param data                  三方资讯数据
     * @param cnt                   三方资讯数据条数
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnThirdInfo(ThirdInfoData* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; };

    /**
     * @brief OnStatus              三方资讯状态回调
     *
     * @param status                三方资讯数据状态
     * @attention                   使用后需要通过接口 IGMDApi::FreeMemory释放数据
     *                              
     */
    virtual void OnStatus(RspQueryStatus* status)
    { IGMDApi::FreeMemory(status); };
};

};
};