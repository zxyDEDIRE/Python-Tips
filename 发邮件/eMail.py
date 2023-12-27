import json

import yagmail


def ReadMem(json_name):
    F = open(json_name, 'r', encoding="utf-8")
    content = F.read()
    F.close()
    return json.loads(content)


def eMail(email_to, email_title, email_content):
    # 发送方 邮件用户
    mail_user = {
        '1925479484@qq.com': "buns_out"
    }
    # 发送方 授权码
    mail_key = 'nhvywvghzvefjfec'
    # smtp服务器
    mail_host = 'smtp.qq.com'
    try:
        mail_server = yagmail.SMTP(
            user=mail_user, password=mail_key, host=mail_host)
        mail_server.send(to=email_to, subject=email_title, contents=email_content)
        mail_server.close()
        return True
    except Exception as e:
        print(e)
        return False


def main():
    Mem = ReadMem("package.json")
    eMail(Mem['to'], Mem['titile'], Mem['content'])


if __name__ == '__main__':
    main()