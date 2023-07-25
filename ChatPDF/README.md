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