#-*-coding:utf-8-*-
#Auther:wenyy
#Date:2019-03-26

import unittest
import requests
import json
import random
import time
from common.config import Conf
from common.CPS_login import login
from testcase.goodsDetail import GoodsDetail
from common.canshu import Merge

class Order(unittest.TestCase):
    u"""下单支付相关接口"""
    def setUp(self):
        self.CPSTOKEN = {
            "CPSTOKEN": login()
        }
        self.a = GoodsDetail.test_a_goodsDetail(self)
        self.skuId = self.a['skuId']
   # 检查库存
    def test_a_checkStock(self):
        u"""检查库存"""
        createVo = [{"withinBuyId": 0,"giveSellcount": 0, "num": 1, "refundNum": 0, "skuId": "{}".format(self.skuId)}]
        data = {
                'clientType': 3,
                'createVo': '{}'.format(createVo),
                }
        data = Merge(data)
        # 格式化成 2019-03-15 19:31:00 格式
        # starttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        starttime = time.time()
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/trade/sure/checkStock", data=data,headers=self.CPSTOKEN)
        # endtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        result = json.loads(response.content)
        endtime = time.time()
        # responsetime = endtime - starttime
        # print(responsetime)
        # print(result)
        return result

    """确认订单时查询基础数据"""
    def test_b_getorder(self):
        u"""确认订单时查询基础数据"""
        createVo = [{"withinBuyId": 0, "giveSellcount": 0, "num": 1, "refundNum": 0, "skuId": "{}".format(self.skuId)}]
        data = {
                'clientType': 3,
                'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
                'createVo': '{}'.format(createVo)
                }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/trade/sure/queryBaseData", data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    """查询金额信息"""
    def test_c_getAmount(self):
        u"""金额查询(云仓发货)"""
        createVo = [{"withinBuyId": 0, "giveSellcount": 0, "num": 1, "refundNum": 0, "skuId": "{}".format(self.skuId)}]
        data = {
                'clientType': 3,
                'imei':'0B3B30A7-41B8-43D6-8979-A49F56020843',
                'createVo': '{}'.format(createVo),
                'addrId': Conf.addrId,
                'idCardId':Conf.idCardId,
                'intefaceType':1,
                'userAddrId':Conf.addrId,
                'takeType':1,
                }
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/trade/sure/getAmount", data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        print(result)
        return result

    """查询可用的优惠券数量"""
    def test_d_countCouponsForBuy(self):
        u"""查询可用的优惠券数量"""
        createVo = [{"withinBuyId": 0, "giveSellcount": 0, "num": 1, "refundNum": 0, "skuId": "{}".format(self.skuId)}]
        data = {
                'clientType': 3,
                'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
                'createVo': '{}'.format(createVo)
                }
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/coupon/queryTradeCanUserCoupons", data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    """查询金额信息"""
    def test_e_getAmount(self):
        u"""查询金额信息(立即仓发货)"""
        createVo = [{"withinBuyId": 0, "giveSellcount": 0, "num": 1, "refundNum": 0, "skuId": "{}".format(self.skuId)}]
        data = {
            'clientType': 3,
            'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
            'createVo': '{}'.format(createVo),
            'addrId': Conf.addrId,
            'idCardId': Conf.idCardId,
            'intefaceType': 1,
            'userAddrId': Conf.addrId,
            'takeType': 2,
        }
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/trade/sure/getAmount", data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        print(result)
        return result

    """创建订单(立即发货)"""
    def test_f_createTrade(self):
        u"""创建订单(立即发货)"""
        createVo = [{"giveSellcount":0,"num":1,"refundNum":0,"withinBuyId":0,"skuId":"{}".format(self.skuId)}]
        data = {
            'userGrade':5,
            'ifAnonymous':'false',
            'ifUsePackage':'false',
            'ifUseSystemCash':'true',
            'systemVersion':11,
            'userAddrId':Conf.addrId,
            'takeType':1,
            'clientType':3,
            'createVo':'{}'.format(createVo),
            'imei':'a613b41652784ebd',
            'mobileModel':'PCAM10'
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+"/yxrweb/trade/sure/createTrade",data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result["result"]["tradeNo"]

    """创建订单(云仓发货)"""
    def test_g_createTrade(self):
        u"""创建订单(云仓发货)"""
        createVo = [{"giveSellcount": 0, "num": 1, "refundNum": 0, "withinBuyId": 0, "skuId": "{}".format(self.skuId)}]
        data = {
            'userGrade': 5,
            'ifAnonymous': 'false',
            'ifUsePackage': 'false',
            'ifUseSystemCash': 'true',
            'systemVersion': 11,
            'userAddrId': Conf.addrId,
            'takeType': 2,
            'clientType': 3,
            'createVo': '{}'.format(createVo),
            'imei': 'a613b41652784ebd',
            'mobileModel': 'PCAM10'
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/trade/sure/createTrade", data=data,
                                 headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result["result"]["tradeNo"]

    """订单支付获取验证码"""
    def test_h_sendSmsForPay(self):
        u"""订单支付获取验证码"""
        data = {
            'clientType':3,
            'tradeNo':self.test_f_createTrade(),
            'mobileModel':"PCAM10",
            'imei':"a613b41652784ebd",
            'systemVersion':11,
            'timestamp':1631256308306,
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+'/yxrweb/trade/sure/sendSmsForPay',data=data,headers= self.CPSTOKEN)
        result = json.loads(response.content)
        return result

    """订单支付（立即发货）"""
    def test_i_paySystemCachAmount(self):
        u"""订单支付(立即发货)"""
        tradeNo = self.test_f_createTrade()
        data = {
                'clientType':3,
                'tradeNo':tradeNo,
                'captcha':666666,
                'mobileModel':'PCAM10',
                'imei':'a613b41652784ebd',
                'systemVersion':11
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+"/yxrweb/trade/sure/paySystemCachAmount",data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    """订单支付（云仓发货）"""
    def test_j_paySystemCachAmount(self):
        u"""订单支付(云仓发货)"""
        tradeNo = self.test_g_createTrade()
        data = {
            'clientType': 3,
            'tradeNo': tradeNo,
            'captcha': 666666,
            'mobileModel': 'PCAM10',
            'imei': 'a613b41652784ebd',
            'systemVersion': 11
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/trade/sure/paySystemCachAmount", data=data,
                                 headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result



    # """查询可用与不可用的优惠券"""
    # def test_getCouponsForBuy(self):
    #     tradeSkuVO = [{"num": 1, "skuId": "{}".format(self.skuId)}]
    #     data = {'systemVersion': '7.0',
    #             'clientType': 2,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'versionAndr': 104,
    #             'version': 104,
    #             'tradeSkuVO': '{}'.format(tradeSkuVO)
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/coupon/getCouponsForBuy", data=data,
    #                              cookies=self.cookie)
    #     result = json.loads(response.content)
    #     coupons = result['result']['canUse']
    #     list = [coupon['id'] for coupon in coupons]  # 推导式得出list
    #     usercouponId = random.sample(list, 1)
    #     return usercouponId
    #
    # """查询手机号列表"""
    # def test_queryMobileListByPage(self):
    #     data = {'systemVersion': '7.0',
    #             'clientType': 3,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'versionAndr': 107,
    #             'version': 107,
    #             'weexVersion':127,
    #             'pageNo': 1
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/trade/mobile/queryMobileListByPage", data=data,
    #                              cookies=self.cookie)
    #     result = json.loads(response.content)
    #     list = result['result']['list']
    #     if list is  None:
    #         print("没有手机号啦~~~")
    #     else:
    #         mobile_list = [mobiles['mobile'] for mobiles in list]
    #         mobile = random.choices(mobile_list)
    #     return mobile
    #
    #
    # """保存手机号"""
    #
    # def test_saveOrUpdateNetInfo(self):
    #     mobile = self.test_queryMobileListByPage()
    #     data = {'systemVersion': '7.0',
    #             'clientType': 3,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'versionAndr': 107,
    #             'version': 107,
    #             'weexVersion': 127,
    #             'idCard': 411321199204123210,
    #             'mobile':mobile,
    #             'name':'温阳阳',
    #             'backPhoto':'https://image.sudian178.com/sd/idcard/20190325150106182209.jpg',
    #             'frontPhoto':'https://image.sudian178.com/sd/idcard/20190325150059777974.jpg',
    #             'idCardPhoto':'https://image.sudian178.com/sd/idcard/20190325150114692970.jpg'
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/trade/mobile/net/saveOrUpdateNetInfo", data=data,
    #                              cookies=self.cookie)
    #     result = json.loads(response.content)
    #     return result['result']['id']
    #
    #
    #
    # """创建订单"""
    # def test_createOrder(self):
    #     Data = self.test_get()
    #     Amount = self.test_getAmount()
    #     ifLiantongCard =Data['result']['ifLiantongCard']
    #     ifNeedCardId = Data['result']['ifNeedCardId']
    #     isCanUseCash = Amount['result']['isCanUseCash']
    #     tradeSkuVO = [{"num": 1, "skuId": "{}".format(self.skuId)}]
    #     if ifLiantongCard=='false' and ifNeedCardId == 'false':
    #         data = {'systemVersion': '7.0',
    #                 'clientType': 3,
    #                 'imei': 860076030766777,
    #                 'mobileModel': 'HUAWEI NXT - AL10',
    #                 'ifUseSystemCash': '{}'.format(isCanUseCash),
    #                 'versionAndr': 104,
    #                 'version': 104,
    #                 'tradeSkuVO': '{}'.format(tradeSkuVO),
    #                 'ifAnonymous': 'false',
    #                 'userAddrId': 258413960000058
    #                 }
    #     elif ifLiantongCard == 'false' and ifNeedCardId =='true':
    #         data={'systemVersion':'7.0',
    #         'clientType':3,
    #         'imei':860076030766777,
    #         'mobileModel':'HUAWEI NXT - AL10',
    #         'ifUseSystemCash':'{}'.format(isCanUseCash),
    #         'versionAndr':107,
    #         'version':107,
    #         'tradeSkuVO':'{}'.format(tradeSkuVO),
    #         'ifAnonymous':'false',
    #         'userAddrId':258413960000058,
    #         'userIdCardId':257935100000055
    #         }
    #     elif ifLiantongCard == 'true' and ifNeedCardId =='false':
    #         mobileNetId = self.test_saveOrUpdateNetInfo()
    #         data = {'systemVersion': '7.0',
    #                 'clientType': 3,
    #                 'imei': 860076030766777,
    #                 'mobileModel': 'HUAWEI NXT - AL10',
    #                 'ifUseSystemCash': '{}'.format(isCanUseCash),
    #                 'versionAndr': 107,
    #                 'version': 107,
    #                 'tradeSkuVO': '{}'.format(tradeSkuVO),
    #                 'ifAnonymous': 'false',
    #                 'userAddrId': 258413960000058,
    #                 'mobileNetId': mobileNetId
    #                 }
    #     else:
    #         mobileNetId = self.test_saveOrUpdateNetInfo()
    #         data = {'systemVersion': '7.0',
    #                 'clientType': 3,
    #                 'imei': 860076030766777,
    #                 'mobileModel': 'HUAWEI NXT - AL10',
    #                 'ifUseSystemCash': '{}'.format(isCanUseCash),
    #                 'versionAndr': 107,
    #                 'version': 107,
    #                 'tradeSkuVO': '{}'.format(tradeSkuVO),
    #                 'ifAnonymous': 'false',
    #                 'userAddrId': 258413960000058,
    #                 'userIdCardId':257935100000055,
    #                 'mobileNetId': mobileNetId
    #                 }
    #     response = requests.post(url=Conf.API_ADDRESS+"/sdapp/trade/confirm/createOrder",data=data,cookies=self.cookie)
    #     code = response.status_code
    #     if code == 200:
    #         result = json.loads(response.content)
    #         # print(result)
    #         tradeNo = result['result']['tradeNo']
    #     return tradeNo
    #
    # """购买礼包确认订单查询接口"""
    # def test_getForGift(self):
    #     data = {'systemVersion': '7.0',
    #             'clientType': 3,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'ifUseSystemCash': 'false',
    #             'versionAndr': 107,
    #             'version': 107,
    #             'goodsId': self.goodsId,
    #             'skuId':self.skuId
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/trade/confirm/getForGift", data=data, cookies=self.cookie)
    #     result = json.loads(response.content)
    #     return result
    #
    # """创建礼包订单"""
    # def test_createOrderForGift(self):
    #     giftData = self.test_getForGift()
    #     ifLiantongCard = giftData['result']['ifLiantongCard']
    #     ifNeedCardId = giftData['result']['ifNeedCardId']
    #     isCanUseCash = giftData['result']['isCanUseCash']
    #     if ifLiantongCard=='false' and ifNeedCardId == 'false':
    #         data = {'systemVersion': '7.0',
    #                 'clientType': 3,
    #                 'imei': 860076030766777,
    #                 'mobileModel': 'HUAWEI NXT - AL10',
    #                 'ifUseSystemCash': '{}'.format(isCanUseCash),
    #                 'versionAndr': 107,
    #                 'version': 107,
    #                 'goodsId': self.goodsId,
    #                 'skuId': self.skuId,
    #                 'ifAnonymous': 'false',
    #                 'userAddrId': '${addrId}'
    #                 }
    #     elif ifLiantongCard == 'false' and ifNeedCardId =='true':
    #         data = {'systemVersion': '7.0',
    #                 'clientType': 3,
    #                 'imei': 860076030766777,
    #                 'mobileModel': 'HUAWEI NXT - AL10',
    #                 'ifUseSystemCash': '{}'.format(isCanUseCash),
    #                 'versionAndr': 107,
    #                 'version': 107,
    #                 'goodsId': self.goodsId,
    #                 'skuId': self.skuId,
    #                 'ifAnonymous': 'false',
    #                 'userAddrId': '${addrId}',
    #                 'userIdCardId': '${cardId}'
    #                 }
    #     elif ifLiantongCard == 'true' and ifNeedCardId =='false':
    #         mobileNetId = self.test_saveOrUpdateNetInfo()
    #         data = {'systemVersion': '7.0',
    #                 'clientType': 3,
    #                 'imei': 860076030766777,
    #                 'mobileModel': 'HUAWEI NXT - AL10',
    #                 'ifUseSystemCash': '{}'.format(isCanUseCash),
    #                 'versionAndr': 107,
    #                 'version': 107,
    #                 'goodsId': self.goodsId,
    #                 'skuId': self.skuId,
    #                 'mobileNetId':mobileNetId,
    #                 'ifAnonymous': 'false',
    #                 'userAddrId': '${addrId}'
    #                 }
    #     else:
    #         mobileNetId = self.test_saveOrUpdateNetInfo()
    #         data = {'systemVersion': '7.0',
    #                 'clientType': 3,
    #                 'imei': 860076030766777,
    #                 'mobileModel': 'HUAWEI NXT - AL10',
    #                 'ifUseSystemCash': '%s' % isCanUseCash,
    #                 'versionAndr': 107,
    #                 'version': 107,
    #                 'goodsId': self.goodsId,
    #                 'skuId': self.skuId,
    #                 'mobileNetId': '%s' % mobileNetId,
    #                 'ifAnonymous': 'false',
    #                 'userAddrId': '${addrId}',
    #                 'userIdCardId': '${cardId}'
    #                 }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/trade/confirm/createOrderForGift", data=data, cookies=self.cookie)
    #     result = json.loads(response.content)
    #     print(result)
    #
    # """去支付"""
    #
    # def test_queryToPay(self):
    #     result = GoodsDetail.test_goodsDetail()
    #     ifGift = result['result']['ifGift']
    #     if ifGift == "false":
    #         tradeNo = self.test_createOrder()
    #     else:
    #         tradeNo = self.test_createOrderForGift()
    #     data = {'systemVersion': '7.0',
    #             'clientType': 3,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'versionAndr': 107,
    #             'version': 107,
    #             'weexVersion': 173,
    #             'tradeNo': tradeNo,
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/trade/confirm/queryToPay", data=data,
    #                              cookies=self.cookie)
    #     code = response.status_code
    #     if code == 200:
    #         result = json.loads(response.content)
    #     print(result)

    """H5支付"""
    # def test_startH5WeixinPay(self):
    #     data = {'systemVersion': '7.0',
    #             'clientType': 2,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'ifUseSystemCash': 'false',
    #             'versionAndr': 104,
    #             'version': 104,
    #             'goodsId': 256814540000430,
    #             'ifAnonymous': 'false',
    #             'userAddrId': 257403870000068,
    #             'userIdCardId': 257664290000141
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/payment/startH5WeixinPay", data=data, cookies=self.cookie)
    #     result = json.loads(response.content)
    #     print(result)
    #
    # """余额支付时发送短信验证码"""
    # def test_sendSmsForPay(self):
    #     tradeNo = self.test_createOrder()
    #     data = {'systemVersion': '7.0',
    #             'clientType': 2,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'versionAndr': 104,
    #             'version': 104,
    #             'tradeNo': '{}'.format(tradeNo),
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/trade/confirm/sendSmsForPay", data=data,
    #                              cookies=self.cookie)
    #     result = json.loads(response.content)
    #     print(result)
    #
    # """短信验证码支付校验接口"""
    # def test_checkSmsForCachOrder(self):
    #     tradeNo = self.test_createOrder()
    #     data = {'systemVersion': '7.0',
    #             'clientType': 3,
    #             'imei': 860076030766777,
    #             'mobileModel': 'HUAWEI NXT - AL10',
    #             'versionAndr': 104,
    #             'version': 104,
    #             'tradeNo': '{}'.format(tradeNo),
    #             'captcha':'8888'
    #             }
    #     response = requests.post(url=Conf.API_ADDRESS + "/sdapp/trade/confirm/checkSmsForCachOrder", data=data,
    #                              cookies=self.cookie)
    #     result = json.loads(response.content)
    #     print(result)



# def test_insertLogistics(self):
#     data = {
#         "postId":"",
#         "num":1,
#         "statustxt":"",
#         "context":"",
#         "logisticsName":"",
#         "ftime":"1552978385"
#     }
#     response = requests.post(url=Conf.API_ADDRESS+"/api/logistics/insertLogistics",data=data,cookies= self.cookie)
#     result = json.loads(response.content)
#     print(result)
#
# def test_updateLogisticsNo(self):
#     data = {
#             "tradeNo":"",
#             "postId": "",
#             "logisticsName": "",
#             "type": 2
#         }
#     response = requests.post(url=Conf.API_ADDRESS + "/api/logistics/updateLogisticsNo", data=data,
#                                  cookies=self.cookie)
#     result = json.loads(response.content)
#     print(result)







    # def tearDown(self):
    #     pass
        # self.result = GoodsDetail.test_goodsDetail(self)
        # ifGift = self.result['result']['ifGift']
        # if ifGift == "false":
        #     self.test_checkStock()
        #     self.test_get()
        #     self.test_getAmount()
        #     self.test_countCouponsForBuy()
        #     self.test_getCouponsForBuy()
        #     self.test_queryMobileListByPage()
        #     self.test_saveOrUpdateNetInfo()
        #     self.test_createOrder()
        #     self.test_queryToPay()
        # else:
        #     self.test_checkStock()
        #     self.test_getForGift()
        #     self.test_queryMobileListByPage()
        #     self.test_saveOrUpdateNetInfo()
        #     self.test_createOrderForGift()
        #     self.test_queryToPay()

if __name__ == '__main__':
    unittest.main()
