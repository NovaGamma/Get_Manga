const User = require("../models/userModel");

const config = require("../config/auth.config")

const jwt = require('jsonwebtoken');

const bcrypt = require('bcryptjs');

exports.register = (req, res) => {
  let newUser = new User(req.body);
  newUser.hash_password = bcrypt.hashSync(req.body.password, 10);
  newUser.role = "user";

  newUser.save((err, user) => {
    if(err){
      res.status(500).send({message: err});
    }
    user.hash_password = undefined;
    res.status(201).json(user);
  });
}

exports.signIn = (req, res) => {
  User.findOne({
    email: req.body.email},
    (err, user) => {
      if (err) throw err;
      if(!user){
        res.status(401).json({message: 'Authentification failed. User not found'});
      } else if (user){
          if(!user.comparePassword(req.body.password)){
            res.status(401).json({message: 'Authentification failed. Wrong password'});
          } else {
            res.json({token: jwt.sign({email: user.email, fullName: user.fullName, _id: user._id, role: user.role}, config.secret, {expiresIn: 86400})
          });
        }
      }
    });
}

exports.loginRequired = (req, res, next) => {
  if(req.user){
    //res.json({message: 'Authorized User, Action Sucessful'});
    next()
  } else {
    res.status(401).json({message: 'Unauthorized user'});
  }
}
