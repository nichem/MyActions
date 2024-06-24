import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

load_dotenv()
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_EMAIL = os.environ.get("SMTP_EMAIL")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")


def notify(title: str, content: str) -> None:
    """
    使用 SMTP 邮件 推送消息。
    """

    print("SMTP 邮件 服务启动")

    message = MIMEText(content, "plain", "utf-8")
    message["From"] = formataddr(
        (
            Header("我的推送", "utf-8").encode(),
            SMTP_EMAIL,
        )
    )
    message["To"] = formataddr(
        (
            Header("我的推送", "utf-8").encode(),
            SMTP_EMAIL,
        )
    )
    message["Subject"] = Header(title, "utf-8")

    try:
        smtp_server = smtplib.SMTP_SSL(SMTP_SERVER)
        smtp_server.login(SMTP_EMAIL, SMTP_PASSWORD)
        smtp_server.sendmail(
            SMTP_EMAIL,
            SMTP_EMAIL,
            message.as_bytes(),
        )
        smtp_server.close()
        print("SMTP 邮件 推送成功！")
    except Exception as e:
        print(f"SMTP 邮件 推送失败！{e}")


if __name__ == "__main__":
    notify("测试标题", "测试信息")
