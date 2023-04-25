#pragma once

#include <iostream>
#include <tgw.h>
#include <tgw_history_spi.h>

namespace galaxy { namespace tgw {

class ReplayHistorySpi : public IGMDHistorySpi
{
public:
    virtual void OnMDSnapshot(int64_t task_id, MDSnapshotL2* snapshots, uint32_t cnt) override;
    virtual void OnMDTickExecution(int64_t task_id, MDTickExecution* ticks, uint32_t cnt) override;
    virtual void OnMDKline(int64_t task_id, MDKLine* klines, uint32_t cnt, uint16_t kline_type) override;
    virtual void OnRspTaskStatus(int64_t task_id, RspTaskStatus* task_status) override;
};


}
}