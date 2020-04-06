#coding:utf-8
import requests,json

class RunMethod:
    def post_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res =requests.post(url,data,headers=header)
        else:
            res =requests.post(url, data)
        return res
    def get_main(self,url,data,header):
        res = None
        if header != None:
            res = requests.get(url, data, headers=header)
        else:
            res = requests.get(url, data)
        return res
    def put_main(self,url,data,header):
        res = None
        if header !=None:
            res = requests.put(url,json=data,headers=header)
        else:
            res = requests.get(url,json=data)
        return res
    def delete_main(self,url,data,header):
        res = None
        if header !=None:
            res = requests.delete(url)
        else:
            res = requests.get(url, data)
        return res
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'GET':
            res = self.get_main(url, data,header)
        elif method== 'POST':
            res = self.post_main(url, data,header)
        elif method=='PUT':
            res = self.delete_main(url,data,header)
        return  res #json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

if __name__ == '__main__':
    from util.get_cookie import *
    url3 = "http://127.0.0.1/api/mgr/customers"
    data3 = {
        "action": "modify_customer",
        "id": 43,
        "newdata": {
            "name": "武汉市桥北医院",
            "phonenumber": "13345678888",
            "address": "武汉市桥北医院北路"
        }
    }
    header3 = {
        "Content-Type": "application/json",
        "Cookie": "",
        "User - Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/80.0.3987.132Safari/537.36"
    }
    r = RunMethod()
    header3["Cookie"]=retunr_cookie()
    res1 = r.run_main('PUT', url=url3, data=data3, header=header3)
    print("新增用户用例：", (res1.json()))