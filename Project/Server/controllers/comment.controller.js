const Comment = require('../models/comment.model.js');

exports.create = (req, res) => {
  const comment = new Comment({
    name: req.body.name,
    title: req.body.title,
    description: req.body.description,
    active: req.body.active
  })
  comment.save()
  .then(data => {
    res.send(data);
  }).catch(err => {
    res.status(500).send({
      message: err.message
    });
  });
};

exports.findAll = (req, res) => {
  Comment.find()
  .then(comments => {
    res.send(comments);
  }).catch(err => {
    res.status(500).send({
      message: err.message
    });
  });
}

exports.findOne = (req, res) => {
  Comment.findById(req.body.commentId)
  .then(comment => {
      if(!comment){
        return res.status(404).send({
          message: "Comment not found with id " + req.body.commentId
        });
      }
      res.send(comment);
  }).catch(err => {
    if(err.kind === 'ObjectId') {
      return res.status(404).send({
        message: "Comment not found with id " + req.body.commentId
      });
    }
    return res.status(500).send({
      message: "Error retrieving Comment with id " + req.body.commentId
    });
  });
}

exports.update = (req, res) => {
  Comment.findOneAndUpdate({ _id: req.body.commentId }, {
    name: req.body.name,
    title: req.body.title,
    description: req.body.description,
    active: req.body.active
  }, {new: true})
  .then(comment =>{
    if(!comment) {
      return res.status(404).send({
        message: "Comment not found with id " + req.body.commentId
      });
    }
    res.send(comment);
  }).catch(err => {
    if(err.king === 'ObjectId') {
      return res.status(404).send({
        message: "Comment not found with id " + req.body.commentId
      });
    }
    return res.status(500).send({
      message: "Error updating comment with id " + req.body.commentId
    });
  });
}

exports.delete = (req, res) => {
  Comment.findByIdAndRemove(req.body.commentId)
  .then(comment => {
    if(!comment) {
      return res.status(404).send({
        message: "Comment not found with id " + req.body.commentId
      });
    }
    console.log(req.user);
    res.send({message: "Comment deleted sucessfully"});
  }).catch(err => {
    if(err.kind === 'ObjectId' || err.name === 'NotFound') {
      return res.status(404).send({
        message: "Comment not found by id " + req.body.commentId
      });
    }
    return res.status(500).send({
      message: "Could not delete comment with id " + req.body.commentId
    });
  });
}

exports.deleteAll = (req, res) => {
  Comment.findAllAndRemove()
  .then(comments => {
    res.send(comments)
  }).catch(err => {
    res.status(500).send({
      message: err.message
    });
  });
}

exports.findByName = (req, res) => {
  Comment.find({name: req.query.name})
  .then(comments => {
      res.send(comments)
  }).catch(err => {
    res.status(500).send("Error -> " + err);
  });
}
