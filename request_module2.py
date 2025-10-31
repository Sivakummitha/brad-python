import requests
url="https://api.agify.io"
parameters={"name":"sivacharan"}
response=requests.get(url,params=parameters)
print(response.json())