let express = require('express');
let app = express();
let swig  = require('swig');
let bodyParser = require('body-parser');
app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true })); 


app.use(express.static('public'));

require("./routes/rdatos.js")(app,swig);




app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});
