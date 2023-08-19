import requests
import json
import time

# 定义API端点和间隔时间
api_url = "https://api.example.com/data"  # 替换为你实际使用的API端点
update_interval = 60  # 每60秒更新一次数据

def get_data_from_api():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

while True:
    data = get_data_from_api()
    if data:
        with open("data.json", "w") as file:
            json.dump(data, file)
        print("数据已更新并保存至data.json文件")
    else:
        print("无法从API获取数据")

    time.sleep(update_interval)
