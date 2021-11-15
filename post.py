import requests

url = "http://127.0.0.1:5000/search?username=mohamed&password=54584855"

payload = "{\"username\":\"mohamed\", \"password\":1234}\r\n"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
