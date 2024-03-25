# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import datetime
import time

import requests

t = time.time()
local_time = time.localtime(t)
date_head = time.strftime("%Y%m%d%H%M%S",local_time)
date_m_secs = str(datetime.datetime.now().timestamp()).split(".")[-1]
timestamp = "%s%.3s" % (date_head,date_m_secs)
def post():

    url = "https://admin.yqtbuy.com/order/orderList?shop_sn=ab83533b"
    headers = {
                  "Accept-Encoding":"gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
        "Content-Length": "1788",
        "Content-Type": "application/json;chrest=utf-8",
        "Authorization":"Bearer bU190jvWC8siYddKLSuUMTIxMjM0ODQ=",
        "Client-Id":"NO_AUTH",
        #"Upload-Time": timestamp,
        "authorization": "XI2EE8Ntu4J3vOGjz369QAMJJj8dNLk8dvRMd7hjvWY=",
        "sec-ch-ua": '"Not?A_Brand";v="8","Chromium";v="108","Microsoft Edge";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin",
        "Host":"supp.yqtyun.com",
        "Cookie":"sidebarStatus=1"

    }
    body = {"order_sn":"","user_mobile":"","distributor_name":"","order_status":"","has_refund":0,"tags":"","supplier_id":"","tag_type":"","begin_time":"","end_time":"","i1_category_id":"","i2_category_id":"","i3_category_id":"","page_size":20,"confirm_begin_time":"","confirm_end_time":"","shop_card_activity_id":"","page":1}

    res = requests.post(url=url, headers=headers,json=body)
    return res.content




if __name__ == '__main__':
    res = post()
    print(res)



