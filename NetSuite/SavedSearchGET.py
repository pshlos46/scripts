import urllib.request
import json
import pandas
import sys
from pandas.io.json import json_normalize
import csv

try:   
    url='<RESTlet-URL>&searchId='+sys.argv[1]
    # #######
    # ADD ENV VARS for CREDENTIALS BELOW
    # #######
    authorization = 'NLAuth nlauth_account=<accountid>,nlauth_email=<email>,nlauth_signature=<password>,nlauth_role=<role-internal-id>' 
    req = urllib.request.Request(url)
    req.add_header('Authorization', authorization)
    req.add_header('Content-Type','application/json')
    response = urllib.request.urlopen(req)
    rr = response.read()
    d = json.loads(rr)
    dnorm = json_normalize(data=d)
    dnorm = dnorm.to_csv()
    print(dnorm, file=open("SavedSearch"+sys.argv[1]+".csv", "w"))

except IOError as e:
    print("EXCEPTION OCCURRED--------------------")
    print("I/O error: {0}".format(e))
    print(e.headers)
    print(e.headers['www-authenticate'])




    