import urllib
import urllib2

import sys

if len(sys.argv) < 4:
    print "usage: %s url pid fid" % (sys.argv[0])
else:
    url = sys.argv[1]
    pid = sys.argv[2]
    fid = sys.argv[3]

    params = {'file_id':fid, 'printer_id':pid}

    data = urllib.urlencode(params)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()

    print the_page
