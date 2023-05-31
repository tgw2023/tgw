#include <string.h>
#include "tgw_push_spi.h"
#include "tgw_query_spi.h"
#include "tgw_replay_spi.h"
#include <tgw_datatype.h>
#include <Windows.h>

// ------------------------------- 推送请求示例 ------------------------------------
void GeneralSubscribeReq()
{
    // 设置订阅参数，以两次订阅为例
    galaxy::tgw::SubscribeItem sub_cfg[2];

    // 第一次订阅的市场类型设置
    sub_cfg[0].market = galaxy::tgw::MarketType::kSZSE;
    // 第一次订阅的数据类型设置
    sub_cfg[0].flag = galaxy::tgw::SubscribeDataType::kNone;
    // 第一次订阅的证券代码设置
    strncpy_s(sub_cfg[0].security_code, "000001", sizeof(sub_cfg[0].security_code));
    // 第一次订阅的品种类别设置
    sub_cfg[0].category_type = galaxy::tgw::VarietyCategory::kNone;

    // 第二次订阅的市场类型设置
    sub_cfg[1].market = galaxy::tgw::MarketType::kNone;
    // 第二次订阅的数据类型设置
    sub_cfg[1].flag = galaxy::tgw::SubscribeDataType::kNone;
    // 第二次订阅的证券代码设置，为空代表全部证券代码
    strncpy_s(sub_cfg[1].security_code, "", sizeof(sub_cfg[1].security_code));
    // 第二次订阅的品种类别设置
    sub_cfg[1].category_type = galaxy::tgw::VarietyCategory::kStock;

    //  发送多个订阅请求
    galaxy::tgw::IGMDApi::Subscribe(sub_cfg, 2);
    
    //  取消订阅
    // galaxy::tgw::IGMDApi::UnSubscribe(sub_cfg, 2);
}

void FactorSubscribeReq()
{
    /**
     * @note 父类型不支持单独全订阅及取消订阅，即 all xxx xxx
     *       因子子类型不支持单独全订阅及取消订阅,即 xxx all xxx
     *       不支持父类型和子类型全订阅及取消订阅，但是因子名称为指定因子，即 all all xxx
     *       不支持因子父类型和因子名称全订阅及取消订阅，但是因子子类型为指定因子，即 all xxx all
     */
    galaxy::tgw::SubFactorItem item[4];
    // 订阅全因子类型设置 all all all
    strncpy_s(item[0].factor_type, "all", sizeof(item[0].factor_type));
    strncpy_s(item[0].factor_sub_type, "all", sizeof(item[0].factor_sub_type));
    strncpy_s(item[0].factor_name, "all", sizeof(item[0].factor_name));

    galaxy::tgw::IGMDApi::SubFactor(&item[0], 1);

    // 订阅指定父类型下全因子类型设置 xxx all all
    strncpy_s(item[1].factor_type, "Financial_Factor", sizeof(item[1].factor_type));
    strncpy_s(item[1].factor_sub_type, "all", sizeof(item[1].factor_sub_type));
    strncpy_s(item[1].factor_name, "all", sizeof(item[1].factor_name));

    galaxy::tgw::IGMDApi::SubFactor(&item[1], 1);

    // 订阅指定父类型+子类型下全因子类型设置 xxx xxx all
    strncpy_s(item[2].factor_type, "Financial_Factor", sizeof(item[2].factor_type));
    strncpy_s(item[2].factor_sub_type, "PE", sizeof(item[2].factor_sub_type));
    strncpy_s(item[2].factor_name, "all", sizeof(item[2].factor_name));

    galaxy::tgw::IGMDApi::SubFactor(&item[2], 1);

    // 订阅指定父类型+子类型+因子名称类型设置 xxx xxx xxx
    strncpy_s(item[3].factor_type, "Financial_Factor", sizeof(item[3].factor_type));
    strncpy_s(item[3].factor_sub_type, "PE", sizeof(item[3].factor_sub_type));
    strncpy_s(item[3].factor_name, "PE_TTL", sizeof(item[3].factor_name));

    galaxy::tgw::IGMDApi::SubFactor(&item[3], 1);
    // 取消因子订阅
    // galaxy::tgw::IGMDApi::UnSubFactor(&item[3], 1);  入参同上
}

// ------------------------------- 查询请求示例 ------------------------------------
void QueryKlineReq(galaxy::tgw::QueryKlineSpi* spi)
{
    galaxy::tgw::ReqKline req_kline;
    memset(&req_kline, 0, sizeof(req_kline));
    strncpy_s(req_kline.security_code, "000001", sizeof(req_kline.security_code));
    req_kline.market_type = 102;
    req_kline.cq_flag = 0;
    req_kline.auto_complete = 1;
    req_kline.cyc_type = galaxy::tgw::MDDatatype::k1KLine; // 1分钟k
    req_kline.begin_date = 20210611;
    req_kline.end_date = 20210611;
    req_kline.begin_time = 930;
    req_kline.end_time = 1700;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryKline(spi, req_kline)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryKline faild, ErrorCode: " << ec << std::endl;
}

void QuerySnapshotReq(galaxy::tgw::QuerySnapshotSpi* spi)
{
    galaxy::tgw::ReqDefault req_snapshot;
    memset(&req_snapshot, 0, sizeof(req_snapshot));
    strncpy_s(req_snapshot.security_code, "000001", sizeof(req_snapshot.security_code));
    req_snapshot.market_type = 102;
    req_snapshot.date = 20210611;
    req_snapshot.begin_time = 93000000;
    req_snapshot.end_time = 170000000;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QuerySnapshot(spi, req_snapshot)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QuerySnapshot faild, ErrorCode: " << ec << std::endl;
}

void QueryTickExecReq(galaxy::tgw::QueryTickExecutionSpi* spi)
{
    galaxy::tgw::ReqDefault req;
    memset(&req, 0, sizeof(req));
    strncpy_s(req.security_code, "000001", sizeof(req.security_code));
    req.market_type = 102;
    req.date = 20210611;
    req.begin_time = 93000000;
    req.end_time = 170000000;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryTickExecution(spi, req)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryTickExec faild, ErrorCode: " << ec << std::endl;
}

void QueryTickOrderReq(galaxy::tgw::QueryTickOrderSpi* spi)
{
    galaxy::tgw::ReqDefault req;
    memset(&req, 0, sizeof(req));
    strncpy_s(req.security_code, "000001", sizeof(req.security_code));
    req.market_type = 102;
    req.date = 20210611;
    req.begin_time = 93000000;
    req.end_time = 170000000;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryTickOrder(spi, req)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryTickOrder faild, ErrorCode: " << ec << std::endl;
}

void QueryOrderQueueReq(galaxy::tgw::QueryOrderQueueSpi* spi)
{
    galaxy::tgw::ReqDefault req;
    memset(&req, 0, sizeof(req));
    strncpy_s(req.security_code, "000001", sizeof(req.security_code));
    req.market_type = 102;
    req.date = 20210611;
    req.begin_time = 93000000;
    req.end_time = 170000000;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryOrderQueue(spi, req)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryOrderQueue faild, ErrorCode: " << ec << std::endl;
}

void QueryCodeTableReq(galaxy::tgw::QueryCodeTableSpi* spi)
{
    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryCodeTable(spi)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryCodeTable faild, ErrorCode: " << ec << std::endl;
}

void QuerySecuritiesInfoReq(galaxy::tgw::QuerySecuritiesInfoSpi* spi)
{
    galaxy::tgw::SubCodeTableItem req_codelist;
    memset(&req_codelist, 0, sizeof(req_codelist));
    strncpy_s(req_codelist.security_code, "000001", sizeof(req_codelist.security_code));
    req_codelist.market = 102;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QuerySecuritiesInfo(spi, &req_codelist, 1)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QuerySecuritiesInfo faild, ErrorCode: " << ec << std::endl;
}

void QueryETFInfoReq(galaxy::tgw::QueryETFInfoSpi* spi)
{
    galaxy::tgw::SubCodeTableItem req_etf;
    memset(&req_etf, 0, sizeof(req_etf));
    strncpy_s(req_etf.security_code, "000001", sizeof(req_etf.security_code));
    req_etf.market = 102;
    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryETFInfo(spi, &req_etf, 1)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryETFInfoReq faild, ErrorCode: " << ec << std::endl;
}

void QueryExFactorReq(galaxy::tgw::QueryExFactorSpi* spi)
{
    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryExFactorTable(spi, "000001")) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryExFactorTable faild, ErrorCode: " << ec << std::endl;
}

void QueryFactorReq(galaxy::tgw::QueryFactorSpi* spi)
{
    galaxy::tgw::ReqFactor req_factor;
    memset(&req_factor, 0, sizeof(req_factor));
    req_factor.task_id = galaxy::tgw::IGMDApi::GetTaskID();
    strncpy_s(req_factor.factor_type, "factor_type", sizeof(req_factor.factor_type));
    strncpy_s(req_factor.factor_sub_type, "factor_sub_type", sizeof(req_factor.factor_sub_type));
    strncpy_s(req_factor.factor_name, "factor_name", sizeof(req_factor.factor_name));
    req_factor.begin_date = 20210611;
    req_factor.end_date = 20210611;
    req_factor.begin_time = 93000000;
    req_factor.end_time = 170000000;
    strncpy_s(req_factor.security_code, "000001", sizeof(req_factor.security_code));
    req_factor.market = 102;
    req_factor.category = 2;
    req_factor.offset = 0;
    req_factor.count = 100;
    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryFactor(spi, req_factor)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryFactor faild, ErrorCode: " << ec << std::endl;
}

void QueryThirdInfoReq(galaxy::tgw::QueryThirdInfoSpi* spi)
{
    auto task_id = galaxy::tgw::IGMDApi::GetTaskID();
    galaxy::tgw::IGMDApi::SetThirdInfoParam(task_id, "function_id", "01");
    galaxy::tgw::IGMDApi::SetThirdInfoParam(task_id, "WD_CODE", "0000001");
    galaxy::tgw::IGMDApi::SetThirdInfoParam(task_id, "trade_data", "20210101");

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::QueryThirdInfo(spi, task_id)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "QueryThirdInfo faild, ErrorCode: " << ec << std::endl;
}

void ReplaySnapshotReq(galaxy::tgw::ReplayHistorySpi* spi)
{
    Sleep(3000);   // 延迟3s至登录成功
    galaxy::tgw::ReqHistoryItem history_item[2];
    history_item[0].market = 102;
    strcpy_s(history_item[0].security_code, "000001");
    history_item[1].market = 102;
    strcpy_s(history_item[1].security_code, "000002");

    galaxy::tgw::ReqReplay req_replay;
    req_replay.begin_date = 20211228;
    req_replay.end_date = 20211228;
    req_replay.begin_time = 91500000;
    req_replay.end_time = 103100000;
    req_replay.req_item_cnt = 2;
    req_replay.req_items = history_item;
    req_replay.md_data_type = galaxy::tgw::MDDatatype::kSnapshot;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::ReplayRequest(spi, req_replay)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "ReplaySnapshot faild, ErrorCode: " << ec << std::endl;
}

void ReplayTickExecReq(galaxy::tgw::ReplayHistorySpi* spi)
{
	Sleep(3000);   // 延迟3s至登录成功
    galaxy::tgw::ReqHistoryItem history_item[2];
    history_item[0].market = 102;
    strcpy_s(history_item[0].security_code, "000001");
    history_item[1].market = 102;
    strcpy_s(history_item[1].security_code, "000002");

    galaxy::tgw::ReqReplay req_replay;
    req_replay.begin_date = 20211228;
    req_replay.end_date = 20211228;
    req_replay.begin_time = 91500000;
    req_replay.end_time = 103100000;
    req_replay.req_item_cnt = 2;
    req_replay.req_items = history_item;

    req_replay.md_data_type = galaxy::tgw::MDDatatype::kTickExecution;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::ReplayRequest(spi, req_replay)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "ReplayTickExec faild, ErrorCode: " << ec << std::endl;        
}

void ReplayKlineReq(galaxy::tgw::ReplayHistorySpi* spi)
{
	Sleep(3000);   // 延迟3s至登录成功
    galaxy::tgw::ReqHistoryItem history_item[2];
    history_item[0].market = 102;
    strcpy_s(history_item[0].security_code, "000001");
    history_item[1].market = 102;
    strcpy_s(history_item[1].security_code, "000002");

    galaxy::tgw::ReqReplayKline req_k;
    memset(&req_k, 0, sizeof(req_k));
    req_k.begin_date = 20211228; 
    req_k.begin_time = 930;     
    req_k.cq_flag = 0;
    req_k.cyc_type = galaxy::tgw::MDDatatype::k1KLine; // 1分钟k
    req_k.auto_complete = 1;  
    req_k.end_date = 20211228; 
    req_k.end_time = 1032;
    req_k.task_id = galaxy::tgw::IGMDApi::GetTaskID();
    req_k.req_item_cnt = 2;
    req_k.req_items = history_item;

    int32_t ec;
    if ((ec = galaxy::tgw::IGMDApi::ReplayKline(spi, req_k)) != galaxy::tgw::ErrorCode::kSuccess)
        std::cout << "ReplayKline faild, ErrorCode: " << ec << std::endl;  
}


int main()
{
    // 准备配置
    galaxy::tgw::Cfg cfg;
    strncpy_s(cfg.server_vip, "127.0.0.1", sizeof(cfg.server_vip));
    cfg.server_port = 9000;
    strncpy_s(cfg.username, "*****", sizeof(cfg.username));
    strncpy_s(cfg.password, "*****", sizeof(cfg.password));

    uint16_t api_mode = galaxy::tgw::ApiMode::kColocationMode;  // 设置api模式 托管机房模式/互联网模式
    // uint16_t api_mode = galaxy::tgw::ApiMode::kInternetMode;  // 设置api模式 托管机房模式/互联网模式
    if (api_mode == galaxy::tgw::ApiMode::kColocationMode)
    {
        cfg.coloca_cfg.channel_mode = galaxy::tgw::ColocatChannelMode::kQTCP;
        cfg.coloca_cfg.qtcp_channel_thread = 8;
        cfg.coloca_cfg.qtcp_max_req_cnt = 1000;
    }

    galaxy::tgw::TgwPushSpi spi;
    bool is_runing = true;
    // 初始化 TGW
    int32_t ec = galaxy::tgw::ErrorCode::kSuccess;
    // if ((ec = galaxy::tgw::IGMDApi::Init(&spi, cfg, api_mode, "./")) != galaxy::tgw::ErrorCode::kSuccess) // 第四个参数可不填写，直接使用默认参数
    if ((ec = galaxy::tgw::IGMDApi::Init(&spi, cfg, api_mode)) 
        != galaxy::tgw::ErrorCode::kSuccess)
    {
        std::cout << "Init TGW faild, ErrorCode: " << ec << std::endl;
        galaxy::tgw::IGMDApi::Release();
        return -1;
    }
    // 修改密码
    // galaxy::tgw::UpdatePassWordReq req;
    // memset(&req, 0, sizeof(req));
    // strncpy_s(req.username, "*****", sizeof(req.username));
    // strncpy_s(req.old_password, "*****", sizeof(req.old_password));
    // strncpy_s(req.new_password, "*****", sizeof(req.new_password));
    // ec = galaxy::tgw::IGMDApi::UpdatePassWord(req);
    // if (ec != galaxy::tgw::ErrorCode::kSuccess)
    //     std::cout << "UpdatePassWord faild, ErrorCode: " << ec << std::endl;
    // else
    //     std::cout << "UpdatePassWord success" << std::endl;
    /*======================================推送示例======================================*/
    // // 1、常规订阅示例
    // GeneralSubscribeReq();
    // // 2、加工因子订阅示例
    // FactorSubscribeReq();

    /*======================================查询示例======================================*/
    // // 1、查询K线
    // galaxy::tgw::QueryKlineSpi* kline_spi = new galaxy::tgw::QueryKlineSpi();
    // QueryKlineReq(kline_spi);

    // // 2、查询快照
    // galaxy::tgw::QuerySnapshotSpi* snapshot_spi = new galaxy::tgw::QuerySnapshotSpi();
    // QuerySnapshotReq(snapshot_spi);

    // // 3、查询逐笔成交
    // galaxy::tgw::QueryTickExecutionSpi* tick_exec_spi = new galaxy::tgw::QueryTickExecutionSpi();
    // QueryTickExecReq(tick_exec_spi);

    // // 4、查询逐笔委托
    // galaxy::tgw::QueryTickOrderSpi* tick_order_spi = new galaxy::tgw::QueryTickOrderSpi();
    // QueryTickOrderReq(tick_order_spi);

    // // 5、查询委托队列
    // galaxy::tgw::QueryOrderQueueSpi* order_queue_spi = new galaxy::tgw::QueryOrderQueueSpi();
    // QueryOrderQueueReq(order_queue_spi);

    //  // 6、查询代码表
    //  galaxy::tgw::QueryCodeTableSpi* code_table_spi = new galaxy::tgw::QueryCodeTableSpi();
    //  QueryCodeTableReq(code_table_spi);

    // // 7、查询证券代码信息
    // galaxy::tgw::QuerySecuritiesInfoSpi* secur_info_spi = new galaxy::tgw::QuerySecuritiesInfoSpi();
    // QuerySecuritiesInfoReq(secur_info_spi);

    // // 8、查询复权因子
    // galaxy::tgw::QueryExFactorSpi* ex_fator_spi = new galaxy::tgw::QueryExFactorSpi();
    // QueryExFactorReq(ex_fator_spi);

    // // 9、查询加工因子
    // galaxy::tgw::QueryFactorSpi* factor_spi = new galaxy::tgw::QueryFactorSpi();
    // QueryFactorReq(factor_spi);

    // // 10、查询三方资讯
    // galaxy::tgw::QueryThirdInfoSpi* thirdinfo_spi = new galaxy::tgw::QueryThirdInfoSpi();
    // QueryThirdInfoReq(thirdinfo_spi);

    // // 11、查询ETF证券信息
    // galaxy::tgw::QueryETFInfoSpi* etf_info_spi = new galaxy::tgw::QueryETFInfoSpi();
    // QueryETFInfoReq(etf_info_spi);

    /*======================================回放示例======================================*/
    // // 1、回放快照
    // galaxy::tgw::ReplayHistorySpi* hSpi = new galaxy::tgw::ReplayHistorySpi();
    // ReplaySnapshotReq(hSpi);

    // // 2、回放逐笔成交
    // ReplayTickExecReq(hSpi);

    // // 3、回放k线
    // ReplayKlineReq(hSpi);

    // 这里必须保证用户的spi实例的生命周期长于TGW的API
    while (is_runing)
    {
		Sleep(3000);
        std::cout << "TGW is running ..." <<std::endl;
    }

    // 释放申请的对象（需保证在数据全部查询/回放完毕后，才可释放）
    {
        // delete kline_spi;
        // delete snapshot_spi;
        // delete tick_exec_spi;
        // delete tick_order_spi;
        // delete order_queue_spi;
        // delete code_table_spi;
        // delete internet_stock_info_spi;
        // delete coloc_stock_info_spi;
        // delete ex_fator_spi;
        // delete factor_spi;
        // delete thirdinfo_spi;
        // delete hSpi;
    }
    // 释放资源
    galaxy::tgw::IGMDApi::Release();
    return 0;
}
