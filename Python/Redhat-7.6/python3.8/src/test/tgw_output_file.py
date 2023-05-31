# coding=utf-8
from distutils.log import error
import shutil
import sys
import os
from tgw import tgw
from data_writer import DataWriter
from tgw_commom import *

depth_level1 = 5
order_queue_size = 50

class TgwOutPutFile():
    def __init__(self,dir):
        
        # 订阅
        self.push_stock_snapshot_writer = None
        self.push_index_snapshot_writer = None
        self.push_option_snapshot_writer = None
        self.push_hkt_snapshot_writer = None
        self.push_afterhour_fixprice_snapshot_writer = None
        self.push_csiindex_snapshot_writer = None
        self.push_cnindex_snapshot_writer = None
        self.push_hktreal_limit_writer = None
        self.push_hktprodu_status_writer = None
        self.push_hkt_vcm_writer = None
        self.push_future_snapshot_writer = None
        self.push_snapshot_deriver_writer = None
        self.push_order_book_snapshot_writer = None
        self.push_order_book_writer = None
        self.push_factor_writer = None
        self.push_kline_writer_map = { 
                                        tgw.MDDatatype.k1KLine: None,
                                        tgw.MDDatatype.k3KLine: None,
                                        tgw.MDDatatype.k5KLine: None,
                                        tgw.MDDatatype.k10KLine: None,
                                        tgw.MDDatatype.k15KLine: None,
                                        tgw.MDDatatype.k30KLine: None,
                                        tgw.MDDatatype.k60KLine: None,
                                        tgw.MDDatatype.k120KLine: None
                                      }
        self.push_kline_file_name_map = { 
                                        tgw.MDDatatype.k1KLine: "1MinKline.csv",
                                        tgw.MDDatatype.k3KLine: "3MinKline.csv",
                                        tgw.MDDatatype.k5KLine: "5MinKline.csv",
                                        tgw.MDDatatype.k10KLine: "10MinKline.csv",
                                        tgw.MDDatatype.k15KLine: "15MinKline.csv",
                                        tgw.MDDatatype.k30KLine: "30MinKline.csv",
                                        tgw.MDDatatype.k60KLine: "60MinKline.csv",
                                        tgw.MDDatatype.k120KLine: "120MinKline.csv"
                                      }

        # 查询
        self.query_tick_order_writer = None
        self.query_tick_excution_writer = None
        self.query_order_queue_writer = None
        self.query_code_table_writer = None
        self.query_securities_info_writer = None
        self.query_etf_info_writer = None
        self.query_exfactor_table_writer = None
        self.query_thirdinfo_data_writer = None
        self.query_snapshot_l1_writer = None
        self.query_snapshot_l2_writer = None
        self.query_index_snapshot_writer = None
        self.query_option_snapshot_writer = None
        self.query_hkt_snapshot_writer = None
        self.query_future_snapshot_writer = None
        self.query_factor_writer = None

        self.query_kline_writer_map = { 
                                        tgw.MDDatatype.k1KLine: None,
                                        tgw.MDDatatype.k3KLine: None,
                                        tgw.MDDatatype.k5KLine: None,
                                        tgw.MDDatatype.k10KLine: None,
                                        tgw.MDDatatype.k15KLine: None,
                                        tgw.MDDatatype.k30KLine: None,
                                        tgw.MDDatatype.k60KLine: None,
                                        tgw.MDDatatype.k120KLine: None,
                                        tgw.MDDatatype.kDayKline: None,
                                        tgw.MDDatatype.kWeekKline: None,
                                        tgw.MDDatatype.kMonthKline: None,
                                        tgw.MDDatatype.kSeasonKline: None,
                                        tgw.MDDatatype.kYearKline: None
                                    }
        self.query_kline_file_name_map = { 
                                            tgw.MDDatatype.k1KLine: "1MinKline.csv",
                                            tgw.MDDatatype.k3KLine: "3MinKline.csv",
                                            tgw.MDDatatype.k5KLine: "5MinKline.csv",
                                            tgw.MDDatatype.k10KLine: "10MinKline.csv",
                                            tgw.MDDatatype.k15KLine: "15MinKline.csv",
                                            tgw.MDDatatype.k30KLine: "30MinKline.csv",
                                            tgw.MDDatatype.k60KLine: "60MinKline.csv",
                                            tgw.MDDatatype.k120KLine: "120MinKline.csv",
                                            tgw.MDDatatype.kDayKline: "DayKline.csv",
                                            tgw.MDDatatype.kWeekKline: "WeekKline.csv",
                                            tgw.MDDatatype.kMonthKline: "MonthKline.csv",
                                            tgw.MDDatatype.kSeasonKline: "SeasonKline.csv",
                                            tgw.MDDatatype.kYearKline: "YearKline.csv"

                                      }
        
        # 回放
        self.replay_tick_excution_writer = None
        self.replay_snapshot_writer = None

        self.replay_kline_writer_map = { 
                                        tgw.MDDatatype.k1KLine: None,
                                        tgw.MDDatatype.k3KLine: None,
                                        tgw.MDDatatype.k5KLine: None,
                                        tgw.MDDatatype.k10KLine: None,
                                        tgw.MDDatatype.k15KLine: None,
                                        tgw.MDDatatype.k30KLine: None,
                                        tgw.MDDatatype.k60KLine: None,
                                        tgw.MDDatatype.k120KLine: None,
                                        tgw.MDDatatype.kDayKline: None
                                    }
        self.replay_kline_file_name_map = { 
                                            tgw.MDDatatype.k1KLine: "1MinKline.csv",
                                            tgw.MDDatatype.k3KLine: "3MinKline.csv",
                                            tgw.MDDatatype.k5KLine: "5MinKline.csv",
                                            tgw.MDDatatype.k10KLine: "10MinKline.csv",
                                            tgw.MDDatatype.k15KLine: "15MinKline.csv",
                                            tgw.MDDatatype.k30KLine: "30MinKline.csv",
                                            tgw.MDDatatype.k60KLine: "60MinKline.csv",
                                            tgw.MDDatatype.k120KLine: "120MinKline.csv",
                                            tgw.MDDatatype.kDayKline: "120MinKline.csv"
                                      }
        
        self.dir = dir


    def PushMDSnapshotToCsv(self,snapshot):
        #第一次有数据时创建落地文件
        try:
            if(self.push_stock_snapshot_writer == None):
                self.push_stock_snapshot_writer = DataWriter(self.dir,"StockSnapshot.csv")

                title = "market_type, security_code, variety_category, orig_time, trading_phase_code, " + \
                        "pre_close_price, open_price, high_price, low_price, last_price, close_price, " + \
                        "bid_price, bid_volume, offer_price, offer_volume, num_trades, total_volume_trade, " + \
                        "total_value_trade, IOPV, high_limited, low_limited\n"
                self.push_stock_snapshot_writer.WriteTitle(title)
            #落地数据
            bid_price = get_tgw_list_to_str(snapshot.bid_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(snapshot.bid_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(snapshot.offer_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(snapshot.offer_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            
            data_str = str(snapshot.market_type) + "," + str(snapshot.security_code) + "," + str(snapshot.variety_category) + "," + \
                    str(snapshot.orig_time) + "," + str(snapshot.trading_phase_code) + "," + \
                    str(snapshot.pre_close_price) + "," + str(snapshot.open_price) + "," + str(snapshot.high_price) + ","  + \
                    str(snapshot.low_price) + "," + str(snapshot.last_price) + "," + str(snapshot.close_price) + "," + \
                    str(bid_price) + "," + str(bid_volume) + "," + str(offer_price) + "," + str(offer_volume) + "," +\
                    str(snapshot.num_trades) + "," + str(snapshot.total_volume_trade) + "," + \
                    str(snapshot.total_value_trade) + "," + str(snapshot.IOPV) + "," + \
                    str(snapshot.high_limited) + "," + str(snapshot.low_limited) + "\n" 
            self.push_stock_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDSnapshotToCsv exception:' + str(error))
    
    def PushMDIndexSnapshotToCsv(self, data):
        try:
            if(self.push_index_snapshot_writer == None):
                self.push_index_snapshot_writer = DataWriter(self.dir,"IndexSnapshot.csv")

                title = "market_type, security_code, orig_time, trading_phase_code, pre_close_index, " + \
                        "open_index, high_index, low_index, last_index, close_index, " + \
                        "total_volume_trade, total_value_trade\n"
                self.push_index_snapshot_writer.WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.trading_phase_code)+ "," + \
                        str(data.pre_close_index)+ "," + str(data.open_index)+ "," + \
                        str(data.high_index)+ "," + str(data.low_index)+ "," + str(data.last_index)+ "," + str(data.close_index)+ "," + \
                        str(data.total_volume_trade)+ "," + str(data.total_value_trade) + "\n"
            self.push_index_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDIndexSnapshotToCsv exception:' + str(error))

    def PushMDOptionSnapshotToCsv(self, data):
        try:
            if(self.push_option_snapshot_writer == None):
                self.push_option_snapshot_writer = DataWriter(self.dir,"OptionSnapshot.csv")

                title = "market_type, security_code, orig_time, trading_phase_code, total_long_position, " + \
                    "total_volume_trade, total_value_trade, pre_settle_price, pre_close_price, " + \
                    "open_price, auction_price, auction_volume, high_price, low_price, last_price, " + \
                    "close_price, high_limited, low_limited, bid_price, bid_volume, offer_price, " + \
                    "offer_volume, settle_price, ref_price, contract_type, expire_date, " + \
                    "underlying_security_code, exercise_price\n"
                self.push_option_snapshot_writer.WriteTitle(title)

            bid_price = get_tgw_list_to_str(data.bid_price, 5, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, 5, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, 5, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, 5, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.trading_phase_code)+ "," + str(data.total_long_position)+ "," + str(data.total_volume_trade)+ "," + \
                        str(data.total_value_trade)+ "," + str(data.pre_settle_price)+ "," + str(data.pre_close_price)+ "," + \
                        str(data.open_price)+ "," + str(data.auction_price)+ "," + str(data.auction_volume)+ "," + \
                        str(data.high_price)+ "," + str(data.low_price)+ "," + str(data.last_price)+ "," + \
                        str(data.close_price)+ "," + str(data.high_limited)+ "," + str(data.low_limited)+ "," + \
                        str(bid_price)+ "," + str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                        str(data.settle_price)+ "," + str(data.ref_price)+ "," + str(data.contract_type)+ "," + \
                        str(data.expire_date)+ "," + str(data.underlying_security_code)+ "," + str(data.exercise_price) + "\n"
                        
            self.push_option_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDOptionSnapshotToCsv exception:' + str(error))

    def PushMDHKTSnapshotToCsv(self, data):
        try:
            if(self.push_hkt_snapshot_writer == None):
                self.push_hkt_snapshot_writer = DataWriter(self.dir,"HKTSnapshot.csv")
                title = "market_type, security_code, orig_time, trading_phase_code, total_volume_trade, " + \
                        "total_value_trade, pre_close_price, nominal_price, high_price, low_price, " + \
                        "last_price, bid_price, bid_volume, offer_price, offer_volume, ref_price, " + \
                        "high_limited, low_limited, bid_price_limit_up, bid_price_limit_down, " + \
                        "offer_price_limit_up, offer_price_limit_down\n"
                self.push_hkt_snapshot_writer.WriteTitle(title)
            

            bid_price = get_tgw_list_to_str(data.bid_price, 5, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, 5, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, 5, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, 5, get_tgw_intdata_by_index)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.trading_phase_code)+ "," + str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "," + \
                        str(data.pre_close_price)+ "," + str(data.nominal_price)+ "," + str(data.high_price)+ "," + \
                        str(data.low_price)+ "," + str(data.last_price)+ "," + str(bid_price)+ "," + \
                        str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                        str(data.ref_price)+ "," + str(data.high_limited)+ "," + str(data.low_limited)+ "," + \
                        str(data.bid_price_limit_up)+ "," + str(data.bid_price_limit_down) + "," + \
                        str(data.offer_price_limit_up) + "," + str(data.offer_price_limit_down) + "\n"
                        
            self.push_hkt_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDHKTSnapshotToCsv exception:' + str(error))

    def PushMDAfterHourFixedPriceSnapshotToCsv(self, data):
        try:
            if(self.push_afterhour_fixprice_snapshot_writer == None):
                self.push_afterhour_fixprice_snapshot_writer = DataWriter(self.dir,"AfterHourFixPriceSnapshot.csv")
                title = "market_type, security_code, variety_category, orig_time,  trading_phase_code, " + \
                        "close_price, bid_price, bid_volume, offer_price, offer_volume, pre_close_price, " + \
                        "num_trades, total_volume_trade, total_value_trade\n"
                self.push_afterhour_fixprice_snapshot_writer.WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.variety_category)+ "," + \
                        str(data.orig_time)+ "," + str(data.trading_phase_code)+ "," + str(data.close_price)+ "," + \
                        str(data.bid_price)+ "," + str(data.bid_volume)+ "," + str(data.offer_price)+ "," + \
                        str(data.offer_volume)+ "," + str(data.pre_close_price)+ "," + str(data.num_trades)+ "," + \
                        str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "\n"
            self.push_afterhour_fixprice_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDAfterHourFixedPriceSnapshotToCsv exception:' + str(error))
        

    def PushMDCSIIndexSnapshotToCsv(self, data):
        try:
            if(self.push_csiindex_snapshot_writer == None):
                self.push_csiindex_snapshot_writer = DataWriter(self.dir,"CSIIndexSnapshot.csv")
                title = "market_type, index_market, security_code, orig_time, last_index, open_index, " + \
                        "high_index, low_index, close_index, pre_close_index, change, ratio_of_change, " + \
                        "total_volume_trade, total_value_trade, exchange_rate, currency_symbol\n"
                self.push_csiindex_snapshot_writer.WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.index_market)+ "," + str(data.security_code)+ "," + \
                        str(data.orig_time)+ "," + str(data.last_index)+ "," + str(data.open_index)+ "," + \
                        str(data.high_index)+ "," + str(data.low_index)+ "," + str(data.close_index)+ "," + \
                        str(data.pre_close_index)+ "," + str(data.change)+ "," + str(data.ratio_of_change)+ "," + \
                        str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "," + str(data.exchange_rate)+ "," + \
                        str(data.currency_symbol)+ "\n"
            self.push_csiindex_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDCSIIndexSnapshotToCsv exception:' + str(error))

    def PushMDCnIndexSnapshotToCsv(self, data):
        try:
            if(self.push_cnindex_snapshot_writer == None):
                self.push_cnindex_snapshot_writer = DataWriter(self.dir,"CnIndexSnapshot.csv") 
                title = "market_type, security_code, orig_time, trading_phase_code, pre_close_index, " + \
                        "open_index, high_index, low_index, last_index, close_index, " + \
                        "total_volume_trade, total_value_trade\n"
                self.push_cnindex_snapshot_writer.WriteTitle(title)
            
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.trading_phase_code)+ "," + str(data.pre_close_index)+ "," + str(data.open_index)+ "," + \
                        str(data.high_index)+ "," + str(data.low_index)+ "," + \
                        str(data.last_index)+ "," + str(data.close_index) + "," + \
                        str(data.total_volume_trade)+ "," + str(data.total_value_trade) + "\n"
            self.push_cnindex_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDCnIndexSnapshotToCsv exception:' + str(error))

    def PushMHKTRealLimitToCsv(self, data):
        try:
            if(self.push_hktreal_limit_writer == None):
                self.push_hktreal_limit_writer = DataWriter(self.dir,"HKTRealLimit.csv")
                title = "market_type, orig_time, threshold_amount, " + \
                        "pos_amt, amount_status, mkt_status\n"

                self.push_hktreal_limit_writer.WriteTitle(title)
            data_str = str(data.market_type)+ "," + str(data.orig_time)+ "," + str(data.threshold_amount)+ "," + \
                        str(data.pos_amt)+ "," + \
                        str(data.amount_status)+ "," + \
                        str(data.mkt_status)+ "\n"
            self.push_hktreal_limit_writer.WriteData(data_str)
        except Exception as error:
            print('PushMHKTRealLimitToCsv exception:' + str(error))
    def PushMDHKTProduStatusToCsv(self, data):
        try:
            if(self.push_hktprodu_status_writer == None):
                self.push_hktprodu_status_writer = DataWriter(self.dir,"HKTProduStatus.csv")
                title = "market_type, security_code, orig_time, " + \
                        "trading_status1, trading_status2\n"
                self.push_hktprodu_status_writer.WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + \
                str(data.orig_time)+ "," + str(data.trading_status1)+ "," + str(data.trading_status2)+ "\n" 
            self.push_hktprodu_status_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDHKTProduStatusToCsv exception:' + str(error))
    

    def PushMDHKTVCMToCsv(self, data):
        try:
            if(self.push_hkt_vcm_writer == None):
                self.push_hkt_vcm_writer = DataWriter(self.dir,"HKTVCM.csv")
                title = "market_type, security_code, orig_time, " + \
                        "start_time, end_time, ref_price, low_price, high_price\n"
                self.push_hkt_vcm_writer.WriteTitle(title)
            
            data_str =  str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.start_time)+ "," + str(data.end_time)+ "," + str(data.ref_price)+ "," + \
                        str(data.low_price)+ "," + str(data.high_price)+ "\n"
            self.push_hkt_vcm_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDHKTVCMToCsv exception:' + str(error))

    def PushMDFutureSnapshotToCsv(self, data):
        try:
            if(self.push_future_snapshot_writer == None):
                self.push_future_snapshot_writer = DataWriter(self.dir,"FutureSnapshot.csv")
                title = "market_type, security_code, orig_time, action_day, last_price, pre_settle_price, pre_close_price, " + \
                        "pre_open_interest, open_price, high_price, low_price, total_volume_trade, total_value_trade, " + \
                        "open_interest, close_price, settle_price, high_limited, low_limited, pre_delta, curr_delta, bid_price, " + \
                        "bid_volume, offer_price, offer_volume, average_price, trading_day, variety_category, latest_volume_trade, " + \
                        "init_volume_trade, change_volume_trade, bid_imply_volume, offer_imply_volume, total_bid_volume_trade, " + \
                        "total_ask_volume_trade, exchange_inst_id\n"
                self.push_future_snapshot_writer.WriteTitle(title)

            bid_price = get_tgw_list_to_str(data.bid_price, 5, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, 5, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, 5, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, 5, get_tgw_intdata_by_index)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.action_day)+ "," + str(data.last_price)+ "," + str(data.pre_settle_price)+ "," + \
                        str(data.pre_close_price)+ "," + str(data.pre_open_interest)+ "," + str(data.open_price)+ "," + \
                        str(data.high_price)+ "," + str(data.low_price)+ "," + str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "," + \
                        str(data.open_interest)+ "," + str(data.close_price)+ "," + str(data.settle_price)+ "," + \
                        str(data.high_limited)+ "," + str(data.low_limited)+ "," +str(data.pre_delta)+ "," + str(data.curr_delta) + "," + \
                        str(bid_price)+ "," + str(bid_volume)+ "," +str(offer_price)+ "," + str(offer_volume) + "," + \
                        str(data.average_price)+ "," + str(data.trading_day)+ "," + str(data.variety_category)+ "," + \
                        str(data.latest_volume_trade)+ "," + str(data.init_volume_trade)+ "," + str(data.change_volume_trade)+ "," + \
                        str(data.bid_imply_volume)+ "," + str(data.offer_imply_volume)+ "," + str(data.total_bid_volume_trade)+ "," + \
                        str(data.total_ask_volume_trade)+ "," + str(data.exchange_inst_id)+ "\n" 
                        
            self.push_future_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDFutureSnapshotToCsv exception:' + str(error))

    def PushMDSnapshotDeriveToCsv(self, data):
        try:
            if(self.push_snapshot_deriver_writer == None):
                self.push_snapshot_deriver_writer = DataWriter(self.dir,"SnapshotDerive.csv")
                title = "market_type, security_code, orig_time, average_price, " + \
                        "circulation_value, total_value, initiative_buy_volume, initiative_sell_volume, " + \
                        "turnover_rate, volume_ratio, ask_bid_ratio, amplitude, PE_static, PE_dynamic, " + \
                        "PE_TTM, PB, entrustment_diff, initiative_flag\n"
                self.push_snapshot_deriver_writer.WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                    str(data.average_price)+ "," + str(data.circulation_value)+ "," + \
                    str(data.total_value)+ "," + str(data.initiative_buy_volume)+ "," + \
                    str(data.initiative_sell_volume)+ "," + str(data.turnover_rate)+ "," + \
                    str(data.volume_ratio)+ "," + str(data.ask_bid_ratio)+ "," + \
                    str(data.amplitude)+ "," + str(data.PE_static)+ "," + \
                    str(data.PE_dynamic)+ "," + str(data.PE_TTM)+ "," + \
                    str(data.PB)+ "," + str(data.entrustment_diff)+ "," + \
                    str(data.initiative_flag)+ "\n" 
            self.push_snapshot_deriver_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDSnapshotDeriveToCsv exception:' + str(error))

    def PushMFactorToCsv(self, data):
        try:
            if(self.push_factor_writer == None):
                self.push_factor_writer = DataWriter(self.dir,"Factor.csv")
                title = "data, size\n" 
                self.push_factor_writer.WriteTitle(title)
            data_str = str(data.json_buf)[:data.data_size] + "," + str(data.data_size)+ "\n" 
            self.push_factor_writer.WriteData(data_str)
        except Exception as error:
            print('PushMFactorToCsv exception:' + str(error))

    def PushMDOrderBookSnapshotToCsv(self, data):
        try:
            if(self.push_order_book_snapshot_writer == None):
                self.push_order_book_snapshot_writer = DataWriter(self.dir,"OrderBookSnapshot.csv")
                title = "market_type, variety_category, " + \
                        "security_code, last_tick_seq, channel_no, " + \
                        "orig_time, last_price, total_num_trades, total_volume_trade, " + \
                        "total_value_trade, total_bid_volume, total_offer_volume, " + \
                        "num_bid_orders, num_offer_orders, " + \
                        "bid_price, bid_volume, offer_price, offer_volume\n"
                self.push_order_book_snapshot_writer.WriteTitle(title)

            #落地数据
            bid_price = get_tgw_list_to_str(data.bid_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)

            data_str = str(data.market_type) + "," + str(data.variety_category) + "," + str(data.security_code) + "," + \
                    str(data.last_tick_seq) + "," + str(data.channel_no) + "," + str(data.orig_time) + "," + \
                    str(data.last_price) + "," + str(data.total_num_trades) + ","  + str(data.total_volume_trade) + "," + \
                    str(data.total_value_trade) + "," + str(data.total_bid_volume) + "," + str(data.total_offer_volume) + "," + \
                    str(data.num_bid_orders) + "," + str(data.num_offer_orders) + "," + \
                    str(bid_price) + "," + str(bid_volume) + "," + str(offer_price) + "," + str(offer_volume) + "\n"
            self.push_order_book_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDOrderBookSnapshotToCsv exception:' + str(error))

    def PushMDOrderBookToCsv(self, data):
        try:
            if(self.push_order_book_writer == None):
                self.push_order_book_writer = DataWriter(self.dir,"OrderBook.csv")
                title = "channel_no, market_type, security_code, last_tick_time, last_snapshot_time, last_tick_seq, " + \
                        "bid_order_book, offer_order_book, " + \
                        "total_num_trades, total_volume_trade, total_value_trade, last_price\n"
                self.push_order_book_writer.WriteTitle(title)

            bid_order_book = data.bid_order_book
            cnt_bid = tgw.Tools_GetDataSize(bid_order_book)
            str_bid_order_book = ""
            for j in range(cnt_bid):
                bid_data = tgw.Tools_GetDataByIndex(bid_order_book, j)
                str_bid_order_book += SerializeMDOrderBookItem(bid_data) + ","

            offer_order_book = data.offer_order_book
            cnt_offer = tgw.Tools_GetDataSize(offer_order_book)
            str_offer_order_book = ""
            for j in range(cnt_offer):
                offer_data = tgw.Tools_GetDataByIndex(offer_order_book, j)
                str_offer_order_book += SerializeMDOrderBookItem(offer_data) + ","

            data_str = str(data.channel_no) + "," + str(data.market_type) + "," + str(data.security_code) + "," + \
                    str(data.last_tick_time) + "," + str(data.last_snapshot_time) + "," + str(data.last_tick_seq) + "," + \
                    str(str_bid_order_book) + str(str_offer_order_book) + \
                    str(data.total_num_trades) + "," + str(data.total_volume_trade) + "," + str(data.total_value_trade) + "," + str(data.last_price) + "\n"
            self.push_order_book_writer.WriteData(data_str)
        except Exception as error:
            print('PushMDOrderBookToCsv exception:' + str(error))

    def PushMDKlineToCsv(self, data, kline_type):
        try:
            if(self.push_kline_writer_map[kline_type] == None):
                self.push_kline_writer_map[kline_type] = DataWriter(self.dir, self.push_kline_file_name_map[kline_type])
                title = "market_type, security_code, orig_time, " + \
                        "kline_time, open_price, high_price, low_price, " + \
                        "close_price, volume_trade, value_trade\n"
                self.push_kline_writer_map[kline_type].WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.kline_time)+ "," + str(data.open_price)+ "," + str(data.high_price)+ "," + \
                        str(data.low_price)+ "," + str(data.close_price)+ "," + \
                        str(data.volume_trade)+ "," + str(data.value_trade)+ "\n" 
            self.push_kline_writer_map[kline_type].WriteData(data_str)
        except Exception as error:
            print('PushMDKlineToCsv exception:' + str(error))

    def QueryMDTickOrderToCsv(self, data):
        try:
            if(self.query_tick_order_writer == None):
                self.query_tick_order_writer = DataWriter(self.dir,"TickOrder.csv")
                title = "market_type, security_code, appl_seq_num, channel_no, order_time, " + \
                        "order_price, order_volume, side, order_type, md_stream_id, product_status, " + \
                        "orig_order_no, biz_index\n"
                self.query_tick_order_writer.WriteTitle(title)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.appl_seq_num)+ "," + \
                        str(data.channel_no)+ "," + str(data.order_time)+ "," + str(data.order_price)+ "," + str(data.order_volume)+ "," + \
                        str(data.side)+ "," + str(data.order_type)+ "," + str(data.md_stream_id)+ "," + \
                        str(data.product_status)+ "," + str(data.orig_order_no)+ "," + str(data.biz_index)+ "\n"
            self.query_tick_order_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDTickOrderToCsv exception:' + str(error))
        

    def QueryMDTickExecutionToCsv(self, data):
        try:
            if(self.query_tick_excution_writer == None):
                self.query_tick_excution_writer = DataWriter(self.dir,"TickExecution.csv")
                title = "market_type, security_code, exec_time, channel_no, appl_seq_num, " + \
                        "exec_price, exec_volume, value_trade, offer_appl_seq_num, side, exec_type, " + \
                        "md_stream_id, biz_index, variety_category\n"
                self.query_tick_excution_writer.WriteTitle(title)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.exec_time)+ "," + \
                        str(data.channel_no)+ "," + str(data.appl_seq_num)+ "," + str(data.exec_price)+ "," + \
                        str(data.exec_volume)+ "," + str(data.value_trade)+ "," + str(data.bid_appl_seq_num)+ "," + \
                        str(data.offer_appl_seq_num)+ "," + str(chr(data.side))+ "," + str(chr(data.exec_type))+ "," + str(data.md_stream_id) +"," + \
                        str(data.biz_index)+ "," + str(data.variety_category) + "\n"

            self.query_tick_excution_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDTickExecutionToCsv exception:' + str(error))
        

    def QueryMDOrderQueueToCsv(self, data):
        try:
            if(self.query_order_queue_writer == None):
                self.query_order_queue_writer = DataWriter(self.dir,"OrderQueue.csv")
                title = "market_type, security_code, order_time, side, order_price, " + \
                        "order_volume, num_of_orders, items, volume, channel_no, md_stream_id\n"
                self.query_order_queue_writer.WriteTitle(title)
            
            volume = get_tgw_list_to_str(data.volume, 50, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.order_time)+ "," + \
                    str(chr(data.side))+ "," + str(data.order_price)+ "," + str(data.order_volume)+ "," + str(data.num_of_orders)+ "," + \
                    str(data.items)+ "," + \
                    str(volume) + "," + \
                    str(data.channel_no)+ "," + str(data.md_stream_id)+ "\n" 
            self.query_order_queue_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDOrderQueueToCsv exception:' + str(error))

    def QueryMDCodeTableToCsv(self, data):
        try:
            if(self.query_code_table_writer == None):
                self.query_code_table_writer = DataWriter(self.dir,"CodeTable.csv")
                title = "security_code, symbol, english_name, market_type, security_type, " + \
                        "currency\n"
                self.query_code_table_writer.WriteTitle(title)
            data_str = str(data.security_code)+ "," + str(data.symbol)+ "," + \
                    str(data.english_name)+ "," + str(data.market_type)+ "," + \
                    str(data.security_type)+ "," + str(data.currency) + "\n"
            self.query_code_table_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDCodeTableToCsv exception:' + str(error))
        

    def QueryMDSecuritiesInfoToCsv(self, data):
        try:
            if(self.query_securities_info_writer == None):
                self.query_securities_info_writer = DataWriter(self.dir,"SecuritiesInfo.csv")
                title = "security_code, market_type, symbol, english_name, security_type, currency, variety_category, " + \
                        "pre_close_price, underlying_security_id, contract_type, exercise_price, expire_date, " + \
                        "high_limited, low_limited, security_status, price_tick, buy_qty_unit, sell_qty_unit, " + \
                        "market_buy_qty_unit, market_sell_qty_unit, buy_qty_lower_limit, buy_qty_upper_limit, " + \
                        "sell_qty_lower_limit, sell_qty_upper_limit, market_buy_qty_lower_limit, market_buy_qty_upper_limit, " + \
                        "market_sell_qty_lower_limit, market_sell_qty_upper_limit, list_day, par_value, outstanding_share, " + \
                        "public_float_share_quantity, contract_multiplier, regular_share, interest, coupon_rate, product_code, " + \
                        "delivery_year, delivery_month, create_date, start_deliv_date, end_deliv_date, position_type\n"
                self.query_securities_info_writer.WriteTitle(title)
            data_str = str(data.security_code)+ "," + str(data.market_type)+ "," + str(data.symbol)+ "," + \
                    str(data.english_name)+ "," + str(data.security_type)+ "," + str(data.currency)+ "," + \
                    str(data.variety_category)+ "," + str(data.pre_close_price)+ "," + str(data.underlying_security_id)+ "," +\
                    str(data.contract_type)+ "," + str(data.exercise_price)+ "," + str(data.expire_date)+ "," +\
                    str(data.high_limited)+ "," + str(data.low_limited)+ "," + str(data.security_status)+ "," +\
                    str(data.price_tick)+ "," + str(data.buy_qty_unit)+ "," + str(data.sell_qty_unit)+ "," +\
                    str(data.market_buy_qty_unit)+ "," + str(data.market_sell_qty_unit)+ "," + str(data.buy_qty_lower_limit)+ "," +\
                    str(data.buy_qty_upper_limit)+ "," + str(data.sell_qty_lower_limit)+ "," + str(data.sell_qty_upper_limit)+ "," +\
                    str(data.market_buy_qty_lower_limit)+ "," + str(data.market_buy_qty_upper_limit)+ "," + str(data.market_sell_qty_lower_limit)+ "," +\
                    str(data.market_sell_qty_upper_limit)+ "," + str(data.list_day)+ "," + str(data.par_value)+ "," +\
                    str(data.outstanding_share)+ "," + str(data.public_float_share_quantity)+ "," + str(data.contract_multiplier)+ "," +\
                    str(data.regular_share)+ "," + str(data.interest)+ "," + str(data.coupon_rate)+ "," +\
                    str(data.product_code)+ "," + str(data.delivery_year)+ "," + str(data.delivery_month)+ "," +\
                    str(data.create_date)+ "," + str(data.start_deliv_date)+ "," + str(data.end_deliv_date)+ "," +\
                    str(data.position_type)+ "\n"
            self.query_securities_info_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDSecuritiesInfoToCsv exception:' + str(error))
        
    def QueryMDETFInfoToCsv(self, data):
        try:
            if(self.query_etf_info_writer == None):
                self.query_etf_info_writer = DataWriter(self.dir,"ETFInfo.csv")
                title = "security_code, creation_redemption_unit, max_cash_ratio, publish, creation, redemption, " + \
                        "creation_redemption_switch, record_num, total_record_num, estimate_cash_component, trading_day, " + \
                        "pre_trading_day, cash_component, nav_per_cu, nav, market_type, symbol, fund_management_company, " + \
                        "underlying_security_id, underlying_security_id_source, dividend_per_cu, creation_limit, " + \
                        "redemption_limit, creation_limit_per_user, redemption_limit_per_user, net_creation_limit, " + \
                        "net_redemption_limit, net_creation_limit_per_user, net_redemption_limit_per_user, all_cash_flag, " + \
                        "all_cash_amount, all_cash_premium_rate, all_cash_discount_rate, rtgs_flag, reserved, " + \
                        "constituent_stock_infos.security_code, constituent_stock_infos.market_type, " + \
                        "constituent_stock_infos.underlying_symbol, constituent_stock_infos.component_share, " + \
                        "constituent_stock_infos.substitute_flag, constituent_stock_infos.premium_ratio, " + \
                        "constituent_stock_infos.discount_ratio, constituent_stock_infos.creation_cash_substitute, " + \
                        "constituent_stock_infos.redemption_cash_substitute, constituent_stock_infos.substitution_cash_amount, " + \
                        "constituent_stock_infos.underlying_security_id, constituent_stock_infos.buy_or_sell_to_open, " + \
                        "constituent_stock_infos.reserved\n"
                self.query_etf_info_writer.WriteTitle(title)
            cnt = tgw.Tools_GetDataSize(data.constituent_stock_infos)
            str_constituent_all = ""
            for i in range(cnt):
                constituent = tgw.Tools_GetDataByIndex(data.constituent_stock_infos, i)
                str_constituent = str("constituent_stock_infos[") + str(i) + str("]:") + str(constituent.security_code) + "," + str(constituent.market_type) + "," + str(constituent.underlying_symbol) + "," +\
                    str(constituent.component_share) + "," + str(constituent.substitute_flag) + "," + str(constituent.premium_ratio) + "," +\
                    str(constituent.discount_ratio) + "," + str(constituent.creation_cash_substitute) + "," + str(constituent.redemption_cash_substitute) + "," +\
                    str(constituent.substitution_cash_amount) + "," + str(constituent.underlying_security_id) + "," + str(constituent.buy_or_sell_to_open) + "," +\
                    str(constituent.reserved) + "\n"
                str_constituent_all += str_constituent
            data_str = str(data.security_code)+ "," + str(data.creation_redemption_unit)+ "," + str(data.max_cash_ratio)+ "," + \
                    str(data.publish)+ "," + str(data.creation)+ "," + str(data.redemption)+ "," + \
                    str(data.creation_redemption_switch)+ "," + str(data.record_num)+ "," + str(data.total_record_num)+ "," + \
                    str(data.estimate_cash_component)+ "," + str(data.trading_day)+ "," + str(data.pre_trading_day)+ "," + \
                    str(data.cash_component)+ "," + str(data.nav_per_cu)+ "," + str(data.nav)+ "," + \
                    str(data.market_type)+ "," + str(data.symbol)+ "," + str(data.fund_management_company)+ "," + \
                    str(data.underlying_security_id)+ "," + str(data.underlying_security_id_source)+ "," + str(data.dividend_per_cu)+ "," + \
                    str(data.creation_limit)+ "," + str(data.redemption_limit)+ "," + str(data.creation_limit_per_user)+ "," + \
                    str(data.redemption_limit_per_user)+ "," + str(data.net_creation_limit)+ "," + str(data.net_redemption_limit)+ "," + \
                    str(data.net_creation_limit_per_user)+ "," + str(data.net_redemption_limit_per_user)+ "," + str(data.all_cash_flag)+ "," + \
                    str(data.all_cash_amount)+ "," + str(data.all_cash_premium_rate)+ "," + str(data.all_cash_discount_rate)+ "," + \
                    str(data.rtgs_flag)+ "," + str(data.reserved) + "\n" +\
                    str(str_constituent_all)
            self.query_etf_info_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDETFInfoToCsv exception:' + str(error))

    def QueryMDExFactorTableTosv(self, data):
        try:
            if(self.query_exfactor_table_writer == None):
                self.query_exfactor_table_writer = DataWriter(self.dir,"ExFactorTable.csv")
                title = "inner_code, security_code, ex_date, ex_factor, cum_factor\n"
                self.query_exfactor_table_writer.WriteTitle(title)
            data_str = str(data.inner_code) + "," + str(data.security_code) + "," + \
                        str(data.ex_date) + "," + str(format(data.ex_factor, '.16f'))  + "," + str(format(data.cum_factor, '.16f')) + "\n" 
            self.query_exfactor_table_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDExFactorTableTosv exception:' + str(error))
        

    def QueryMDThirdInfoDataToCsv(self, data):
        try:
            if(self.query_thirdinfo_data_writer == None):
                self.query_thirdinfo_data_writer = DataWriter(self.dir,"ThirdInfoData.csv")
                title = "task_id, data_size, json_data\n"
                self.query_thirdinfo_data_writer.WriteTitle(title)
            
            data_str = str(data.task_id)+ "," + str(data.data_size)+ "," + str(data.json_data)[:data.data_size] + "\n"
            self.query_thirdinfo_data_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDThirdInfoDataToCsv exception:' + str(error))
        

    def QueryMDStockSnapshotL1ToCsv(self, data):
        try:
            if(self.query_snapshot_l1_writer == None):
                self.query_snapshot_l1_writer = DataWriter(self.dir,"StockSnapshotL1.csv")
                title = "market_type, security_code, variety_category, orig_time, trading_phase_code, " + \
                        "pre_close_price, open_price, high_price, low_price, last_price, close_price, " + \
                        "bid_price, bid_volume, offer_price, offer_volume, num_trades, " + \
                        "total_volume_trade, total_value_trade, IOPV, high_limited, low_limited\n"

                self.query_snapshot_l1_writer.WriteTitle(title)

            bid_price = get_tgw_list_to_str(data.bid_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.variety_category)+ "," + str(data.orig_time)+ "," + \
                    str(data.trading_phase_code)+ "," + str(data.pre_close_price)+ "," + str(data.open_price)+ "," + str(data.high_price)+ "," + \
                    str(data.low_price)+ "," + str(data.last_price)+ "," + str(data.close_price)+ "," + \
                    str(bid_price)+ "," + str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                    str(data.num_trades)+ "," + str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "," + \
                    str(data.IOPV)+ "," + str(data.high_limited)+ "," + str(data.low_limited)+ "\n"
                    
            self.query_snapshot_l1_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDStockSnapshotL1ToCsv exception:' + str(error))

    def QueryMDStockSnapshotL2ToCsv(self, data):
        try:
            if(self.query_snapshot_l2_writer == None):
                self.query_snapshot_l2_writer = DataWriter(self.dir,"StockSnapshotL2.csv")
                title = "market_type, security_code, orig_time, trading_phase_code, " + \
                        "pre_close_price, open_price, high_price, low_price, last_price, close_price, " + \
                        "bid_price, bid_volume, offer_price, offer_volume, num_trades, total_volume_trade, " + \
                        "total_value_trade, total_bid_volume, total_offer_volume, weighted_avg_bid_price, " + \
                        "weighted_avg_offer_price, IOPV, yield_to_maturity, high_limited, low_limited, " + \
                        "price_earning_ratio1, price_earning_ratio2, change1, change2\n"
                self.query_snapshot_l2_writer.WriteTitle(title)

            bid_price = get_tgw_list_to_str(data.bid_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                    str(data.trading_phase_code)+ "," + str(data.pre_close_price)+ "," + str(data.open_price)+ "," + str(data.high_price)+ "," + \
                    str(data.low_price)+ "," + str(data.last_price)+ "," + str(data.close_price)+ "," + \
                    str(bid_price)+ "," + str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                    str(data.num_trades)+ "," + str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "," + \
                    str(data.total_bid_volume)+ "," + str(data.total_offer_volume)+ "," + str(data.weighted_avg_bid_price)+ "," + \
                    str(data.weighted_avg_offer_price)+ "," + str(data.IOPV)+ "," + str(data.yield_to_maturity)+ "," + \
                    str(data.high_limited)+ "," + str(data.low_limited)+ "," + str(data.price_earning_ratio1)+ "," + \
                    str(data.price_earning_ratio2)+ "," + str(data.change1)+ "," + str(data.change2)+ "\n"
            self.query_snapshot_l2_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDStockSnapshotL2ToCsv exception:' + str(error))

    def QueryMDIndexSnapshotToCsv(self, data):
        try:
            if(self.query_index_snapshot_writer == None):
                self.query_index_snapshot_writer = DataWriter(self.dir,"IndexSnapshot.csv")
                title = "market_type, security_code, orig_time, trading_phase_code, pre_close_index, " + \
                        "open_index, high_index, low_index, last_index, close_index, " + \
                        "total_volume_trade, total_value_trade\n" 
                self.query_index_snapshot_writer.WriteTitle(title)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.trading_phase_code)+ "," + str(data.pre_close_index)+ "," + \
                        str(data.open_index)+ "," + str(data.high_index)+ "," + \
                        str(data.low_index)+ "," + str(data.last_index)+ "," + \
                        str(data.close_index)+ "," + str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "\n"
            self.query_index_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDIndexSnapshotToCsv exception:' + str(error))

    def QueryMDOptionSnapshotToCsv(self, data):
        try:
            if(self.query_option_snapshot_writer == None):
                self.query_option_snapshot_writer = DataWriter(self.dir,"OptionSnapshot.csv")
                title = "market_type, security_code, orig_time, trading_phase_code, total_long_position, " + \
                        "total_volume_trade, total_value_trade, pre_settle_price, pre_close_price, " + \
                        "open_price, auction_price, auction_volume, high_price, low_price, last_price, " + \
                        "close_price, high_limited, low_limited, bid_price, bid_volume, offer_price, " + \
                        "offer_volume, settle_price, ref_price, contract_type, expire_date, " + \
                        "underlying_security_code, exercise_price\n"
                self.query_option_snapshot_writer.WriteTitle(title)

            bid_price = get_tgw_list_to_str(data.bid_price, 5, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, 5, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, 5, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, 5, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + \
                    str(data.orig_time)+ "," + str(data.trading_phase_code)+ "," + \
                    str(data.total_long_position)+ "," + str(data.total_volume_trade)+ "," + \
                    str(data.total_value_trade)+ "," + str(data.pre_settle_price)+ "," + \
                    str(data.pre_close_price)+ "," + str(data.open_price)+ "," + \
                    str(data.auction_price)+ "," + str(data.auction_volume)+ "," + \
                    str(data.high_price)+ "," + str(data.low_price)+ "," + \
                    str(data.last_price)+ "," + str(data.close_price)+ "," + \
                    str(data.high_limited)+ "," + str(data.low_limited)+ "," + \
                    str(bid_price)+ "," + str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                    str(data.settle_price)+ "," + str(data.ref_price)+ "," + \
                    str(data.contract_type)+ "," + str(data.expire_date)+ "," + \
                    str(data.underlying_security_code)+ "," + str(data.exercise_price)+ "\n" 

            self.query_option_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDOptionSnapshotToCsv exception:' + str(error))

    def QueryMDHKTSnapshotToCsv(self, data):
        try:
            if(self.query_hkt_snapshot_writer == None):
                self.query_hkt_snapshot_writer = DataWriter(self.dir,"HKTSnapshot.csv")
                title = "market_type, security_code, orig_time, trading_phase_code, total_volume_trade, " + \
                        "total_value_trade, pre_close_price, nominal_price, high_price, low_price, " + \
                        "last_price, bid_price, bid_volume, offer_price, offer_volume, ref_price, " + \
                        "high_limited, low_limited, bid_price_limit_up, bid_price_limit_down, "  + \
                        "offer_price_limit_up, offer_price_limit_down\n"
                self.query_hkt_snapshot_writer.WriteTitle(title)

            bid_price = get_tgw_list_to_str(data.bid_price, 5, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, 5, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, 5, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, 5, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + \
                    str(data.security_code)+ "," + \
                    str(data.orig_time)+ "," + \
                    str(data.trading_phase_code)+ "," + \
                    str(data.total_volume_trade)+ "," + \
                    str(data.total_value_trade)+ "," + \
                    str(data.pre_close_price)+ "," + \
                    str(data.nominal_price)+ "," + \
                    str(data.high_price)+ "," + \
                    str(data.low_price)+ "," + \
                    str(data.last_price)+ "," + \
                    str(bid_price)+ "," + str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                    str(data.ref_price)+ "," + \
                    str(data.high_limited)+ "," + \
                    str(data.low_limited)+ "," + \
                    str(data.bid_price_limit_up)+ "," + \
                    str(data.bid_price_limit_down)+ "," + \
                    str(data.offer_price_limit_up)+ "," + \
                    str(data.offer_price_limit_down) + "\n"
            self.query_hkt_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDHKTSnapshotToCsv exception:' + str(error))

    def QueryMDFutureSnapshotToCsv(self, data):
        try:
            if(self.query_future_snapshot_writer == None):
                self.query_future_snapshot_writer = DataWriter(self.dir,"FutureSnapshot.csv")
                title = "market_type, security_code, orig_time, action_day, last_price, pre_settle_price, pre_close_price, " + \
                        "pre_open_interest, open_price, high_price, low_price, total_volume_trade, total_value_trade, " + \
                        "open_interest, close_price, settle_price, high_limited, low_limited, pre_delta, curr_delta, bid_price, " + \
                        "bid_volume, offer_price, offer_volume, average_price, trading_day, variety_category, latest_volume_trade, " + \
                        "init_volume_trade, change_volume_trade, bid_imply_volume, offer_imply_volume, total_bid_volume_trade, " + \
                        "total_ask_volume_trade, exchange_inst_id\n"
                self.query_future_snapshot_writer.WriteTitle(title)
            
            bid_price = get_tgw_list_to_str(data.bid_price, 5, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, 5, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, 5, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, 5, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + \
                    str(data.security_code)+ "," + \
                    str(data.orig_time)+ "," + \
                    str(data.action_day)+ "," + \
                    str(data.last_price)+ "," + \
                    str(data.pre_settle_price)+ "," + \
                    str(data.pre_close_price)+ "," + \
                    str(data.pre_open_interest)+ "," + \
                    str(data.open_price)+ "," + \
                    str(data.high_price)+ "," + \
                    str(data.low_price)+ "," + \
                    str(data.total_volume_trade)+ "," + \
                    str(data.total_value_trade)+ "," + \
                    str(data.open_interest)+ "," + \
                    str(data.close_price)+ "," + \
                    str(data.settle_price)+ "," + \
                    str(data.high_limited)+ "," + \
                    str(data.low_limited)+ "," + \
                    str(data.pre_delta)+ "," + \
                    str(data.curr_delta)+ "," + \
                    str(bid_price)+ "," + str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                    str(data.average_price)+ "," + \
                    str(data.trading_day)+ "," + \
                    str(data.variety_category)+ "," + \
                    str(data.latest_volume_trade)+ "," + \
                    str(data.init_volume_trade)+ "," + \
                    str(data.change_volume_trade)+ "," + \
                    str(data.bid_imply_volume)+ "," + \
                    str(data.offer_imply_volume)+ "," + \
                    str(data.total_bid_volume_trade)+ "," + \
                    str(data.total_ask_volume_trade)+ "," + \
                    str(data.exchange_inst_id)+ "\n"
            self.query_future_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDFutureSnapshotToCsv exception:' + str(error))

    def QueryMDFactorToCsv(self, data):
        try:
            if(self.query_factor_writer == None):
                self.query_factor_writer = DataWriter(self.dir,"Factor.csv")
                title = "data, size\n"
                self.query_factor_writer.WriteTitle(title)
            data_str = str(data.json_buf)[:data.data_size]+ "," + \
                        str(data.data_size)+ "\n"
            self.query_factor_writer.WriteData(data_str)
        except Exception as error:
            print('QueryMDFactorToCsv exception:' + str(error))
        

    def QueryMDKlineToCsv(self, data, kline_type):
        try:
            if(self.query_kline_writer_map[kline_type] == None):
                self.query_kline_writer_map[kline_type] = DataWriter(self.dir, self.query_kline_file_name_map[kline_type])
                title = "market_type, security_code, orig_time, " + \
                        "kline_time, open_price, high_price, low_price, " + \
                        "close_price, volume_trade, value_trade\n"
                self.query_kline_writer_map[kline_type].WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.kline_time)+ "," + str(data.open_price)+ "," + str(data.high_price)+ "," + \
                        str(data.low_price)+ "," + str(data.close_price)+ "," + \
                        str(data.volume_trade)+ "," + str(data.value_trade)+ "\n" 
            self.query_kline_writer_map[kline_type].WriteData(data_str)
        except Exception as error:
            print('QueryMDKlineToCsv exception:' + str(error))
        

    def ReplayMDTickExecutionToCsv(self, data):
        try:
            if(self.replay_tick_excution_writer == None):
                self.replay_tick_excution_writer = DataWriter(self.dir,"TickExecution.csv")
                title = "market_type, security_code, exec_time, channel_no, appl_seq_num, " + \
                        "exec_price, exec_volume, value_trade, offer_appl_seq_num, side, exec_type, " + \
                        "md_stream_id, biz_index, variety_category\n"
                self.replay_tick_excution_writer.WriteTitle(title)
            
            data_str = str(data.market_type)+ "," + \
                    str(data.security_code)+ "," + str(data.exec_time)+ "," + str(data.channel_no)+ "," + \
                    str(data.appl_seq_num)+ "," + str(data.exec_price)+ "," + str(data.exec_volume)+ "," + \
                    str(data.value_trade)+ "," + str(data.bid_appl_seq_num)+ "," + str(data.offer_appl_seq_num)+ "," + \
                    str(data.side)+ "," + str(data.exec_type)+ "," + str(data.md_stream_id)+ "," + \
                    str(data.biz_index)+ "," + str(data.variety_category) + "\n"
            self.replay_tick_excution_writer.WriteData(data_str)
        except Exception as error:
            print('ReplayMDTickExecutionToCsv exception:' + str(error))

    def ReplayMDStockSnapshotToCsv(self, data):
        try:
            if(self.replay_snapshot_writer == None):
                self.replay_snapshot_writer = DataWriter(self.dir,"StockSnapshot.csv")
                title = "market_type, security_code, orig_time, trading_phase_code, " + \
                        "pre_close_price, open_price, high_price, low_price, last_price, close_price, " + \
                        "bid_price, bid_volume, offer_price, offer_volume, num_trades, total_volume_trade, " + \
                        "total_value_trade, total_bid_volume, total_offer_volume, weighted_avg_bid_price, " + \
                        "weighted_avg_offer_price, IOPV, yield_to_maturity, high_limited, low_limited, " + \
                        "price_earning_ratio1, price_earning_ratio2, change1, change2\n"
                self.replay_snapshot_writer.WriteTitle(title)

            bid_price = get_tgw_list_to_str(data.bid_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            bid_volume = get_tgw_list_to_str(data.bid_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_price = get_tgw_list_to_str(data.offer_price, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            offer_volume = get_tgw_list_to_str(data.offer_volume, tgw.ConstField.kPositionLevelLen, get_tgw_intdata_by_index)
            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                    str(data.trading_phase_code)+ "," + str(data.pre_close_price)+ "," + str(data.open_price)+ "," + str(data.high_price)+ "," + \
                    str(data.low_price)+ "," + str(data.last_price)+ "," + str(data.close_price)+ "," + \
                    str(bid_price)+ "," + str(bid_volume)+ "," + str(offer_price)+ "," + str(offer_volume)+ "," + \
                    str(data.num_trades)+ "," + str(data.total_volume_trade)+ "," + str(data.total_value_trade)+ "," + \
                    str(data.total_bid_volume)+ "," + str(data.total_offer_volume)+ "," + str(data.weighted_avg_bid_price)+ "," + \
                    str(data.weighted_avg_offer_price)+ "," + str(data.IOPV)+ "," + str(data.yield_to_maturity)+ "," + \
                    str(data.high_limited)+ "," + str(data.low_limited)+ "," + str(data.price_earning_ratio1)+ "," + \
                    str(data.price_earning_ratio2)+ "," + str(data.change1)+ "," + str(data.change2)+ "\n"
            self.replay_snapshot_writer.WriteData(data_str)
        except Exception as error:
            print('ReplayMDStockSnapshotToCsv exception:' + str(error))

    def ReplayMDKlineToCsv(self, data, kline_type):
        try:
            if(self.replay_kline_writer_map[kline_type] == None):
                self.replay_kline_writer_map[kline_type] = DataWriter(self.dir, self.replay_kline_file_name_map[kline_type])
                title = "market_type, security_code, orig_time, " + \
                        "kline_time, open_price, high_price, low_price, " + \
                        "close_price, volume_trade, value_trade\n"
                self.replay_kline_writer_map[kline_type].WriteTitle(title)

            data_str = str(data.market_type)+ "," + str(data.security_code)+ "," + str(data.orig_time)+ "," + \
                        str(data.kline_time)+ "," + str(data.open_price)+ "," + str(data.high_price)+ "," + \
                        str(data.low_price)+ "," + str(data.close_price)+ "," + \
                        str(data.volume_trade)+ "," + str(data.value_trade)+ "\n" 
            self.replay_kline_writer_map[kline_type].WriteData(data_str)
        except Exception as error:
            print('ReplayMDKlineToCsv exception:' + str(error))
        

    
    