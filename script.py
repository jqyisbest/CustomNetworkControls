import requests
import time
import re
import os

# 请求插件并保存结果
def request_and_save_plugins():
    for root, ds, fs in os.walk('./Loon/'):
        for f in fs:
            # yield f
            f=str(f)
            plugin_link="https://raw.githubusercontent.com/jqyisbest/LoonKissSurge/refs/heads/main/Loon/"+str(f)
            # 构造请求URL
            url = f"http://localhost:9101/file/_start_/{plugin_link}/_end_/Weibo_remove_ads.sgmodule.txt?type=loon-plugin&target=surge-module&sni=%20%2C%20&del=true&pm=REJECT&category=iKeLee"
            transfer_success = False
            retry_times=0
            while (not transfer_success) and retry_times <5:
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        # 保存返回的结果为 f[0:len(f)-7].sgmodule
                        file_name = f"{f[0:len(f)-7]}.sgmodule"
                        with open(file_name, 'w', encoding='utf-8') as file:
                            file.write(response.text)
                        print(f"Surge插件 {f} 已保存为 {file_name}")
                        transfer_success = True
                    else:
                        print(f"Surge插件 {f} 请求失败，状态码: {surge_response.status_code}，即将重试")
                        retry_times +=1
                except Exception as e:
                    retry_times +=1
                    print(f"url {url} 请求异常，即将重试")
                    print(e)
            

# 主函数
def main():
    request_and_save_plugins()

if __name__ == "__main__":
    main()
