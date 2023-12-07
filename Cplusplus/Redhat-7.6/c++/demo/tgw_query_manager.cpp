#include "tgw_query_manager.h"

namespace galaxy { namespace tgw {

TgwQueryManager& TgwQueryManager::GetRef()
{
    static TgwQueryManager manager;
    return manager;
}

void TgwQueryManager::SetQueryTaskMap(int64_t task_id, MultipleReqs& req_spi)
{
    std::lock_guard<decltype(mutex_req_)> _(mutex_req_);
    map_req_[task_id] = req_spi;
}

void TgwQueryManager::DeleteQueryMap(int64_t task_id)
{
    std::lock_guard<decltype(mutex_req_)> _(mutex_req_);
    if (map_req_.find(task_id) != map_req_.end())
    {
        map_req_.erase(task_id);
    }
}

bool TgwQueryManager::FindQueryTaskId(int64_t task_id)
{
    std::lock_guard<decltype(mutex_req_)> _(mutex_req_);
    if (map_req_.find(task_id) != map_req_.end())
        return true;
    else
        return false;
}

MultipleReqs& TgwQueryManager::GetQueryMap(int64_t task_id)
{
    std::lock_guard<decltype(mutex_req_)> _(mutex_req_);
    return map_req_[task_id];
}

}
}