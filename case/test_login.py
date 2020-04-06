import unittest
from HTMLTestRunner import HTMLTestRunner
from dataconfig.staticdata import *
from util.connect_email import SendEmail
from util.get_cookie import *


m = RunMethod()
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("用例开始")

    def test_get_customer(self):
        header1["Cookie"] = retunr_cookie()
        res = m.run_main('GET', url=url1, data=params1, header=header1)
        print("获取用户列表用例：",(res.text))
        print("获取状态码：",res.status_code)

    def test_add_customer(self):
        header2["Cookie"] = retunr_cookie()
        res = m.run_main('POST',url=url2,data=data2,header=header2)
        print("获取状态码：", res.status_code)
        print("新增用户用例：",(res.text).encode('utf8').decode('unicode_escape'))

    def test_modify_customer(self):
        header3["Cookie"] = retunr_cookie()
        res = m.run_main('PUT',url=url3,data=data3,header=header3)
        print("获取状态码：", res.status_code)
        print("新增用户用例：", (res.text).encode('utf8').decode('unicode_escape'))
    @classmethod
    def tearDownClass(cls):
        user_list = ["个人邮箱"]
        sub = "接口自动化"
        content = "测试邮件发送"
        s = SendEmail()
        s.send_email_file(user_list, sub, content)
        print("用例结束")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test("test_get_customer"))
    suite.addTest(Test("test_add_customer"))
    filename = r'F:\TestFrame\report\report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='接口测试报告', description='用例执行情况：')
    runner.run(suite)
    fp.close()  # 关闭报告文件




