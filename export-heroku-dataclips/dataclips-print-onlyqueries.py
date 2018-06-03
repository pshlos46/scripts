# use dataclips-snatch.py to snatch the dataclips
# You can print the queries, names, slug only in readable format using this

import json

with open('all-dataclips-detailed.json') as json_data:
	jl = json.load(json_data)

count = 1	
for i in jl:
	print "----------------------------------\n"
	print "Number: " + str(count) + "\n"
	print "name: " + i['name'] 
	print "slug: " + i['slug'] 
	print "----------------------------------\n"
	print i['sql']
	print "----------------------------------"
	print "----------------------------------"
	print "----------------------------------\n"
	count +=1
	
	
	
	
	


