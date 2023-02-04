import urllib.request
from re import findall

url = "http://www.summet.com/dmsi/html/codesamples/addresses.html"

resp = urllib.request.urlopen(url)

html = resp.read()

htmlstr = html.decode()

pdata = findall("\(\d{3}\) \d{3}-\d{4}", htmlstr)

for item in pdata:
    print(item)
