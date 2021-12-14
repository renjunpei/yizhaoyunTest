#-*- coding:utf-8 -*-
import unittest
from common.canshu import Merge,random_name
from common.CPS_login import login
from common.mylogin import mylogin
import requests
from common.config import Conf
import json


class Me(unittest.TestCase):
    u"""我的页面数据接口"""
    def setUp(self):
        self.CPSTOKEN = {
            "CPSTOKEN":login()
        }
        self.name = random_name()    # 调用随机生成名字的方法
    # 获取个人信息数据接口
    def test_a_getuserinfo(self):
        u"""获取个人信息数据"""
        data = {
            'reqttime':'1631514045916',
            'sign':'cc0d99ee767f4c2fd91a002d1ed51cce',
            'apiversion':20,
            'userid':mylogin(),
            'islogin':1,
            'merchantid':2,
            'device_value':'d41d8cd98f00b204e9800998ecf8427e',
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+'/TAOBAO/apps/getuserinfo',data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    # 获取我的页面分享数据接口
    def test_b_getadvertisement(self):
        u"""获取我的页面分享数据接口"""
        data = {
            'reqttime': '1631514782307',
            'sign': 'a5e13b132ec9e5f202fce642f4760971',
            'apiversion': 20,
            'userid': mylogin(),
            'islogin': 1,
            'advertisementposition': 42,
            'device_value': 'd41d8cd98f00b204e9800998ecf8427e',
            'merchantid':2
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+"/TAOBAO/apps/getadvertisement",data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    # 获取我的页面icon数据
    def test_c_getappico(self):
        u"""获取我的页面icon数据"""
        data = {
            'reqttime': '1631514782313',
            'sign': '21286ee76a93bf0e8f02a1ed986c9705',
            'apiversion': 20,
            'userid': mylogin(),
            'islogin': 1,
            'merchantid': 2,
            'device_value': 'd41d8cd98f00b204e9800998ecf8427e',
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+'/TAOBAO/apps/getappico',data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    # 获取我的页面订单状态的数量
    def test_d_findTradeCount(self):
        data = {
            'clientType': 3,
            'mobileModel': 'PCAM10',
            'imei':'a613b41652784ebd',
            'systemVersion': 11,
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+'/yxrweb/trade/findTradeCount',data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    # 获取我的页面底部商品数据
    def test_e_queryHotIndexGoods(self):
        u"""获取我的页面底部商品数据"""
        data = {
            'clientType': 3,
            'mobileModel': 'PCAM10',
            'imei': 'a613b41652784ebd',
            'systemVersion': 11,
            'pageNum':1
        }
        data = Merge(data)
        response = requests.get(url=Conf.API_ADDRESS+"/yxrweb/core/queryHotIndexGoods",params=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        # print(result)
        return result

    # 修改昵称
    def test_f_userinfoedit(self):
        u"""修改昵称"""
        data = {
            'reqttime': '1631518974462',
            'sign': 'cfa1384f0cc694a451207e31c2fcf2f5',
            'apiversion': 20,
            'userid': mylogin(),
            'islogin': 1,
            'merchantid': 2,
            'device_value': 'd41d8cd98f00b204e9800998ecf8427e',
            'username':self.name
        }
        response = requests.post(url=Conf.API_ADDRESS+"/TAOBAO/apps/userinfoedit",data=data,headers=self.CPSTOKEN)
        result = json.loads(response.content)
        print(self.name)
        print(result)


    # 上传头像
    def test_g_Upload(self):
        u"""上传头像"""
        pass








if __name__ == '__main__':
    unittest.main()









