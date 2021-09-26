from urllib import request

url = "http://ftp.lysator.liu.se/pub/awe32/soundfonts/mean.zip"
r = request.urlopen(url)
f = open("mean.zip", "wb"")
f.write(r.read())
f.close()
r.close()
