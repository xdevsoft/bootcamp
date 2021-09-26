from urllib import request

filename = "mean.zip"
url = "http://ftp.lysator.liu.se/pub/awe32/soundfonts/{}".format(filename)
print("Downloading: {}".format(url))
r = request.urlopen(url)
print("Saving to: {}".format(filename))
f = open(filename, "wb")
f.write(r.read())
f.close()
r.close()
print("Done!")
