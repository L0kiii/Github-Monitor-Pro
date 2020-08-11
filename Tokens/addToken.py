"""
@usage: 在tokens.txt中添加需要的token
@author: L0ki
@blog: https://l0ki.top
"""
import requests
import json

# 此处填写项目部署的地址
burp_url = 'http://ip:8001/api/monitor/token.json'
burp_header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    'Accept': "application/json",
    'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'Authorization': "Token 1bfab848ec0ebd306a55136e0e07fe6374df2ff9",
    'Content-Type': "application/json; charset=utf-8",
    'Origin': "http://ip:8001"
}


def sent_data():
    with open(file="tokens.txt", mode="r", encoding="utf-8") as f:
        tokens = f.readlines()
        for to in tokens:
            token = to.strip("\n")
            data = {"value": token}
            burp_data = json.dumps(data)
            response = requests.post(url=burp_url, headers=burp_header, data=burp_data)
            if response:
                print("[+]Add Token Success!")


if __name__ == '__main__':
    print(
        """

████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗███████╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║███████╗
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║╚════██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║███████║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝
@author: L0ki
@blog: https://l0ki.top   
        """
    )
    sent_data()