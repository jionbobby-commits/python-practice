import requests

#目标网站
target_url = "https://www.tiobe.com/"

# 发送GET请求
response = requests.get(target_url)

# 输出文本
print(response.text)

