import requests
import json
 
# API_KEY = "填充你应用的API Key"
# SECRET_KEY = "填写你应用的Secret Key"
# 从 config.py 引入
from config import API_KEY, SECRET_KEY  # 导入密钥
 
def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()
 
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你要询问AI的内容"
            },
 
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
 
    response = requests.request("POST", url, headers=headers, data=payload)
 
    aso = response.text
    result = json.loads(aso)
    print(result['result'])
 
 
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
 
 
if __name__ == '__main__':
    main()