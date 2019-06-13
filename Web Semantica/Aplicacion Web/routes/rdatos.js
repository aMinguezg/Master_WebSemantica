let request = require("request");
let parser = require('xml2js').parseString;

module.exports = function(app, swig) {

	app.get('/', function (req, res) {


        let resultado = swig.renderFile('views/index.html', {
        });
        res.send(resultado)
    });


    app.get('/:id', function (req, res) {

        let options = {
            method: 'GET',
            url: 'https://query.wikidata.org/sparql',
            qs: { query: 'SELECT * {wd:'+req.params.id+' p:P1082 ?nodo . ?nodo ps:P1082 ?poblacion . ?nodo pq:P585 ?momento}' },
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
                    let tempYear = result['sparql']['results'][0]['result'][i]['binding'][2]['literal'][0]['_']
                    let year = tempYear.substring(0,4);
                    years.push(year)
                }
                console.log(poblaciones );
                console.log(years);
                let resultado = swig.renderFile('views/index.html', {
                    poblaciones: poblaciones
                });
                
                res.send(resultado)
            });       
        });    
    });

    app.post('/', function (req, res) {

        let options = {
            method: 'GET',
            url: 'https://query.wikidata.org/sparql',
            qs: { query: 'SELECT * {wd:'+req.body.ciudad+' p:P1082 ?nodo . ?nodo ps:P1082 ?poblacion . ?nodo pq:P585 ?momento}' },
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
                    let tempYear = result['sparql']['results'][0]['result'][i]['binding'][2]['literal'][0]['_']
                    let year = tempYear.substring(0,4);
                    years.push(year)
                }
                console.log(poblaciones );
                console.log(years);
                let resultado = swig.renderFile('views/data.html', {
                    poblaciones: poblaciones
                });
                
                res.send(resultado)
            });       
        });    
    });

};
