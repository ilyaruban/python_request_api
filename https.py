import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
max = response.json()[0]['powerstats']['intelligence']
dict = {}
for i in response.json():
    if i['name'] == 'Hulk' or i['name'] == 'Captain America' or i['name'] == 'Thanos':
        if i['powerstats']['intelligence'] > max:
            max = i['powerstats']['intelligence']
            dict[max] = i['name']
for n in dict.keys():
    if n == max:
        print(dict[n])
