# -*- coding: UTF-8 -*-
__version__ ="0.1.0"
import time
import warnings
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

start = time.time()
warnings.filterwarnings('ignore')

freq = 59  # 30分钟发一次邮件汇报
limit = 1050007880  # 最大300条数据，停止，发送邮件汇报
mailflag = True
latest_price = 0
yyeaRr = 2024
receive_list = ['782568799@qq.com']  # ,'2397462028@qq.com']

def sendmail(receive_mail, title=None, sendtime=None):
    send_usr = '782568799@qq.com'  # 发件人
    send_pwd = 'svkjzmjipaczbehc'  # 'pdnfrwfijoewbeff'#'BUQRRQFPUANBCWMY' # 授权码，邮箱设置
    receive = receive_mail  # '782568799@qq.com'  # 接收者
    content = '发送于{}<p><a href="{}">GBPCNY-中国银行现价动态</a></p>'.format(time.ctime(), url)
    # content 内容设置
    html_img = f'<p>{content}<br><img src="cid:image1"></br></p>'  # html格式添加图片
    email_server = 'smtp.qq.com'

    msg = MIMEMultipart()  # 构建主体
    msg['Subject'] = Header(title, 'utf8')  # 邮件主题
    msg['From'] = "ForeX_Git"  # send_usr  # 发件人
    msg['To'] = Header('midy', 'utf8')  # 收件人--这里是昵称

    # msg.attach(MIMEText(content,'html','utf-8'))  # 构建邮件正文,不能多次构造
    attchment = MIMEApplication(open(r'data_boc\{}.png'.format("SEND"), 'rb').read())  # 文件
    attchment.add_header('Content-Disposition', 'attachment', filename=r'data_boc\{}.png'.format("SEND"))
    msg.attach(attchment)  # 添加附件到邮件
    attchment2 = MIMEApplication(open(r'{}.csv'.format('SEND'), 'rb').read())  # 文件
    attchment2.add_header('Content-Disposition', 'attachment', filename=r'{}.csv'.format('SEND'))
    msg.attach(attchment2)  # 添加附件到邮件

    f = open(r'data_boc\{}.png'.format("SEND"), 'rb')  # 打开图片
    msgimage = MIMEImage(f.read())
    f.close()
    msgimage.add_header('Content-ID', '<image1>')  # 设置图片
    msg.attach(msgimage)
    msg.attach(MIMEText(html_img, 'html', 'utf-8'))  # 添加到邮件正文
    try:
        smtp = SMTP_SSL(email_server)  # 指定邮箱服务器
        smtp.ehlo(email_server)  # 部分邮箱需要
        smtp.login(send_usr, send_pwd)  # 登录邮箱
        smtp.sendmail(send_usr, receive, msg.as_string())  # 分别是发件人、收件人、格式
        smtp.quit()  # 结束服务
        print(receive_mail, '邮件发送成功,mailflag已经改成False!', time.ctime())
        global mailflag
        mailflag = False
    except Exception as E:
        print('发送失败', E)
        return 'sent'
