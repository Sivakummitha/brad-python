import requests
import urllib.request

url = input('Webpage to grab source from: ')
html_output_name = input('Name for html file: ')

req = request.get(url, 'html.parser')

with open(html_output_name, 'w') as f:
    f.write(req.text)
    f.close()
