from urllib import request

r = request.urlopen("http://python.org")
print(r.read())
r.close()
