var db = require ('../db');

// Insert query
exports.create = function(req, res) {
    var mac_address = req.body.mac_address;
    var descrizione = req.body.descrizione;
    var status = req.body.status;
    var number_value = req.body.number_value;
    var char_value = req.body.char_value;

    db.query("INSERT INTO device (mac_address, descrizione, status, number_value, char_value) VALUES (?, ?, ?, ?, ?)",
        [mac_address, descrizione, status, number_value, char_value],
        function(err, rows) {
            if(err)
                console.log("Error: %s", err);
            else
                res.json(rows);
        }
    );
};

// Select query
exports.read = function(req, res) {
    db.query('SELECT * FROM device', function(err, rows) {
        if(err)
            console.log("Error: %s", err);
        else
            res.json(rows);
    });
};

exports.update = function(req, res) {
    var mac_address = req.params.mac_address;
    var descrizione = req.body.descrizione;
    var status = req.body.status;
    var number_value = req.body.number_value;
    var char_value = req.body.char_value;
    db.query("UPDATE device SET descrizione = ?, status = ?, number_value = ?, char_value = ? WHERE mac_address = ?",
        [descrizione, status, number_value, char_value, mac_address],
        function(err, rows) {
            if(err)
                console.log("Error: %s", err);
            else
                res.json(rows);
        }
    );
};

exports.delete = function(req, res) {
    var mac_address = req.params.mac_address;
    db.query("DELETE FROM device WHERE mac_address = ?", [mac_address], function(err, rows) {
        if(err)
            console.log("Error: %s", err);
        else
            res.json(rows);
    });
};
