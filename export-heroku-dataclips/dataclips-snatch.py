import json
import requests

# grab a valid cookie while browsing to the https://dataclips.heroku.com/ or else it won't work (Inspect -> Network tab, load the page, dataclips.heroku.com -> Response Headers -> Set-Cookie)
# I've left the different fields below to let you know exactly which part of the cookie to grab

cookies = {
'dataclips-sso-session':'<cookie-string>; path=/; expires=Mon, 04 Jun 2018 13:42:40 -0000; secure; HttpOnly'
}

headers = {
}

response = requests.get('https://dataclips.heroku.com/api/v1/clips/', headers=headers, cookies=cookies)

	
count = 1
json_data = json.loads(response.text)

# keep a json of the summary

with open('all-dataclips-summary.json', 'w') as f:
	print >> f, json.dumps(json_data)
lista = []

# iterate and grab each one of them

for item in json_data:
	dt = item['slug']
	r2 = requests.get('https://dataclips.heroku.com/api/v1/clips/'+dt, headers=headers, cookies=cookies)
	jdata2 = json.loads(r2.text)
	lista.append(jdata2)
	print "processed \"" + jdata2['name'] + "\" succesfully and added to list, dataclip number " + str(count)
	count += 1

print "Dataclip dumping has ended"
	
with open('all-dataclips-detailed.json', 'w') as f:
	print >> f, json.dumps(lista, sort_keys=True)



