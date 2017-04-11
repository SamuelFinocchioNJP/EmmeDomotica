// Defines the connection settings and initializes the connection the mysql database
var mysql = require('mysql');

var db = mysql.createConnection ({
    host: 'localhost',
    user: 'root',
    password: '',
    port: 3306,
    database: 'EmmeDomotica'
});

db.connect();
module.exports = db;
