import requests
import os
from dotenv import load_dotenv

load_dotenv()

CHATPDF_API_KEY = os.getenv("CHATPDF_API_KEY")

headers = {
    'x-api-key': CHATPDF_API_KEY,
    "Content-Type": "application/json",
}

message_1 = "I want you to work as a job description parser to extract the file's information.\
                Step 1: Can you give me the job title?\
                Step 2: Can you give me the working address of the job?\
                Step 3: Can you give me the job type of the job for example full-time, part-time, contract?\
                Step 4: Can you give me the job requirement of the job?\
                Step 5: Can you give me the benefits of the job?"
message_2 = "This is a job description. Can you give me the job title, working address, job type, job requirements, job benefits?\
            Give the answer in json format. If not available, please put 'null' "

data = {
    'sourceId': "src_TLjI8gd2GJmWs73nGGVEY",
    'messages': [
        {
            'role': "user",
            'content': message_2,
        }
    ]
}

response = requests.post(
    'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

if response.status_code == 200:
    print('Result:', response.json()['content'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)