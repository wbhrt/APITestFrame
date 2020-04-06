import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

class SendEmail:
    global send_user
    global email_host
    global password
    send_user = "个人邮箱"
    email_host = "smtp.qq.com"
    password = "授权码"
    def send_email_file(self,user_list,sub,content):
        #构造邮件相关信息
        user = '个人邮箱' +"<" + send_user +">"
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        #添加xls附件到邮箱
        part = MIMEText(content,'plain','utf-8')
        message.attach(part)
        part = MIMEApplication(open(r"../report/report.html",'r',encoding='UTF-8').read())
        part.add_header('Content-Disposition', 'attachment', filename="report.html")
        message.attach(part)

        # jpg类型附件
        # part = MIMEApplication(open('foo.jpg', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.jpg")
        # message.attach(part)

        # pdf类型附件
        # part = MIMEApplication(open('foo.pdf', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        # message.attach(part)

        # mp3类型附件
        # part = MIMEApplication(open('foo.mp3', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
        # message.attach(part)
        #链接服务器，发送邮件
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(send_user,user_list,message.as_string())
        server.close()


if __name__ == '__main__':
    send_user = "1426858895@qq.com"
    email_host = "smtp.qq.com"
    password = "krqkkbcqkliehbce"
    user_list = ["个人邮箱"]  # HAOREAEIKJELFQHT
    sub = "接口自动化"
    content = "测试邮件发送"
    s = SendEmail()
    s.send_email_file(user_list,sub,content)


