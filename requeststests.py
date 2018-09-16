# This piece of code helps create an imperfect copy of the page you wish to emulate, try https://www.facebook.com for best results

import requests

name = input("Enter the website you want to make an imperfect copy of (use https://) -   ")
r = requests.get(name)

status_code = r.status_code
if status_code >= 200 and status_code < 300 :
	page = open("copy.html","w+")
	page.write(r.text)