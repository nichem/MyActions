import requests, os
from common import *

cookie = os.environ.get("ZXCS_COOKIE")
print(cookie)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://zxcstxt.com",
    "Cookie": cookie,
}
url = "https://zxcstxt.com/wp-admin/admin-ajax.php"
r = requests.post(url, {"action": "user_checkin"}, headers=headers)
print(r.json())
notify("签到信息", r.json()["msg"])
