import requests
import json
import rethinkdb as r

conn = r.connect(db='test')

cursor = r.table("houselisting").run(conn);

def rehash(o):
    o1 = {}
    for key in o:
        new_key = "u_"+str(key)
        o1[new_key] = o[key]
    return o1

for document in cursor:

    # Set the request parameters
    url = 'https://dev22327.service-now.com/api/now/import/u_import_house_listing'

    # Eg. User name="admin", Password="admin" for this code sample.
    
    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=json.dumps(rehash(document)))

    # Check for HTTP codes other than 200
    if response.status_code != 201:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)

