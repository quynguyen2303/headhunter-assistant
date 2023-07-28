import requests
import os
from dotenv import load_dotenv

load_dotenv()

CHATPDF_API_KEY = os.getenv("CHATPDF_API_KEY")

filePath = "job_description/Qode HCMC_Full-stack Engineer.pdf"

files = [
    ('file', ('file', open(filePath, 'rb'), 'application/octet-stream'))
]

headers = {
    'x-api-key': CHATPDF_API_KEY
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)