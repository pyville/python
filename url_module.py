def get_web(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('web page url?')
content = get_web(url)
print(content)