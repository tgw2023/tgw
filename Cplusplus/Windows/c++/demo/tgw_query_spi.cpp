#include "tgw_query_spi.h"
#include <tgw.h>

namespace galaxy { namespace tgw {

void QuerySnapshotSpi::OnMDSnapshotL2(MDSnapshotL2* snapshots, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive stock snapshotL2 Info: " << std::endl
            << "market_type: " << (int)snapshots[i].market_type << std::endl
            << "security_code: " << snapshots[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(snapshots);
}

void QuerySnapshotSpi::OnMDSnapshotL1(MDSnapshotL1* snapshots, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive stock snapshotL1 Info: " << std::endl
            << "market_type: " << (int)snapshots[i].market_type << std::endl
            << "security_code: " << snapshots[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(snapshots);
}

void QuerySnapshotSpi::OnMDIndexSnapshot(MDIndexSnapshot* index_snapshots, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive index snapshot Info: " << std::endl
            << "market_type:" << (int)index_snapshots[i].market_type << std::endl
            << "security_code:" << index_snapshots[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(index_snapshots);
}

void QuerySnapshotSpi::OnMDHKTSnapshot(MDHKTSnapshot* hkt_snapshots, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive hkt snapshot Info: " << std::endl
            << "market_type:" << (int)hkt_snapshots[i].market_type << std::endl
            << "security_code:" << hkt_snapshots[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(hkt_snapshots);
}

void QuerySnapshotSpi::OnMDOptionSnapshot(MDOptionSnapshot* opt_snapshots, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive option snapshot Info: " << std::endl
            << "market_type:" << (int)opt_snapshots[i].market_type << std::endl
            << "security_code:" << opt_snapshots[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(opt_snapshots);
}

void QuerySnapshotSpi::OnMDFutureSnapshot(MDFutureSnapshot* future_snapshots, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive future snapshot Info: " << std::endl
            << "market_type:" << (int)future_snapshots[i].market_type << std::endl
            << "security_code:" << future_snapshots[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(future_snapshots);
}

void QuerySnapshotSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QuerySnapshotSpi Status : "              << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "req_type = "            << status->rsp_union_status.req_type << "\n"
            << "market_type = "         << (int)status->rsp_union_status.market_type << "\n"
            << "security_code = "       << status->rsp_union_status.security_code << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryTickOrderSpi::OnMDTickOrder(MDTickOrder* tick_orders, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive tickOrder Info: " << std::endl
            << "market_type:" << (int)tick_orders[i].market_type << std::endl
            << "security_code:" << tick_orders[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(tick_orders);
}

void QueryTickOrderSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryTickOrderSpi Status : "              << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "market_type = "         << (int)status->rsp_union_status.market_type << "\n"
            << "security_code = "       << status->rsp_union_status.security_code << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryTickExecutionSpi::OnMDTickExecution(MDTickExecution* tick_execs, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive tickExecution Info: " << std::endl
            << "market:" << (int)tick_execs[i].market_type << std::endl
            << "security_code:" << tick_execs[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(tick_execs);
}

void QueryTickExecutionSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryTickExecutionSpi Status : "         << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "market_type = "         << (int)status->rsp_union_status.market_type << "\n"
            << "security_code = "       << status->rsp_union_status.security_code << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryOrderQueueSpi::OnMDOrderQueue(MDOrderQueue* order_queues, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive MDOrderQueue Info: " << std::endl
            << "market_type:" << (int)order_queues[i].market_type << std::endl
            << "security_code:" << order_queues[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(order_queues);
}

void QueryOrderQueueSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryOrderQueueSpi Status : "            << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "market_type = "         << (int)status->rsp_union_status.market_type << "\n"
            << "security_code = "       << status->rsp_union_status.security_code << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryKlineSpi::OnMDKLine(MDKLine* klines, uint32_t cnt, uint16_t kline_type)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive MDQueryKline Info: " << std::endl
            << "market_type:"  << (int)klines[i].market_type << std::endl
            << "security_code:" << klines[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(klines);
}

void QueryKlineSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryKlineSpi Status : "                 << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "market_type = "         << (int)status->rsp_union_status.market_type << "\n"
            << "security_code = "       << status->rsp_union_status.security_code << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryCodeTableSpi::OnMDCodeTable(MDCodeTable* code_tables, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive MDCodeTable Info: " << std::endl
            << "security_code:" << code_tables[i].security_code << std::endl
            << "symbol:" << code_tables[i].symbol << std::endl;
    }
    IGMDApi::FreeMemory(code_tables);
}

void QueryCodeTableSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryCodeTableSpi Status : "             << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n";
    IGMDApi::FreeMemory(status);
}

void QuerySecuritiesInfoSpi::OnMDSecuritiesInfo(MDCodeTableRecord* code_tables, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive securitiesInfo Info: " << std::endl
            << "security_code:" << code_tables[i].security_code << std::endl
            << "symbol:" << code_tables[i].symbol << std::endl;
    }
    IGMDApi::FreeMemory(code_tables);
}

void QuerySecuritiesInfoSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QuerySecuritiesInfoSpi Status : "        << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "  market_type = "       << (int)status->rsp_stockinfo_status.codes[0].market << "\n"
            << "  security_code = "     << status->rsp_stockinfo_status.codes[0].security_code << "\n";
    IGMDApi::FreeMemory(status);
}


void QueryETFInfoSpi::OnMDETFInfo(MDETFCodeTableRecord* etf_info, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive ETFInfo Info: " << std::endl
            << "security_code:" << etf_info[i].security_code << std::endl
            << "symbol:" << etf_info[i].symbol << std::endl;
    }
    IGMDApi::FreeMemory(etf_info);
}

void QueryETFInfoSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QuerySecuritiesInfoSpi Status : "        << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "  market_type = "       << (int)status->rsp_stockinfo_status.codes[0].market << "\n"
            << "  security_code = "     << status->rsp_stockinfo_status.codes[0].security_code << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryExFactorSpi::OnMDExFactor(MDExFactorTable* ex_factor_tables, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << "Receive exFactorTable Info: " << std::endl
            << " inner_code:" << ex_factor_tables[i].inner_code<< std::endl
            << " security_code:" << ex_factor_tables[i].security_code << std::endl;
    }
    IGMDApi::FreeMemory(ex_factor_tables);
}

void QueryExFactorSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryExFactorSpi Status : "              << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryFactorSpi::OnFactor(Factor* factors, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << " json_buf is: " << factors[i].json_buf << std::endl;
        std::cout << " data_size is: " << factors[i].data_size << std::endl;
        IGMDApi::FreeMemory(factors[i].json_buf);
    }
    IGMDApi::FreeMemory(factors);
}

void QueryFactorSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryFactorSpi Status : "                << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "  task_id = "           << status->rsp_status.task_id << "\n";
    IGMDApi::FreeMemory(status);
}

void QueryThirdInfoSpi::OnThirdInfo(ThirdInfoData* data, uint32_t cnt)
{
    for (uint32_t i = 0; i < cnt; ++i)
    {
        std::cout << " task_id is: " << data[i].task_id << std::endl;
        std::cout << " json_data is: " << data[i].json_data << std::endl;
        std::cout << " data_size is: " << data[i].data_size << std::endl;
    }
    IGMDApi::FreeMemory(data);
}

void QueryThirdInfoSpi::OnStatus(RspQueryStatus* status)
{
    std::cout << "Receive QueryThirdInfoSpi Status : "             << "\n"
            << "  error_code  =  "      << status->error_code      << "\n"
            << "  error_msg_len  =  "   << status->error_msg_len   << "\n"
            << "  error_msg  =  "       << status->error_msg       << "\n"
            << "  task_id = "           << (int)status->rsp_thirdinfo_status.task_id << "\n";
    IGMDApi::FreeMemory(status);
}

}
}