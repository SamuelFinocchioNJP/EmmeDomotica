// Domotica rest server
// Developed 11/04/2017

// Libraries import
var express = require('express');
var cors = require('cors');
var bodyParser = require('body-parser');

// Server configuration
var port = 8000;
var app = module.exports = express();
app.use(cors());

// Adding body-parser to support json encoding
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

// Import controllers
require ('./controller/device');

// Import model
require ('./model/device');

// Initialized the server
app.listen(port, function() {
    console.log("EmmeDomotica listening on port " + port);
});
