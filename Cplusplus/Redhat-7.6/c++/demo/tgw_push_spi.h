#pragma once

#include <iostream>
#include <map>
#include <tgw.h>

namespace galaxy { namespace tgw {

class TgwPushSpi : public IGMDSpi
{
public:
    TgwPushSpi();
    void OnLog(const int32_t& level,const char* log,
                       uint32_t len) override;
    void OnLogon(LogonResponse* data) override;

    void OnMDSnapshot(MDSnapshotL1* data, uint32_t cnt) override;
    void OnMDIndexSnapshot(MDIndexSnapshot* data, uint32_t cnt) override;
    void OnMDOptionSnapshot(MDOptionSnapshot* data, uint32_t cnt) override;
    void OnMDHKTSnapshot(MDHKTSnapshot* data, uint32_t cnt) override;
    void OnMDAfterHourFixedPriceSnapshot(MDAfterHourFixedPriceSnapshot* data, uint32_t cnt) override;
    void OnMDCSIIndexSnapshot(MDCSIIndexSnapshot* data, uint32_t cnt) override;
    void OnMDCnIndexSnapshot(MDCnIndexSnapshot* data, uint32_t cnt) override;
    void OnMDHKTRealtimeLimit(MDHKTRealtimeLimit* data, uint32_t cnt) override;
    void OnMDHKTProductStatus(MDHKTProductStatus* data, uint32_t cnt) override;
    void OnMDHKTVCM(MDHKTVCM* data, uint32_t cnt) override;
    void OnMDFutureSnapshot(MDFutureSnapshot* data, uint32_t cnt) override;
    void OnKLine(MDKLine* data, uint32_t cnt, uint32_t kline_type) override;
    void OnSnapshotDerive(MDSnapshotDerive* data, uint32_t cnt) override;
    void OnFactor(Factor* data) override;
    void OnMDOrderBook(std::vector<MDOrderBook>& order_book) override;
    void OnMDOrderBookSnapshot(MDOrderBookSnapshot* order_book_snapshots, uint32_t cnt) override;

private:
};


}
}
