from urllib import request

def http_get(url):    
    r = request.urlopen(url)
    response_code = r.code
    response_body = r.read()
    r.close()
    return (response_code, response_body)


code, body = http_get("http://python.org")
print(body, code)
