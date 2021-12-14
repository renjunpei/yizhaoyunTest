#-*- coding:utf-8 -*-
import requests
from common.config import Conf
import json
from common.canshu import Merge
import time


def mylogin():
    # t = time.time()
    # print(t)
    # nowTime = round(t * 1000)
    # print(nowTime)
    data = {
        'reqttime':1631254155150,
        'userphone':Conf.userphone,
        'sign':'d930722dcaa6451a6bc284ad09b9c017',
        'apiversion':20,
        'islogin':0,
        'device_value':'d41d8cd98f00b204e9800998ecf8427e',
        'smscode':666666,
    }
    data= Merge(data)
    # print(data)
    response = requests.post(url=Conf.API_ADDRESS+"/TAOBAO/apps/loginbysmscode",data=data)
    result = json.loads(response.content)
    # print(result)
    # userid = result["userid"]
    # print(userid)
    return result["userid"]

if __name__ == '__main__':
    mylogin()

