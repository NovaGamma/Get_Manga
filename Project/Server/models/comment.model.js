const mongoose = require("mongoose");

const CommentSchema = mongoose.Schema({
  name: {type: String, required: true},
  title: {type: String, required: true},
  description: String,
  active: {type: Boolean, default: false}
});

module.exports = mongoose.model('Comment', CommentSchema);
