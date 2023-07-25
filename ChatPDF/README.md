## ChatPDF Solution
Link: https://www.chatpdf.com/docs/api/backend


### Example for Add PDF via URL

```
import requests

headers = {
  'x-api-key': 'sec_xxxxxx',
  'Content-Type': 'application/json'
}
data = {'url': 'https://api.chatpdf.com/v1'}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-url', headers=headers, json=data)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)
```

### Example for Add PDF via File

```
import requests

files = [
    ('file', ('file', open('/path/to/file.pdf', 'rb'), 'application/octet-stream'))
]
headers = {
    'x-api-key': 'sec_xxxxxx'
}

response = requests.post(
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

if response.status_code == 200:
    print('Source ID:', response.json()['sourceId'])
else:
    print('Status:', response.status_code)
    print('Error:', response.text)
```

### Chat with PDF

```
import requests

headers = {
    'x-api-key': 'sec_xxxxxx',
    "Content-Type": "application/json",
}

data = {
  "sourceId": "src_xxxxxx",
  "messages": [
    {
      "role": "user",
      "content": "How much is the world?"
    },
    {
      "role": "assistant",
      "content": "The world is 10 dollars."
    },
    {
      "role": "user",
      "content": "Where can I buy it?"
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
```

### Reference sources

```
{
  "referenceSources": true,
  "sourceId": "src_xxxxxx",
  "messages": [
    {
      "role": "user",
      "content": "how much is the world?"
    }
  ]
}
```