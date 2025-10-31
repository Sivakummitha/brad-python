import requests
response=requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
urls=["https://api.github.com","https://api.github.com/unknown"]
for url in urls:
    res=requests.get(url)
    print(url,res.status_code)