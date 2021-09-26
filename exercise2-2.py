from urllib import request

def download(filename, url):
    url = "{}{}".format(url, filename)
    print("Downloading: {}".format(url))
    r = request.urlopen(url)
    print("Saving to: {}".format(filename))
    f = open(filename, "wb")
    f.write(r.read())
    f.close()
    r.close()
    return "Done!"

filename = "mean.zip"
url = "http://ftp.lysator.liu.se/pub/awe32/soundfonts/"
status = download(filename, url)
print(status)
