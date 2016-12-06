
r = require('rethinkdb');
_ = require('underscore');
var spotcrime = require('spotcrime');

var radius = 0.1;


var connection = null;



r.connect( {host: 'localhost', port: 28015}, function(err, conn) {
    if (err) throw err;
    connection = conn;


    r.table('houselisting').run(connection, function(err, cursor) {
    if (err) throw err;
    cursor.toArray(function(err, result) {
        if (err) throw err;
        for(var i= 0, len = result.length; i< len ; i++){


            var house_listing = result[i];



            if(house_listing["crime_data"] == true)
                continue;

            createCrime(house_listing);


        }
    });
});});


function createCrime(house_listing){

            // get latitude and longitude.
            var loc = {
                lat:house_listing["lat"],
                lon:house_listing["lon"]
            };

            var id = house_listing["id"];

            spotcrime.getCrimes(loc,radius,function(err,crimes){

                console.log("getting crimes for id = " + id + " and the crimes = " + crimes);
                if(err) return;
                if(_.isUndefined(crimes)) {
                    r.table("houselisting").get(id).update({"crime_data":true}).run(connection);
                    return;
                }
                for(var i= 0, len = crimes.length; i < len ; i ++) {
                    var crime = crimes[i];
                    crime["houseId"] = id;
                    r.table("crimedata").insert(crime).run(connection,function(err,row){
                        if(err) console.log("The error = ", err);
                    });
                }

                r.table("houselisting").get(id).update({"crime_data":true}).run(connection);

            });
}


