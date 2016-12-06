from craigslist import CraigslistHousing
import rethinkdb as r
import requests


cl = CraigslistHousing(site='newjersey', category='apa',
                         filters={'max_price': 2000, 'min_price': 1300, 'has_image':True})

conn = r.connect(db='test')


# given latitude and longitude, return
def get_geographic_location(lat,long):
    url = "http://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(long)+"&sensor=false"

    r = requests.get(url)
    place = r.json();

    try:
        county =  place["results"][1]["formatted_address"]
    except:
        county  = '';

    return county;



def insert_records(table_name,o):


    cursor = r.table(table_name).get_all(o["id"],index="postId").run(conn)
    repo = dto_to_repo(o);


    for document in cursor:
        print "an update is happening..."+document["id"];
        r.table(table_name).get(document["id"]).replace(repo);
        return;

    if(o["has_map"] == False or o["geotag"] == None):
        return



    r.table(table_name).insert(repo).run(conn)


def dto_to_repo(o):

    if o["geotag"] == None:
        lat = -1
        long = -1
    else:
        (lat,long) = o["geotag"]
    division = str(o["where"])
    print("division = " + str(division));
    repo = {"postId": o["id"] ,
    "lat": lat,
    "lon": long,
    "link": o["url"],
    "price":o["price"],
    "division":o["where"],
    "crime_data":False,
    "crime_data_index":"100"
    };

    return repo;




results = cl.get_results(sort_by='newest', geotagged=True)
for result in results:
    insert_records("houselisting",result)







