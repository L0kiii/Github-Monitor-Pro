"""
@usage: 任务名为markdown对应的标题/ip和Token需修改为自己的
@author: L0ki
@blog: https://l0ki.top
"""
import requests
import json

burp_url = 'http://ip:8001/api/monitor/task.json'
burp_header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    'Accept': "application/json",
    'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'Authorization': "Token 1bfab848ec0ebd306a55136e0e07fe6374df2ff9",
    'Content-Type': "application/json; charset=utf-8",
    'Origin': "http://ip:8001"
}


def send_data():
    with open(file="urls.txt", mode="r", encoding="utf-8") as f:
        domains = f.readlines()
        for do in domains:
            domain = do.strip("\n")
            with open(file="keys.txt", mode="r", encoding="utf-8") as p:
                keys = p.readlines()
                keywords = []
                for k in keys:
                    key = domain + ' ' + k
                    keywords.append(key)
                n = ""
                for i in keywords:
                    n = n + i.strip() + "\n"
                data = {"name": domain, "keywords": n, "match_method": 0, "ignore_org": "", "ignore_repo": "",
                        "mail": "",
                        "pages": 5, "interval": 60}
                burp_data = json.dumps(data)
                try:
                    response = requests.post(url=burp_url, headers=burp_header, data=burp_data)
                    # 打印请求状态
                    if response:
                        print("[+]Add Task Success!")
                    response.close()
                except EOFError:
                    print("[*]time out!")


if __name__ == '__main__':
    print(
        """    
████████╗ █████╗ ███████╗██╗  ██╗███████╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝
   ██║   ███████║███████╗█████╔╝ ███████╗
   ██║   ██╔══██║╚════██║██╔═██╗ ╚════██║
   ██║   ██║  ██║███████║██║  ██╗███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
@author: L0ki
@blog: https://l0ki.top                                                                          
        """
    )
    send_data()
