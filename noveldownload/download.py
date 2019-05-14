import requests

def downloader():
    url = 'https://ck101.com/forum.php?mod=viewthread&tid=3039179&extra=page%3D1&page=1'
    data = requests.get(url)
    print(data)
    with open('text.txt', 'w') as f:
        f.write(data.text.encode('utf-8'))

downloader()