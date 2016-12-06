import csv
import json
import rethinkdb as r


conn = r.connect(db='test')

table_name = "rail_timings";
csvfile = open('light_rail.csv', 'r')


fieldnames = ("id","stop_code","stop_name","stop_desc","stop_lat","stop_lon","zone_id")
#stop_id	stop_name	stop_desc	stop_lat	stop_lon
#fieldnames = ("id","stop_name","stop_desc","stop_lat","stop_lon")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    r.table(table_name).insert(row).run(conn)



