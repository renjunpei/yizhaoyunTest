# -*- coding:utf-8-*-
import unittest
from common.canshu import Merge,create_phone
import requests
from common.config import Conf
import json

# 注册接口
class ZhuCe(unittest.TestCase):
    u"""用户注册接口"""
    def setUp(self):
        self.phone = create_phone()  # 调用注册手机号

    def test_a_loginbysmscode(self):
        u"""手机号注册"""
        # userphone = create_phone()   # 调用注册手机号
        # print(userphone)
        print(self.phone)
        data = {
            'reqttime':1631241504625,
            'userphone':self.phone,
            'sign':'4275c24121e0cd5a1c0a33c7e2f11956',
            'apiversion':20,
            'islogin':0,
            'merchantid':2,
            'device_value':'d41d8cd98f00b204e9800998ecf8427e',
            'smscode':666666,
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+'/TAOBAO/apps/loginbysmscode',data=data)
        result = json.loads(response.content)
        # print(result)
        return result

    def test_b_findbyextensionid(self):
        u"""查询上级邀请码"""
        data = {
            'reqttime':1631242611030,
            'sign':'c2f14cd637fb45920c458d9318033538',
            'apiversion':20,
            'islogin':0,
            'merchantid':2,
            'device_value':'d41d8cd98f00b204e9800998ecf8427e',
            'extensionid':'ukynm2',
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+'/TAOBAO/apps/findbyextensionid',data=data)
        result = json.loads(response.content)
        # print(result)
        return result

    def test_c_usersetpwd(self):
        u"""注册绑定"""
        # userphone = create_phone()   #调用随机生成手机号
        data = {
            'wxmc':self.phone,
            'reqttime':1631244840586,
            'userphone':self.phone,
            'sign':'528fba64d7dd0073e8f889470ec7d8e6',
            'userpwd':'e10adc3949ba59abbe56e057f20f883e',
            'apiversion':20,
            'userid':380,
            'islogin':0,
            'merchantid':2,
            'device_value':'d41d8cd98f00b204e9800998ecf8427e',
            'extensionid':'ukynm2',
        }
        data = Merge(data)
        response = requests.post(url=Conf.API_ADDRESS+"/TAOBAO/apps/usersetpwd",data=data)
        result = json.loads(response.content)
        print(result)
        return result



if __name__ == '__main__':
    unittest.main()