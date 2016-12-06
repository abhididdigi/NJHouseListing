import gpxpy.geo
from haversine import haversine

def diff((lat1,lon1),(lat2,lon2)):
    dist = haversine((lat1,lon1), (lat2,lon2), miles=True)
    return dist;

# Point one
lat1 = 40.7130
lon1 = 74.013

# Point two
# 40.661277,-74.116410,336
lat2 = 40.661277
lon2 = -74.116410

# What you were looking for
print diff((lat2,lon2),(lat1,lon1));


