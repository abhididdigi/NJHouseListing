import rethinkdb as r

house_listing_table_name = "houselisting"
crime_data_table_name = "crimedata"
conn = r.connect(db='test')

r.table(house_listing_table_name).delete().run(conn);
r.table(crime_data_table_name).delete().run(conn)
