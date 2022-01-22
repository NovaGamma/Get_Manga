const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const jwt = require("jsonwebtoken");

mongoose.Promise = global.Promise;

const uri = "mongodb+srv://Elvin:GZhijs6m7aMYU8q@cluster0.nkrp5.mongodb.net/efrei?retryWrites=true&w=majority"
mongoose.connect(uri,{useNewUrlParser: true, useUnifiedTopology: true})
  .then(()=>{console.log("Database Connected");
             console.log("Sucessfully connected to MongoDB");
           }).catch(err=>{
             console.log(err);
             console.log("Could not connect to MongoDB");
           })


var corsOptions = {
  origin: "http://localhost:8080"
};

const app = express();
app.use(cors(corsOptions));

app.use(express.json());
app.use(express.urlencoded({extended:true}));

const config = require('./config/auth.config.js')
app.use((req, res, next) => {
  if(req.headers && req.headers.authorization && req.headers.authorization.split(' ')[0] === 'JWT'){
    jwt.verify(req.headers.authorization.split(' ')[1], config.secret, (err, decode) => {
      if(err) req.user = undefined;
      req.user = decode;
      next();
    });
  } else {
    req.user = undefined;
    next();
  }
});


require('./routes/comment.routes.js')(app);
app.get("/", (req, res) => {
  res.json({message: "Server lives!!!"});
});

app.listen(5000, () => {
  console.log("Server has started!")
})
