import requests
from requests.auth import HTTPBasicAuth
host = 'http://<ip_addr>/domjudge/'
res = requests.get(host + 'feed/ext.php', auth=HTTPBasicAuth("<event_reader_username>", "<event_reader_password>"))
f = open("ext.xml", "w", encoding='utf8')
f.write(res.text)