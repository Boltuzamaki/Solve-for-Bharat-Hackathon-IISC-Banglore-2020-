import requests

url = "http://172.27.74.255//dashboard//save_image.php"
files = {'image':open('sample.png','rb')}
try:
	response = requests.post(url,files= files, timeout = 60)
	print (response)
except:
        pass
