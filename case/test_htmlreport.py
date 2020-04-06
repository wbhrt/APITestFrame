import unittest
from HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def setUp(self):
        print("test start")


    def test_bbb(self):
        print("test bbb")

    def test_aaa(self):
        print("test aaa")

    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test("test_bbb"))
    suite.addTest(Test('test_aaa'))
    filename = r'F:\接口测试\report\report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(suite)
    fp.close()  # 关闭报告文件


