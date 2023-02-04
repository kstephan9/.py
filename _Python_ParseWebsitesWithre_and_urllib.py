# https://www.youtube.com/watch?v=GEshegZzt3M
# Python 3 Programming Tutorial - Parsing Websites with re and urllib
#
# sentdex
#
import os
import urllib.request
import urllib.parse
import re


def main():
 
    ##### other methods/attributes of os.path
    print("getcwd(): ",os.getcwd())

    url = 'http://pythonprogramming.net'
    values = {'s':'basics',
              'submit':'search'}
    
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    #print(respData)
    
    paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
    for eachP in paragraphs:
        print("31: ", eachP)
    

if __name__ == '__main__':
    main()
