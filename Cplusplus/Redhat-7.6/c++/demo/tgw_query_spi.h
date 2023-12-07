#pragma once

#include <iostream>
#include <tgw_history_spi.h>
#include "tgw_query_manager.h"

namespace galaxy { namespace tgw {

class QuerySnapshotSpi : public IGMDSnapshotSpi
{
public:
    QuerySnapshotSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDSnapshotL2(MDSnapshotL2* snapshots, uint32_t cnt) override;
    virtual void OnMDSnapshotL1(MDSnapshotL1* snapshots, uint32_t cnt) override;
    virtual void OnMDIndexSnapshot(MDIndexSnapshot* index_snapshots, uint32_t cnt) override;
    virtual void OnMDHKTSnapshot(MDHKTSnapshot* hkt_snapshots, uint32_t cnt) override;
    virtual void OnMDOptionSnapshot(MDOptionSnapshot* opt_snapshots, uint32_t cnt) override;
    virtual void OnMDFutureSnapshot(MDFutureSnapshot* future_snapshots, uint32_t cnt) override;
    virtual void OnMDHKExOrderSnapshot(MDHKExOrderSnapshot* hke_order_snapshot, uint32_t cnt) override;
    virtual void OnMDHKExOrderBrokerSnapshot(MDHKExOrderBrokerSnapshot* hke_order_broker_snapshot, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 逐笔委托查询Spi（托管机房模式spi）
class QueryTickOrderSpi : public IGMDTickOrderSpi
{
public:
    QueryTickOrderSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDTickOrder(MDTickOrder* tick_orders, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 逐笔成交查询Spi（互联网和托管机房模式通用spi）
class QueryTickExecutionSpi : public IGMDTickExecutionSpi
{
public:
    QueryTickExecutionSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDTickExecution(MDTickExecution* tick_execs, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 委托队列查询Spi（托管机房模式spi）
class QueryOrderQueueSpi : public IGMDOrderQueueSpi
{
public:
    QueryOrderQueueSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDOrderQueue(MDOrderQueue* order_queues, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// K线Spi（互联网和托管机房模式通用spi）
class QueryKlineSpi : public IGMDKlineSpi
{
public:
    QueryKlineSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDKLine(MDKLine* klines, uint32_t cnt, uint16_t kline_type) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 代码表Spi（托管机房模式spi）
class QueryCodeTableSpi : public IGMDCodeTableSpi
{
public:
    QueryCodeTableSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDCodeTable(MDCodeTable* code_tables, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 证券代码信息查询Spi（互联网和托管机房模式通用spi）
class QuerySecuritiesInfoSpi : public IGMDSecuritiesInfoSpi
{
public:
    QuerySecuritiesInfoSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDSecuritiesInfo(MDCodeTableRecord* code_tables, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// ETF代码信息查询Spi（互联网和托管机房模式通用spi）
class QueryETFInfoSpi : public IGMDETFInfoSpi
{
public:
    QueryETFInfoSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDETFInfo(MDETFCodeTableRecord* etf_info, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 复权因子查询Spi（托管机房模式spi）
class QueryExFactorSpi: public IGMDExFactorSpi
{
public:
    QueryExFactorSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnMDExFactor(MDExFactorTable* ex_factor_tables, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 加工因子查询Spi（互联网和托管机房模式通用spi）
class QueryFactorSpi: public IGMDFactorSpi
{
public:
    QueryFactorSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnFactor(Factor* factors, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};

// 三方资讯查询Spi（互联网和托管机房模式通用spi）
class QueryThirdInfoSpi: public IGMDThirdInfoSpi
{
public:
    QueryThirdInfoSpi()
    {
        task_id_ = IGMDApi::GetTaskID();
    }
    virtual void OnThirdInfo(ThirdInfoData* data, uint32_t cnt) override;
    virtual void OnStatus(RspQueryStatus* status) override;
    int64_t& GetTaskID(){ return task_id_; }
private:
    int64_t task_id_{0};
};


}
}