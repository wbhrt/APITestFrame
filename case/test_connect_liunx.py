import paramiko

# 创建SSHClient实例对象
ssh = paramiko.SSHClient()

# 调用方法，标识没有远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程机器 地址端口用户名密码
ssh.connect("192.168.142.130",22,"y","root1227")
stdin,stdout,stderr = ssh.exec_command("ls")
print(stdout.read())
ssh.close()
