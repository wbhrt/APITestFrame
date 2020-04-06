if __name__ == '__main__':
    import requests
    response = requests.get("http://127.0.0.1/mgr/index.html#/")
    cookie_value = ''
    for key, value in response.cookies.items():
        cookie_value += key + '=' + value + ';'
    print(cookie_value)
