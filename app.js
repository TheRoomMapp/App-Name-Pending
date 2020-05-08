const express = require('express');
const app = express();
const path = require('path');

//used to grab user inputs - see use of urlencodedParser variable. 
const bodyParser=require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: true })

app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs')
app.use(express.static(__dirname+ '/public'));


// Home page
app.get('/', function(req, res){
	res.render('pages/index');
});

// displays the results of the python file on the /results page
app.post('/results', urlencodedParser, function(req, res){
    // console.log(req.body);
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./python_code/roomour_f2019.py", 
                                    req.body.weekday, 
                                    req.body.option = 1,
                                    req.body.start,
                                    req.body.end] );

    process.stdout.on('data', function(data) {
    //console.log(data.toString());
    // console.log(typeof data);
    res.render('pages/results', {data: data, values: req.body})
    })



});


// displays the results of the python file on the /results page
app.post('/resultsTwo', urlencodedParser, function(req, res){
    console.log(req.body);
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./python_code/roomour_f2019.py", 
                                    req.body.weekday, 
                                    req.body.option = 2,
                                    req.body.buildingNum,
                                    req.body.roomNum] );

    process.stdout.on('data', function(data) {
    console.log(data.toString());
    res.render('pages/resultsTwo', {data: data, values: req.body})
    })


});


// start server
app.listen(process.env.PORT || 5000, function(){
	console.log('server started on port 5000');
})