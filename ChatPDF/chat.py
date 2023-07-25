import requests
import os
from dotenv import load_dotenv

load_dotenv()

CHATPDF_API_KEY = os.getenv("CHATPDF_API_KEY")

headers = {
    'x-api-key': CHATPDF_API_KEY,
    "Content-Type": "application/json",
}

data = {
    'sourceId': "cha_rJUFb99cENZ28wru4341I",
    'messages': [
        # {
        #     'role': "user",
        #     'content': "Can you give me his name, email, phone and address? Output csv format.?",
        # },
        {
            'role': "user",
            'content': "<start>",
        },
        # {
        #     'role': "user",
        #     'content': "<start>I want you to work as a resume parser to extract candidate's information, email, phone and  working experience. Before going on, please YES if you understand.",
        # },
        # {
        #     'role': "user",
        #     'content': "Can you give me his name?",
        # },
        # {
        #     'role': "user",
        #     'content': "Can you give me his email?",
        # },
        # {
        #     'role': "user",
        #     'content': "Can you give me his phone?",
        # }
        # {
        #     'role': "user",
        #     'content': "What is his college and major? Output csv format",
        # }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)