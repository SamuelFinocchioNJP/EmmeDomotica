var device = require ('../model/device');
var app = require ('../app');

app.post('/device/create', device.create);

app.get('/device/read', device.read);

app.put('/device/update/:mac_address', device.update);

app.delete('/device/delete/:mac_address', device.delete);
