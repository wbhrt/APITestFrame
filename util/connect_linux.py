import paramiko

class Linux(object):
    def __init__(self,ip,username,password,timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        self.try_times = 3
        self.transport = ''
        try:
            self.transport = paramiko.SSHClient()
            self.transport.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.transport.connect(self.ip, 22, self.username, self.password)
            print('链接%s成功' % self.ip)
        except Exception:
            if self.try_times != 0:
                print(u'连接%s失败，进行重试' % self.ip)
                self.try_times -= 1
            else:
                print(u'重试3次失败，结束程序')
                exit(1)
    # 断开连接
    def close(self):
        self.transport.close()
    # 发送要执行的命令
    def send(self, cmd):
        stdin, stdout, stderr = self.transport.exec_command(cmd)
        print(stdout.read())

# 测试linux类代码
if __name__ == '__main__':
    ip = "192.168.142.130"
    port = 22
    user = "y"
    password = "root1227"
    host = Linux(ip, user, password)
    host.send('pwd')
    host.close()