import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email import encoders

class SendEmail:
    global send_user
    global email_host
    global password
    send_user = "个人邮箱"
    email_host = "smtp.qq.com"
    password = "授权码"
    def send_email(self,user_list,sub,content):
        user = '个人邮箱' +"<" + send_user +">"
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        part = MIMEText(content,'plain','utf-8')
        message.attach(part)
        part = MIMEApplication(open(r"../report/report.html",encoding='UTF-8').read())
        part.add_header('Content-Disposition', 'attachment', filename=r"../report/report.html")
        message.attach(part)

        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(send_user,user_list,message.as_string())
        server.close()

if __name__ == '__main__':
    user_list = ['个人邮箱']
    sub = "接口自动化"
    content = "运行个数:10"
    s = SendEmail()
    s.send_email(user_list,sub,content)

