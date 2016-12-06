/**
 * Created by abhididdigi on 12/5/16.
 */
var spotcrime = require('spotcrime');

// somewhere near phoenix, az
var loc = {
  lat: 40.827679,
  lon: -74.152056
};

var radius = 0.2; // this is miles

spotcrime.getCrimes(loc, radius, function(err, crimes){
    console.log(crimes);
});
