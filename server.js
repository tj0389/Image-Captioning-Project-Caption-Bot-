let express=require("express");
// const {spawn} = require('child_process');
require('dotenv').config();
let app=express();
var port=process.env.PORT || 8000;

app.use(function(req,res,next){
    console.log(`${new Date()} - ${req.method} request for ${req.url}`);
    next();
});

app.use(express.static("static"));

app.get('/', (req, res) => {

    res.sendFile(__dirname+'/index.html');
 
    // var dataToSend;
    // // spawn new child process to call the python script
    // const python = spawn('python', ['script1.py']);
    // // collect data from script
    // python.stdout.on('data', function (data) {
    //  console.log('Pipe data from python script ...');
    //  dataToSend = data.toString();
    // });
    // // in close event we are sure that stream from child process is closed
    // python.on('close', (code) => {
    // console.log(`child process close all stdio with code ${code}`);
    // // send data to browser
    // res.send(dataToSend)
    // });
    
   });

app.listen(port,() => {
    console.log(`Running on server at http://localhost:${port}/`);
});
