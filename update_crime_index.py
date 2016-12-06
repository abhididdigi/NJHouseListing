import rethinkdb as r
conn = r.connect(db='test')

housing_table_name = "houselisting"
crime_table_data = "crimedata"



crime_rating = {"Arrest":5,"Arson":5,"Assault":8,"Burglary":10,"Other":3,"Robbery":8,"Shooting":10,"Theft":8,"Vandalism":8}

housing_cursor = r.table(housing_table_name).run(conn);
for document in housing_cursor:
    housing_id = document["id"];
    total_crime_index = 0;
    # get all the items from the crimedata

    crime_cursor = r.table(crime_table_data).filter({"houseId":housing_id}).group("type").run(conn);

    ungrouped_crime_custor = r.table(crime_table_data).filter({"houseId":housing_id}).count()


    for i in crime_cursor:

        group = crime_cursor[i]
        group_magnitude = crime_rating[i];
        total_crime_index = total_crime_index + (group_magnitude * len(group))

    magnitude_crime_index = total_crime_index / ungrouped_crime_custor
    r.table(housing_table_name).get(housing_id).update({"crime_data_index":magnitude_crime_index},non_atomic = True).run(conn);



