'use strict';

 module.exports = function(app) {
 let commentsList = require('../controllers/comment.controller');
 let userHandlers = require('../controllers/authController');

 // commentList Routes

 // get and post request for /comments endpoints
  app.route("/api/comments")
    .get(commentsList.findAll)
  app.route("/api/create_comment")
    .post(userHandlers.loginRequired, commentsList.create); // update with login handler
  app.route("/api/comment")
    .get(userHandlers.loginRequired, commentsList.findOne); // update with login handler
  app.route("/api/update_comment")
    .post(userHandlers.loginRequired, commentsList.update); // update with login handler
  app.route("/api/delete_comment")
    .post(userHandlers.loginRequired, commentsList.delete); // update with login handler
  app.route("/api/delete_comments")
    .post(userHandlers.loginRequired, commentsList.deleteAll); // update with login handler
  app.route("/api/comments_by_name")
    .get(commentsList.findByName); // update with login handler


/// rest of request defined in Routes politics

 // post request for user registration
 app.route("/auth/register")
  .post(userHandlers.register);

 // post request for user log in
 app.route("/auth/login")
  .post(userHandlers.signIn);
}
