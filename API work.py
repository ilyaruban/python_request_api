import requests

token_1 = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        with open('Python.jpg', 'rb') as file:
            response_1 = requests.put(path_to_file, files={'file': file})

if __name__ == '__main__':
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    params = {'path': 'Image/Python.jpg'}
    headers = {'Authorization': token_1}
    response = requests.get(url, headers=headers, params=params)
    path_to_file = response.json().get('href', '')
    token = token_1
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)