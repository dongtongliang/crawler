# -*- coding:utf-8 -*-
import re
import urllib2
import gzip
from StringIO import StringIO
import MySQLdb


conn= MySQLdb.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='1234',
        db ='test',
        charset="utf8",
        )
cur = conn.cursor()
b = []
a=[139,138,137,136,135,134,147,150,151,152,157,158,159,178,182,183,184,187,188,130,131,132,155,156,185,186,145,176,133,153,177,173,180,181,189,170,171]
for t in range(len(a)):
    url = 'http://www.jihaoba.com/haoduan/'+str(a[t])+'/guoluo.htm'
    response = urllib2.urlopen(url)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        html = f.read()
    else:
        html=response.read( )
        resultCourse = re.findall(r'<li class="hd-city01"><a href="(.*?)" target="_blank" title="(.*?)">(.*?)</a><\/li>', html,re.S)
        for i in range(len(resultCourse)):
            tis = str(resultCourse[i][2])
            cur.execute("insert into phone_city (phone,city) values ("+tis+",'果洛')")
            conn.commit()
            print resultCourse[i][2]
cur.close()
conn.close()





