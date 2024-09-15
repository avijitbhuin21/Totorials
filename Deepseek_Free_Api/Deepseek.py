import requests
import json


class deepseek_chat:
    def __init__(self, authorization):
        self.authorization = authorization
        print("Models Available:",'deepseek_chat', 'and deepseek_code')
    
    def get_text_response(self,response):
        content = ""
        for line in response.iter_lines():
            if line and line.decode('utf-8').startswith("data:"):
                data = json.loads(line.decode('utf-8')[5:])
                content += data.get('choices', [{}])[0].get('delta', {}).get('content', '')
        return content 

    def ask(self, question, model = 'deepseek_chat')-> str: #deepseek_code for deepseek coder v2.5
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {self.authorization}',
            'content-type': 'application/json',
            'origin': 'https://chat.deepseek.com',
            'priority': 'u=1, i',
            'referer': 'https://chat.deepseek.com/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
            'x-app-version': '20240126.0',
        }
        json_data = {
            'message': question,
            'stream': True,
            'model_preference': None,
            'model_class': model,
            'temperature': 0,
        }
        res = requests.post('https://chat.deepseek.com/api/v0/chat/completions',headers=headers, json=json_data)
        return self.get_text_response(res)
