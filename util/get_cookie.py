from api.method_url import RunMethod
import requests
def retunr_cookie():
    r = RunMethod()
    url = 'http://127.0.0.1/api/mgr/signin'
    data = {
        "username": "byhy",
        "password": 88888888
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = r.run_main('POST', url=url, data=data, header=header)
    cookie = res.cookies
    cookie = requests.utils.dict_from_cookiejar(cookie)
    return ("sessionid="+cookie["sessionid"])
if __name__ == '__main__':
    s = retunr_cookie()
    print(s)