let express = require('express');
let app = express();
let request = require("request");
let parser = require('xml2js').parseString;

app.get('/', function (req, res) {


    let options = {
        method: 'GET',
        url: 'https://query.wikidata.org/sparql',
        qs: { query: 'SELECT * {wd:Q14317 p:P1082 ?nodo . ?nodo ps:P1082 ?poblacion . ?nodo pq:P585 ?momento}' },
        headers:
        {
            'Postman-Token': '4172e2b1-f59f-44c5-8550-86133584d1ab',
            'cache-control': 'no-cache'
        }
    };

    request(options, function (error, response, body) {
        if (error) throw new Error(error);
        let poblaciones = [];
        let years = [];
        let i;
        parser(body, function (err, result) {
            let numResultados = Object.keys(result['sparql']['results'][0]['result']).length;
            for (i = 0; i < numResultados; i++){
                poblaciones.push(result['sparql']['results'][0]['result'][i]['binding'][1]['literal'][0]['_']);
                years.push(result['sparql']['results'][0]['result'][i]['binding'][2]['literal'][0]['_'])
            }
            console.log(poblaciones );
            console.log(years);
            res.send(result);
        });
        
        
    });

    /*request(options, function (error, response, body) {
        if (error) throw new Error(error);
        let json = parser.xml2json(body);
        console.log(json['sparql']['results']['binding']);
        res.send(JSON.stringify(json, null, 4));
    });*/


});

app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});
