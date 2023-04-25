#include "tgw_push_spi.h"

namespace galaxy { namespace tgw {

TgwPushSpi::TgwPushSpi()
{
}

void TgwPushSpi::OnLog(const int32_t& level, const char* log, uint32_t len)
{
    if (level > LogLevel::kDebug)
    {
        std::cout << "TGW log: " 
                << "    level: " << level 
                << "    log:   " << log << std::endl;
    }
}

void TgwPushSpi::OnLogon(LogonResponse* data)
{
    std::cout << "Receive OnLogon Info: " << std::endl;
    std::cout << "api_mode: "
                << data->api_mode << std::endl
                << "logon_msg_len: "
                << data->logon_msg_len << std::endl
                << "logon_json: "
                << data->logon_json << std::endl;
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDSnapshot(MDSnapshotL1* data, uint32_t cnt)
{
    std::cout << "Receive OnMDSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDIndexSnapshot(MDIndexSnapshot* data, uint32_t cnt)
{
    std::cout << "Receive OnMDIndexSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDOptionSnapshot(MDOptionSnapshot* data, uint32_t cnt)
{
    std::cout << "Receive OnMDOptionSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDHKTSnapshot(MDHKTSnapshot* data, uint32_t cnt)
{
    std::cout << "Receive OnMDHKTSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDAfterHourFixedPriceSnapshot(MDAfterHourFixedPriceSnapshot* data, uint32_t cnt)
{
    std::cout << "Receive OnMDAfterHourFixedPriceSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDCSIIndexSnapshot(MDCSIIndexSnapshot* data, uint32_t cnt)
{
    std::cout << "Receive OnMDCSIIndexSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
   IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDCnIndexSnapshot(MDCnIndexSnapshot* data, uint32_t cnt)
{
    std::cout << "Receive OnMDCnIndexSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDHKTRealtimeLimit(MDHKTRealtimeLimit* data, uint32_t cnt)
{
    std::cout << "Receive OnMDHKTRealtimeLimit Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "orig_time: "
                    << data[i].orig_time << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDHKTProductStatus(MDHKTProductStatus* data, uint32_t cnt)
{
    std::cout << "Receive OnMDHKTProductStatus Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDHKTVCM(MDHKTVCM* data, uint32_t cnt)
{
    std::cout << "Receive OnMDHKTVCM Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnMDFutureSnapshot(MDFutureSnapshot* data, uint32_t cnt)
{
    std::cout << "Receive OnMDFutureSnapshot Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnKLine(MDKLine* data, uint32_t cnt, uint32_t kline_type)
{
    std::cout << "Receive OnKLine Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnSnapshotDerive(MDSnapshotDerive* data, uint32_t cnt)
{
    std::cout << "Receive OnSnapshotDerive Info: " << std::endl;
    for (uint32_t i = 0 ; i < cnt; i++)
    {
        std::cout << "market_type: "
                    << (int)data[i].market_type << std::endl
                    << "security_code: "
                    << data[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void TgwPushSpi::OnFactor(Factor* data)
{
    std::cout << "Receive OnFactor Info: " << std::endl;
    std::cout << "data_size: "
                << data->data_size << std::endl
                << "json_buf: "
                << data->json_buf << std::endl;
   IGMDApi::FreeMemory(data);
}

}
}
