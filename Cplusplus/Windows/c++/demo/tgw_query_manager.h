#pragma once

#include <map>
#include <mutex>
#include <vector>
#include "tgw_query_spi.h"

namespace galaxy { namespace tgw {

// 存储查询请求
struct MultipleReqs
{
    ReqKline req_kline;        // 存储k线查询请求
    ReqDefault req_default;    // 存储快照、逐笔成交、逐笔委托、委托队列查询请求
    ReqFactor req_factor;      // 存储三方资讯查询请求
    char code[32];             // 复权因子表查询代码
    std::vector<SubCodeTableItem> vec_code_table_items;     // 保存个股基本信息、ETF代码表查询请求
    std::map<std::string, std::string> map_thirdinfo_req;   // 保存三方资讯请求中设置的key和value
};

class TgwQueryManager
{
public:
    TgwQueryManager() {}
    ~TgwQueryManager() {}
    static TgwQueryManager& GetRef();

    void SetQueryTaskMap(int64_t task_id, MultipleReqs& req);  // 保存各查询任务id、请求
    void DeleteQueryMap(int64_t task_id);       // 删除存储的请求
    bool FindQueryTaskId(int64_t task_id);      // 查询task_id是否存在
    MultipleReqs& GetQueryMap(int64_t task_id);    // 获取task_id对应的MultipleReqs

private:
    std::map<int64_t, MultipleReqs> map_req_;
    std::mutex mutex_req_;
};

}
}