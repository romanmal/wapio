import urllib3
#import xml.etree.ElementTree as ET
import requests
import csv
import os
urllib3.disable_warnings()

user = os.environ.get('APIUSER')
passw = os.environ.get('APIPASS')

# getting list of files
r = requests.get('https://download.wattsight.com/list-files?response-as=csv', auth=(user, passw), verify=False)
r.status_code
decoded = r.content.decode('utf-8')
cr = csv.reader(decoded.splitlines(), delimiter=';')
my_list = list(cr)
for row in my_list:
    print(row)

# getting files
f = requests.get('https://download.wattsight.com/download-file?file=CON_POW_H_F&area=np', auth=(user, passw), verify = False)
decoded = f.content.decode('utf-8')
cr = csv.reader(decoded.splitlines(), delimiter=';')
my_list = list(cr)
for row in my_list:
    print(row)


f = requests.get('https://download.wattsight.com/download-file?file=PRO_WND_H_F&area=np', auth=(user, passw), verify=False)
decoded = f.content.decode('utf-8')
cr = csv.reader(decoded.splitlines(), delimiter=';')
my_list = list(cr)
for row in my_list:
    print(row)

f = requests.get('https://download.wattsight.com/download-file?file=PRO_NUC_H_F&area=np', auth=(user, passw))
decoded = f.content.decode('utf-8')
cr = csv.reader(decoded.splitlines(), delimiter=';')
my_list = list(cr)
for row in my_list:
    print(row)


f = requests.get('https://download.wattsight.com/download-file?file=PRI_EXC_INSTANTSPOT_H_F&area=de', auth=(user, passw))
decoded = f.content.decode('utf-8')
cr = csv.reader(decoded.splitlines(), delimiter=';')
my_list = list(cr)
for row in my_list:
    print(row)
