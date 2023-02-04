# https://www.youtube.com/watch?v=tJxcKyFMTGo&feature=youtu.be

import os
import urllib.request
import datetime
import sys

from DefaultItems import DataFolder

print("Python Version: ",sys.version)

def main():

    #### print out current working directory
    print("getcwd(): ",os.getcwd())

    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    data = u.read()

    file_and_path = os.path.join(DataFolder, "rt22.xml")
    with open(file_and_path, 'wb') as f:
        f.write(data)

    ##### parse the xml file
    from xml.etree.ElementTree import parse
    doc = parse(file_and_path)

    daves_latitude = 41.980262
    daves_latitude = 41.880262
    daves_longitude = -87.668452

    candidates = []
    for bus in doc.findall('bus'):
        d = bus.findtext('d')
        lat = float(bus.findtext('lat'))
#        if lat > daves_latitude:
        if 1 == 1:
            direction = bus.findtext('d')
            if direction.startswith('North'):
                busid = bus.findtext('id')
                candidates.append(busid)

    for idx, val in enumerate(candidates):
        sentence = "line 38: idx: {0} val: {1}".format(idx, val)
        #print(sentence)

    def distance(lat1, lat2):
        return 69 * abs(lat1-lat2) # in miles

    def monitor():
        # haversine
        u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
        doc = parse(u)
        for bus in doc.findall('bus'):
            now = datetime.datetime.now()
            sent = "{0:%Y_%m_%d_%H:%M:%S}".format(now)

            busid = bus.findtext('id')
            if busid in candidates:
                lat = float(bus.findtext('lat'))
                dis = distance(lat, daves_latitude)
                sentence = "line 53: {0} busid: {1}, lat: {2:.4f}, dist: {3:.4f}".format(sent, busid, lat, dis)
                print(sentence)


    import time
    #while True:
    #    monitor()
    #    time.sleep(10)
    monitor()
    import webbrowser
 #   webbrowser.open('http://www.espn.com')
     # find all busses that are traveling  nortbound of Dave's office

    now = datetime.datetime.now()
    sentence = "Current time is: {0:%Y_%m_%d_%H:%M:%S}".format(now)
    print(sentence)




if __name__ == '__main__':
    main()
