var express = require("express"),
    app = express(),
    mongoose = require("mongoose"),
    port = 8000,
    request = require('request'),
    views = __dirname + "/views/",
    mongoSanitize = require('express-mongo-sanitize'),
    https = require('https'),
    url = "mongodb+srv://ExternalUser:7ZKqWRIRgvP4tF4I@recommendationrulesamer.a7xea.mongodb.net/anime?retryWrites=true&w=majority";


mongoose.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})

app.set('view engine', 'ejs');
app.use(express.static(__dirname + "style"));
app.use(mongoSanitize());


app.get("/", function (req, res) {
    /*
    const options = {
        hostname: 'localhost',
        port: 8080,
        path: '/',
        method: 'GET'
      }
      
      const newRequest = https.request(options, newResponse => {
        
        console.log(`statusCode: ${newResponse.statusCode}`)
      
        newResponse.on('data', d => {
          process.stdout.write(d)
        })
      })
      
      newRequest.on('error', error => {
        console.error(error)
      })
      
      newRequest.end()
      */
    var dummy = "didnt work"
    request('http://127.0.0.1:8080/', function (error, response, body) {
        console.error('error:', error); // Print the error
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        console.log('body:', body); // Print the data received
        dummy = body;
        console.log("Dummy: "+dummy);
        // console.log("Dummy2: "+dummy);
        res.render("index.ejs",{ dum: dummy});
        // res.send(body); //Display the response on the website
    });
    
});

app.listen(port, function () {
    console.log("Server Started")
});