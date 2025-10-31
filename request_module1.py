
import requests
response=requests.get('https://api.github.com')
print(response.status_code)
print("text is::::",response.text)
print("json_is:::",response.json())
print("headers:::",response.headers)
