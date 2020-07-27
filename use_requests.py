import requests

url = 'https://detik.com'
status = requests.get(url)
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        print(f'Content {response.content}')
    else:
        print(f'Woopss ada kesalahan {response.status_code}')
except Exception as e:
    print('There is an Error', e)
print('Program End')