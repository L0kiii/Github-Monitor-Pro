"""
@usage: 任务名为markdown对应的标题/ip和Token需修改为自己的，多线程慎跑
@author: L0ki
@blog: https://l0ki.top
"""
import requests
import json
import random
import time
import threading
from random import choice

burp_url = 'http://ip:8001/api/monitor/task.json'
burp_header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
    'Accept': "application/json",
    'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    'Authorization': "Token 1bfab848ec0ebd306a55136e0e07fe6374df2ff9",
    'Content-Type': "application/json; charset=utf-8",
    'Origin': "http://ip:8001"
}

namesDict = {}
with open(file="urls.txt", mode="r", encoding="utf-8") as f:
    urls = f.readlines()
    n = 0
    for line in urls:
        n = n + 1
        line = line.strip()
        if line.startswith("###"):
            value = line[4:]
        else:
            namesDict[line] = value + str(n)
"""
随机数命名：
with open(file="urls.txt", mode="r", encoding="utf-8") as f:
    urls = f.readlines()
    n = 0
    for line in urls:
        n = n + 1
        line = line.strip()
        if line.startswith("###"):
            value = line[4:] + str(random.randint(0, 200))
        else:
            namesDict[line] = value + str(random.randint(0, 9))
"""

def getName(domain):
    if domain.startswith("###"):
        return None
    return namesDict[domain]


def send_data(threadNum):
    with open(file="urls.txt", mode="r", encoding="utf-8") as f:
        domains = f.readlines()
        for do in domains:
            domain = do.strip("\n")
            if getName(domain) is None:
                continue
            with open(file="keys.txt", mode="r", encoding="utf-8") as p:
                keys = p.readlines()
                keywords = []
                for k in keys:
                    key = domain + ' ' + k
                    keywords.append(key)
                n = ""
                for i in keywords:
                    n = n + i.strip() + "\n"
                data = {"name": getName(domain), "keywords": n, "match_method": 0, "ignore_org": "", "ignore_repo": "",
                        "mail": "",
                        "pages": 5, "interval": 60}
                burp_data = json.dumps(data)
                try:
                    response = requests.post(url=burp_url, headers=burp_header, data=burp_data)
                    # 打印请求状态
                    if response:
                        print(u"线程" + str(threadNum) + u"状态码：" + str(response) + "\n" + "[+]Add Task Success!")
                    response.close()
                except EOFError:
                    print("[*]Connection is failed! time out!")


def run(threadNum, internTime, duration):
    # 创建数组存放线程
    threads = []
    try:
        # 创建线程
        for i in range(1, threadNum):
            # 针对函数创建线程
            t = threading.Thread(target=send_data, args=(i,))
            # 把创建的线程加入线程组
            threads.append(t)
    except Exception as e:
        print(e)
    try:
        # 启动线程
        for thread in threads:
            thread.setDaemon(True)
            thread.start()
            time.sleep(internTime)
        # 等待所有线程结束
        for thread in threads:
            thread.join(duration)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    startime = time.strftime("%Y%m%d%H%M%S")
    now = time.strftime("%Y%m%d%H%M%S")
    duratiion = input(u"输入持续运行时间:")
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
    while (startime + str(duratiion)) != now:
        run(10, 1, int(duratiion))
        now = time.strftime("%Y%m%d%H%M%S")
