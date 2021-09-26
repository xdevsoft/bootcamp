from urllib import request

url = "http://python.org"
r = request.urlopen(url)
response_code = r.code
response_body = r.read()
print(response_body, response_code)
r.close()
