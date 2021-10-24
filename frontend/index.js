var express = require("express"),
    app = express(),
    mongoose = require("mongoose"),
    port = 8000,
    request = require('request'),
    views = __dirname + "/views/",
    mongoSanitize = require('express-mongo-sanitize'),
    url = "mongodb+srv://ExternalUser:7ZKqWRIRgvP4tF4I@recommendationrulesamer.a7xea.mongodb.net/anime?retryWrites=true&w=majority";


mongoose.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})

app.set('view engine', 'ejs');
console.log("dirname: "+__dirname+ "/static");

app.use(express.static(__dirname));

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
        res.render("index.ejs",{ dum: dummy, q: ""});
        // res.send(body); //Display the response on the website
    });
    
});


app.get("/search", function (req, res) {
  noMatch = "",
  dataTotal = []
  // console.log(req.query.sorted);
  if (req.query.search.length > 1) {

      const regex = new RegExp(escapeRegex(req.query.search), 'gi');
      // Get all campgrounds from DB
      Anime.find({
          Left: {
              $regex: regex
              // $regex: "left3"
          }
      }, {
          _id: 0,
          __v: 0
      }, function (error, data) {
          if (error) {
              console.log(err);
          } else {

              data.forEach(x => {
                  //console.log(dataTotal);
                  // x["Confidence"] = x["Confidence"].substring(0, 6);
                  dataTotal.push(x);
              });
              //console.log(data);
          }

          // console.log(dataTotal);
          res.render("index.ejs", { data: sortResults(dataTotal, req.query.sorted), noMatch: noMatch, sort: sort, q: req.query.search, q2: req.query.sorted });
      });



  } else {
      // Get all animes from DB
      Anime.find({}, function (err, data) {
          if (err) {
              console.log(err);
          } else {
              res.render("index.ejs", { data: sortResults(dataTotal), noMatch: noMatch, sort: sort, q: "", q2: "None" });
          }
      });
  }
});

function escapeRegex(text) {
  return text.replace(/[-[\]{}()*+?.,\\^$|#\s]/, "\\$&");
};




app.listen(port, function () {
    console.log("Server Started")
});