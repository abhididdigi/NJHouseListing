# 1. Go through every item in the table.
# 2. calculate the difference between latitude and longitude for all thr 290 stations and get the minimum.
# 3. update it back only if the distance is less than 200 000 00


import rethinkdb as r
import difference_points
conn = r.connect(db='test')

cursor = r.table("houselisting").run(conn);


for document in cursor:
        # 2. get the latitude and longitude.
        house_lat = document["lat"];
        house_lon = document["lon"];
        stop_cursor = r.table("rail_timings").run(conn);
        local_min = float("Inf");
        for stop_document in stop_cursor:

            hdist = difference_points.diff((float(house_lat),float(house_lon)),(float(stop_document["stop_lat"]),float(stop_document["stop_lon"])))
            if(local_min > hdist):
                local_min = hdist

        r.table("houselisting").get(document["id"]).update({"min_distance":local_min}).run(conn);

        # WTC co-ordinates..

        wtc = (40.661277,-74.116410)

        wdist = difference_points.diff((float(house_lat),float(house_lon)),wtc)
        if wdist < 35000000:
            r.table("houselisting").get(document["id"]).update({"office_distance":wdist}).run(conn)
        else:
            r.table("houselisting").get(document["id"]).update({"office_distance":float("Inf")}).run(conn)









