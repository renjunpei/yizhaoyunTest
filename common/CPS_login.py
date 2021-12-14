import requests
from common.config import Conf
import json
from common.mylogin import mylogin
from common.mylogin import Merge
import time

def login():
    a= mylogin()
    # t = time.time()
    # print(t)
    # nowTime = round(t * 1000)
    # print(nowTime)
    data = {
        'reqttime':1631254155247,
        'sign': '3981d120c230bd2f36cb08daed40c738',
        'apiversion': '20',
        'userid':a,
        'islogin': 1,
        'merchantid': 2,
        'device_value': 'd41d8cd98f00b204e9800998ecf8427e',
    }
    data = Merge(data)
    response = requests.get(url=Conf.API_ADDRESS+"/CPS/cps/user/dmjLogin",params=data)
    result = json.loads(response.content)
    # print(result["data"]["token"])
    return result["data"]["token"]


if __name__ == '__main__':
    login()