import requests

name = input("Enter the website you want to make an imperfect copy of (use https://) -   ")
r = requests.get(name)

status_code = r.status_code
if status_code >= 200 and status_code < 300 :
	page = open("copy.html","w+")
	page.write(r.text)