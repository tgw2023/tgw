#include "tgw_replay_spi.h"

namespace galaxy { namespace tgw {


void ReplayHistorySpi::OnMDSnapshot(int64_t task_id, MDSnapshotL2* snapshots, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive stock snapshot Info: " << std::endl
            << "market_type: " << (int)snapshots[i].market_type << std::endl
            << "security_code: " << snapshots[i].security_code << std::endl;
    }

    // 应用可将数据指针复制到回调函数之外，数据在释放之前一直可用
    // 应用必须在适当的地方释放内存，否则可能造成数据阻塞
    IGMDApi::FreeMemory(snapshots);
}

void ReplayHistorySpi::OnMDTickExecution(int64_t task_id, MDTickExecution* ticks, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive MDTickExecution Info: " << std::endl
            << "market:" << (int)ticks[i].market_type << std::endl
            << "security_code:" << ticks[i].security_code << std::endl;
    }

    // 应用可将数据指针复制到回调函数之外，数据在释放之前一直可用
    // 应用必须在适当的地方释放内存，否则可能造成数据阻塞
    IGMDApi::FreeMemory(ticks);
}

void ReplayHistorySpi::OnMDKline(int64_t task_id, MDKLine* klines, uint32_t cnt, uint16_t kline_type)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive OnMDKline Info: " << std::endl
            << "market_type:"  << (int)klines[i].market_type << std::endl
            << "security_code:" << klines[i].security_code << std::endl;
    }

    // 应用可将数据指针复制到回调函数之外，数据在释放之前一直可用
    // 应用必须在适当的地方释放内存，否则可能造成数据阻塞    
    IGMDApi::FreeMemory(klines);
}

void ReplayHistorySpi::OnRspTaskStatus(int64_t task_id, RspTaskStatus* task_status) 
{
   
}

}
}