let express = require('express');
let app = express();
let swig  = require('swig');
let bodyParser = require('body-parser');
let methodOverride = require("method-override");

app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true })); 


app.use(methodOverride());
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE, PUT");
  res.header("Access-Control-Allow-Headers", "Access-Control-Allow-Headers,Authorization,Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.use(express.static('public'));

require("./routes/rdatos.js")(app,swig);


app.listen(3000, function () {
    console.log('Listening on port 3000!');
});
