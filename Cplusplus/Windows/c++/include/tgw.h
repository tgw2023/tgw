#pragma once

#include "tgw_struct.h"
#include "tgw_datatype.h"
#include "tgw_export.h"
#include <functional>

namespace galaxy { namespace tgw {

class IGMDSpi;
class IGMDHistorySpi;          // 回放接口类
class IGMDSnapshotSpi;         // 快照查询接口类
class IGMDTickOrderSpi;        // 逐笔委托查询接口类
class IGMDTickExecutionSpi;    // 逐笔成交接口类
class IGMDOrderQueueSpi;       // 委托队列接口类
class IGMDKlineSpi;            // K线查询接口类
class IGMDCodeTableSpi;        // 代码表查询接口类
class IGMDExFactorSpi;         // 复权因子查询接口类
class IGMDFactorSpi;           // 因子查询接口类
class IGMDThirdInfoSpi;        // 三方资讯查询接口类
class IGMDSecuritiesInfoSpi;   // 证券代码信息查询接口类
class IGMDETFInfoSpi;          // ETF代码信息查询接口类

class TGW_EXPORT IGMDApi
{
public:
    /**
     * @brief GetVersion            获取TGW版本信息
     * 
     * @return                      版本内容
     * @attention                   托管机房和互联网模式适用
     */
    static const char* GetVersion();

    /**
    * @brief Init                   初始化接口
    * 
    * @param spi                    IGMDSpi的继承类实例指针，调用Release函数之后，该实例才能被销毁。
    * @param cfg                    初始化所需参数
    * @param api_mode               模式选择，参照tgw_datatype.h中的ApiMode
    * @param path                   互联网模式指定证书及相关路径（无特殊用法可不填写，使用默认路径即可）
    * @return                       返回错误码，参照tgw_datatype.h中的ErrorCode
    * @attention                   托管机房和互联网模式适用
    */
    static int32_t Init(const IGMDSpi* pSpi, const Cfg& cfg, uint16_t api_mode, const std::string& path = "");

    /**
     * @brief Release               资源释放
     * 
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t Release();

    /**
     * @brief FreeMemory            释放内存函数
     * 
     * @param data                  数据指针
     * @attention                   Spi回调数据使用完成后必须调用该接口释放内存
     *                              托管机房和互联网模式适用
     */
    static void FreeMemory(void* data);

    /**
     * @brief GetTaskID             获取task_id编号
     * 
     * @return                      返回编号
     * @attention                   用于部分需要task_id入参的查询，回放
     * @attention                   托管机房和互联网模式适用
     */
    static int64_t GetTaskID();

    /** 
     * @brief UpdatePassWord        更新密码接口
     * 
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   错误码为超时kTimeoutExit则大概率是失败，仍有小概率网络问题会修改成功，需要注意该错误码
     * @attention                   托管机房和互联网模式适用（托管机房模式需开启TCP通道）
     */
    static int32_t UpdatePassWord(const UpdatePassWordReq& req);

/********************************************订阅接口********************************************/
    /**
    * @brief Subscribe              订阅请求接口
    * 
    * @param item                   订阅请求所需参数
    * @param cnt                    订阅请求个数
    * @return                       返回错误码，参照tgw_datatype.h中的ErrorCode
    * @attention                    托管机房和互联网模式适用
    */
    static int32_t Subscribe(const SubscribeItem* item, uint32_t cnt);

    /**
    * @brief UnSubscribe            取消订阅请求接口
    * 
    * @param item                   取消订阅请求所需参数
    * @param cnt                    取消订阅请求个数
    * @return                       返回错误码，参照tgw_datatype.h中的ErrorCode
    * @attention                    托管机房和互联网模式适用
    */
    static int32_t UnSubscribe(const SubscribeItem* item, uint32_t cnt);

    /**
    * @brief SubFactor              订阅因子请求接口
    * 
    * @param item                   订阅请求所需参数
    * @param cnt                    订阅请求个数
    * @return                       返回错误码，参照tgw_datatype.h中的ErrorCode
    * @attention                    托管机房和互联网模式适用
    */
    static int32_t SubFactor(const SubFactorItem* item, uint32_t cnt);

    /**
    * @brief UnSubFactor            取消订阅因子请求接口
    * 
    * @param item                   取消订阅请求所需参数
    * @param cnt                    取消订阅请求个数
    * @return                       返回错误码，参照tgw_datatype.h中的ErrorCode
    * @attention                    托管机房和互联网模式适用
    */
    static int32_t UnSubFactor(const SubFactorItem* item, uint32_t cnt);

    /**
     * @brief                       行情衍生数据订阅操作
     *
     * @param subscribe_type        订阅操作类型，请参考 SubscribeType
     * @param derived_data_type     订阅衍生数据类型，请参考 SubscribeDerivedDataType
     * @param item                  衍生数据类型对应的订阅代码数据项，具体参数请参考 SubscribeDerivedDataItem
     * @param cnt                   订阅的数据项个数
     *
     * @return                      错误码，具体错误信息请参考ErrorCode
     * @attention                   仅托管机房模式适用
     */
    static int32_t SubscribeDerivedData(int32_t subscribe_type, uint32_t derived_data_type, const SubscribeDerivedDataItem* item, uint32_t cnt);

/********************************************查询接口********************************************/
    /**
     * @brief QueryKline            k线数据查询异步接口  
     *                    
     * @param kline_spi             k线数据回调spi
     * @param req_kline             设置k线查询信息
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QueryKline(const IGMDKlineSpi* kline_spi, const ReqKline& req_kline);

    /**
     * @brief QuerySnapshot         快照数据查询异步接口(含港股委托挂单、港股经纪商席位)  
     *                    
     * @param snapshot_spi          快照数据回调spi
     * @param req_snapshot          设置快照查询信息
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QuerySnapshot(const IGMDSnapshotSpi* snapshot_spi, const ReqDefault& req_snapshot);
    
    /**
     * @brief QueryOrderQueue       委托队列查询异步接口  
     *                    
     * @param order_queue_spi       委托队列数据回调spi
     * @param req_order_queue       设置委托队列查询信息
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   仅托管机房模式适用
     */
    static int32_t QueryOrderQueue(const IGMDOrderQueueSpi* order_queue_spi, const ReqDefault& req_order_queue);
    
    /**
     * @brief QueryTickExecution    逐笔成交查询异步接口  
     *                    
     * @param tick_exec_spi         逐笔成交数据回调spi
     * @param req_tick_execution    设置逐笔成交查询信息
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QueryTickExecution(const IGMDTickExecutionSpi* tick_exec_spi, const ReqDefault& req_tick_execution);
    
    /**
     * @brief QueryTickOrder        逐笔委托查询异步接口  
     *                    
     * @param tick_order_spi        逐笔委托数据回调spi
     * @param req_tick_order        设置逐笔委托查询信息
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   仅托管机房模式适用
     */
    static int32_t QueryTickOrder(const IGMDTickOrderSpi* tick_order_spi, const ReqDefault& req_tick_order);
    
    /**
     * @brief QueryCodeTable        代码表查询异步接口  
     *                    
     * @param code_table_spi        代码表数据回调spi
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QueryCodeTable(const IGMDCodeTableSpi* code_table_spi);

    /**
     * @brief QuerySecuritiesInfo   证券代码信息数据查询异步接口  
     *                    
     * @param code_table_spi        证券代码信息数据回调spi
     * @param item                  设置证券代码信息查询请求
     * @param cnt                   证券代码信息查询请求个数
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QuerySecuritiesInfo(const IGMDSecuritiesInfoSpi* code_table_spi, const SubCodeTableItem* item, uint32_t cnt);

    /**
     * @brief QueryETFInfo          ETF代码表信息查询接口
     * 
     * @param etf_info_spi          IGMDETFInfoSpi的继承类实例指针，查询结束之后，该实例才能被销毁 
     * @return                      参照tgw_datatype.h中的ErrorCode               
     * @attention                   每次使用的etf_info_spi入参需要保证唯一性且生命周期必须持续到数据或者状态回调之后
     *                              市场当前仅沪深有效
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QueryETFInfo(const IGMDETFInfoSpi* etf_info_spi, const SubCodeTableItem* item, uint32_t cnt);


    /**
     * @brief QueryExFactorTable    复权因子查询异步接口  
     *                    
     * @param ex_factor_spi         复权因子数据回调spi
     * @param code                  复权因子查询信息
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QueryExFactorTable(const IGMDExFactorSpi* ex_factor_spi, const char* code);

    /**
     * @brief QueryFactor           加工因子查询异步接口  
     *                    
     * @param factor_spi            加工因子数据回调spi
     * @param req_factor            加工因子查询信息
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QueryFactor(const IGMDFactorSpi* factor_spi, const ReqFactor& req_factor);  

    /**
     * @brief SetThirdInfoParam     设置三方资讯查询请求接口  
     *                    
     * @param task_id               三方资讯请求编号
     * @param key                   三方资讯请求json的key
     * @param value                 三方资讯请求json的value
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t SetThirdInfoParam(int64_t task_id, const std::string& key, const std::string& value);
    
    /**
     * @brief QueryThirdInfo        三方资讯查询请求接口  
     *                    
     * @param third_info_spi        三方资讯数据回调spi
     * @param task_id               三方资讯请求编号
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   托管机房和互联网模式适用
     */
    static int32_t QueryThirdInfo(const IGMDThirdInfoSpi* third_info_spi, int64_t task_id);

/********************************************回放接口********************************************/
    /**
     * @brief ReplayKline           k线回放请求接口  
     *                    
     * @param pSpi                  k线回放数据回调spi
     * @param req_kline             k线回放请求
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   仅托管机房模式适用
     */
    static int32_t ReplayKline(const IGMDHistorySpi* pSpi, const ReqReplayKline& req_kline);
    
    /**
     * @brief ReplayRequest         快照，逐笔成交回放请求接口  
     *                    
     * @param pSpi                  快照，逐笔成交回放数据回调spi
     * @param req_replay            快照，逐笔成交回放请求
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   仅托管机房模式适用
     */
    static int32_t ReplayRequest(const IGMDHistorySpi* pSpi, const ReqReplay& req_replay);
    
    /**
     * @brief CancelTask            取消回放请求接口  
     *                    
     * @param task_id               需要取消的回放请求编号
     * @return                      返回错误码，参照tgw_datatype.h中的ErrorCode
     * @attention                   仅托管机房模式适用
     */
    static int32_t CancelTask(int64_t task_id);
};

class IGMDSpi
{
public:
    virtual ~IGMDSpi(){};

    /**
     * @brief OnLog                 接收日志数据回调
     *
     * @param level                 日志级别，具体请参考LogLevel
     * @param log                   日志内容
     * @param len                   日志内容字节长度
     * @attention                   托管机房和互联网模式适用
     */
    virtual void OnLog(const int32_t& level, const char* log, uint32_t len)
    {}

    /**
     * @brief OnLogon               接收登陆成功时的信息回调
     *
     * @param data                  登陆成功后返回的账号信息
     * @attention                   需要通过接口IGMDApi::FreeMemory释放数据
     *                              托管机房和互联网模式适用
     */
    virtual void OnLogon(LogonResponse* data)
    {IGMDApi::FreeMemory(data);}

    /**
     * @brief                       接收监控数据回调
     *
     * @param indicator             监控数据内容
     * @param len                   监控数据长度
     * @attention                   托管机房模式适用
     */
    virtual void OnIndicator(const char* indicator, uint32_t len)
    { (void)indicator; (void)len; }

    /**
     * @brief                       事件通知回调，使用者可根据该回调事件做相应的处理
     *
     * @param level                 事件级别
     * @param code                  事件代码
     * @param event_msg             事件具体信息 
     * @param len                   事件具体信息长度
     * @attention                   仅托管机房模式适用
     */
    virtual void OnEvent(uint32_t level, uint32_t code, const char* event_msg, uint32_t len)
    { (void)level; (void)code; (void)event_msg; (void)len; }

    /**
    * @brief OnMDSnapshot           处理现货快照推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDSnapshot(MDSnapshotL1* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDIndexSnapshot      处理指数快照推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDIndexSnapshot(MDIndexSnapshot* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDOptionSnapshot     处理期权快照推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDOptionSnapshot(MDOptionSnapshot* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDHKTSnapshot        处理港股通快照推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDHKTSnapshot(MDHKTSnapshot* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDAfterHourFixedPriceSnapshot        处理盘后定价交易快照推送数据
    * 
    * @param data                                   数据内容
    * @param cnt                                    数据个数
    * @attention                                    需要通过接口IGMDApi::FreeMemory释放数据
    *                                               仅互联网模式适用
    */
    virtual void OnMDAfterHourFixedPriceSnapshot(MDAfterHourFixedPriceSnapshot* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDCSIIndexSnapshot   处理中证指数快照推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDCSIIndexSnapshot(MDCSIIndexSnapshot* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDCnIndexSnapshot    处理深交所国证指数快照推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDCnIndexSnapshot(MDCnIndexSnapshot* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDHKTRealtimeLimit   处理港股通实时额度推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDHKTRealtimeLimit(MDHKTRealtimeLimit* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDHKTProductStatus   处理港股通产品状态推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDHKTProductStatus(MDHKTProductStatus* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDHKTVCM   处理港股VCM推送数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDHKTVCM(MDHKTVCM* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnMDFutureSnapshot     处理期货快照数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               仅互联网模式适用
    */
    virtual void OnMDFutureSnapshot(MDFutureSnapshot* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnKLine                处理k线数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @param kline_type             k线类型，参照tgw_datatype.h中的MDDatatype
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               托管机房和互联网模式适用
    */
    virtual void OnKLine(MDKLine* data, uint32_t cnt, uint32_t kline_type)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnSnapshotDerive       处理衍生数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               托管机房和互联网模式适用
    */
    virtual void OnSnapshotDerive(MDSnapshotDerive* data, uint32_t cnt)
    { IGMDApi::FreeMemory(data); (void)cnt; }

    /**
    * @brief OnFactor               处理因子数据
    * 
    * @param data                   数据内容
    * @param cnt                    数据个数
    * @attention                    需要通过接口IGMDApi::FreeMemory释放数据
    *                               托管机房和互联网模式适用
    */
    virtual void OnFactor(Factor* data)
    { IGMDApi::FreeMemory(data); }

    /**
    * @brief                        接收委托簿回调
    * @attention                    启用委托簿功能后盘中不能进行动态数据订阅，会影响委托簿的计算结果
    *                               仅托管机房模式适用
    *
    * @param order_book             委托簿数据列表
    */
    virtual void OnMDOrderBook(std::vector<MDOrderBook>& order_book) 
    {(void)order_book; }

    /**
    * @brief                       接收委托簿快照回调
    *
    * @param order_book_snapshots  接收委托簿快照数据
    * @param cnt                   接收委托簿快照数据条数
    * @attention                   仅托管机房模式适用
    */
    virtual void OnMDOrderBookSnapshot(MDOrderBookSnapshot* order_book_snapshots, uint32_t cnt) 
    {IGMDApi::FreeMemory(order_book_snapshots); (void)cnt; }
};

};
};