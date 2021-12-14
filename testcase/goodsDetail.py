import unittest
import requests
import json
from common.config import Conf
from common.CPS_login import login
from common.canshu import Merge

class GoodsDetail(unittest.TestCase):
    u"""商品详情相关接口"""
    def setUp(self):
        self.CPSTOKEN = {
            "CPSTOKEN":login()
        }
    # 商品详情页
    def test_a_goodsDetail(self):
        u"""商品详情页"""
        data={
            'clientType':3,
            'goodsId':Conf.goodsId,
            'imei':'0B3B30A7-41B8-43D6-8979-A49F56020843',
            'mobileModel':'PCAM10',
            'ifNewUserGoodsAdd':'false',
            'systemVersion':10,
        }
        data = Merge(data)
        # print(self.CPSTOKEN)
        response = requests.post(url=Conf.API_ADDRESS+'/yxrweb/goods/queryGodosDetail',params=data,headers=self.CPSTOKEN)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            goodsId = result["result"]["goodsDetail"]["goodsId"]
            skuId = result["result"]["goodsSkus"][0]["skuId"]
            # list = []
            #
            # list.append(skuId)
            # list.append(goodsId)
            # # return skuIds[0]
            # return list
            dict = {"skuId":skuId,"goodsId":goodsId}
            # print(str(dict))
            return dict

    def test_b_carCount(self):
        u"""商品详情页购物车数量"""
        data = {
                'mobileModel': "PCAM10"
        }
        data = Merge(data)
        # print(self.CPSTOKEN)
        response = requests.post(url=Conf.API_ADDRESS + '/yxrweb/car/carCount', params=data,headers=self.CPSTOKEN)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            # print(result)

            return result

    def test_c_addshopcar(self):
        u"""加入购物车列表"""
        a = self.test_a_goodsDetail()
        skuId = a['skuId']
        tradeSkuVO = [{"num": 1, "skuId": "{}".format(skuId)}]
        data = {
                'clientType': 3,
                 'tradeSkuVO': '{}'.format(tradeSkuVO),
                 # 'skuId':'{}'.format(skuId),
                 # 'num':1
                 'systemVersion':10,
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS + "/yxrweb/car/addShopCar", data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        return result

    # 商品优惠券（需要查看该商品有没有优惠券）
    def test_d_goodscoupon(self):
        u"""商品详情优惠券列表接口"""
        a = self.test_a_goodsDetail()
        id = a['goodsId']
        data = {
            'clientType': 3,
            'goodsId': id,
            "systemVersion":10,
        }
        data=Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+'/yxrweb/coupon/findByGoodsId',data=data,headers=self.CPSTOKEN)
        code = response.status_code
        if code == 200:
            result = json.loads(response.content)
            # id = result["result"][0]["id"]
            # print(id)
            return result["result"][0]["id"]

    # 领取优惠券
    def test_e_receivecoupon(self):
        u"""领取优惠券"""
        id1 = self.test_d_goodscoupon()
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'couponId': id1,
            "systemVersion": 10,
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+"/yxrweb/coupon/addUserCoupon",data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        return result

    def test_f_shiyongcoupon(self):
        u"""使用优惠券"""
        id1 = self.test_d_goodscoupon()
        data = {
            'clientType': 2,
            'imei': 'D439B4B3-DB5D-4505-B38E-4AB6351B158E',
            'couponId': id1,
            "systemVersion": 10,
            "sort":'zh',
            "pageNum":1,
        }
        data = Merge(data)
        # get请求用params  post请求用data
        response = requests.get(url=Conf.API_ADDRESS + "/yxrweb/goods/queryEsByParam", params=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        return result

    # 商品分享
    def test_g_fexniang(self):
        u"""商品分享"""
        data = {
            'clientType': 3,
            'imei': '0B3B30A7-41B8-43D6-8979-A49F56020843',
            'systemVersion': '12.1',
            'dataId': Conf.goodsId,
            'type':4,
            "systemVersion": 10,
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS + '/yxrweb/core/share/detail', data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        return result

    # def tearDown(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
