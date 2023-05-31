#pragma once

#include <iostream>
#include <tgw_history_spi.h>

namespace galaxy { namespace tgw {

class QuerySnapshotSpi : public IGMDSnapshotSpi
{
public:
    virtual void OnMDSnapshotL2(MDSnapshotL2* snapshots, uint32_t cnt) override;
    virtual void OnMDSnapshotL1(MDSnapshotL1* snapshots, uint32_t cnt) override;
    virtual void OnMDIndexSnapshot(MDIndexSnapshot* index_snapshots, uint32_t cnt) override;
    virtual void OnMDHKTSnapshot(MDHKTSnapshot* hkt_snapshots, uint32_t cnt) override;
    virtual void OnMDOptionSnapshot(MDOptionSnapshot* opt_snapshots, uint32_t cnt) override;
    virtual void OnMDFutureSnapshot(MDFutureSnapshot* future_snapshots, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 逐笔委托查询Spi（托管机房模式spi）
class QueryTickOrderSpi : public IGMDTickOrderSpi
{
public:
    virtual void OnMDTickOrder(MDTickOrder* tick_orders, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 逐笔成交查询Spi（托管机房模式spi）
class QueryTickExecutionSpi : public IGMDTickExecutionSpi
{
public:
    virtual void OnMDTickExecution(MDTickExecution* tick_execs, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 委托队列查询Spi（托管机房模式spi）
class QueryOrderQueueSpi : public IGMDOrderQueueSpi
{
public:
    virtual void OnMDOrderQueue(MDOrderQueue* order_queues, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// K线Spi（互联网和托管机房模式通用spi）
class QueryKlineSpi : public IGMDKlineSpi
{
public:
    virtual void OnMDKLine(MDKLine* klines, uint32_t cnt, uint16_t kline_type) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 代码表Spi（托管机房模式spi）
class QueryCodeTableSpi : public IGMDCodeTableSpi
{
public:
    virtual void OnMDCodeTable(MDCodeTable* code_tables, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 证券代码信息查询Spi（互联网和托管机房模式通用spi）
class QuerySecuritiesInfoSpi : public IGMDSecuritiesInfoSpi
{
public:
    virtual void OnMDSecuritiesInfo(MDCodeTableRecord* code_tables, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// ETF代码信息查询Spi（互联网和托管机房模式通用spi）
class QueryETFInfoSpi : public IGMDETFInfoSpi
{
public:
    virtual void OnMDETFInfo(MDETFCodeTableRecord* etf_info, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 复权因子查询Spi（托管机房模式spi）
class QueryExFactorSpi: public IGMDExFactorSpi
{
public:
    virtual void OnMDExFactor(MDExFactorTable* ex_factor_tables, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 加工因子查询Spi（互联网和托管机房模式通用spi）
class QueryFactorSpi: public IGMDFactorSpi
{
public:
    virtual void OnFactor(Factor* factors, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};

// 三方资讯查询Spi（互联网和托管机房模式通用spi）
class QueryThirdInfoSpi: public IGMDThirdInfoSpi
{
public:
    virtual void OnThirdInfo(ThirdInfoData* data, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
};


}
}