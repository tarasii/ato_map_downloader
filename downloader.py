import datetime
import urllib2
import os.path
import re


path = 'D:/prg/ato/'

#finds last downloaded file 
start_dt = datetime.date(2015,1,1) #default start day 01.01.2015
l = [f for f in os.listdir(path) if re.match('ato\d{8}\.(png|jpg)', f)]
l.sort()
if l:
  last_fn = l[-1]
  dtl = [int(last_fn[3:7]),int(last_fn[7:9]),int(last_fn[9:11])]
  start_dt = datetime.date(dtl[0],dtl[1],dtl[2]) + datetime.timedelta(1)

print start_dt

#today
cur_dt = datetime.date.today()
tmp_dt = start_dt

#saves image from url to file 
def process_dt(dt):
  html_str = "http://mediarnbo.org/wp-content/uploads/%04d/%02d/%02d-%02d.jpg" % (tmp_dt.year, tmp_dt.month, tmp_dt.day, tmp_dt.month)

  file_str = path + "ato%04d%02d%02d.jpg" % (tmp_dt.year, tmp_dt.month, tmp_dt.day)

  if not os.path.isfile(file_str):
    try:
      response = urllib2.urlopen(html_str)
      html = response.read()
    
    except:
      print "--", html_str

    else:
      print file_str, html_str
      #print html
      f = open(file_str, 'wb')
      f.write(html)
      f.close()


  else:
    print "-", file_str, html_str
    

#get images from startday to today 
while tmp_dt <= cur_dt:
  process_dt(tmp_dt)
  tmp_dt = tmp_dt + datetime.timedelta(1)
  
