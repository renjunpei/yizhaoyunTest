#-*- coding:utf-8 -*-
#Auther:wenyy
#Date:2019-03-26

class DevelopmentConfig(object):
    API_ADDRESS='http://cps.17gouba.com' #测试环境
    goodsId=268432050000207  # 商品id
    userphone=13537430000 # 手机号
    addrId=273059180000091  # 用户收货地址
    idCardId=268525990003056  # 用户实名认证id=273059180000091


    # API_ADDRESS = 'http://192.168.11.230:8000'#测试环境内网
    # API_ADDRESS = 'http://cps.17gouba.com'#测试环境内网   NN地址



class ProductionConfig(object):
    API_ADDRESS = 'https://m.sudian178.com'#H5地址
    # API_ADDRESS = 'https://prerelease.sudian178.com'#预发环境


Conf = DevelopmentConfig