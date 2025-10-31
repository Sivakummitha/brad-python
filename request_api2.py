import requests
url="https://api.open-meteo.com/v1/forecast?latitude=17.385&longitude=78.4867&current_weather=true"
res=requests.get(url)
data=res.json()
print("city:hyderabad")
print("tempararture:",data['current_weather']['temperature'],"c")
print("windspeed:",data['current_weather']['windspeed'],"km/h")
print(res.json())