<template>
<div class="comment">
  <div v-if="editing">
    <input v-model="title" :placeholder="data.title">
    <input v-model="description" :placeholder="data.description">
    <button @click='submit'>Submit</button>
  </div>
  <div v-else>
    {{data.name}}
    <br>
    {{data['title']}}
    <p v-if='data.active'>
    {{data['description']}}
    </p>
    <button @click='edit'>Edit</button>
  </div>
  <button @click='hide'>Hide</button>
  <button @click='del'>Delete</button>
</div>
</template>

<script>
import VueJwtDecode from "vue-jwt-decode";
export default {
  name: 'Comment',
  emits:['update'],
  data(){
    return {
      title:'',
      description:'',
      editing:false
    }
  },
  props:{
    data:{
    type: Object
    }
  },
  methods:{
    getUser(){
      if(localStorage.jwt == undefined) return false;
      let decoded = VueJwtDecode.decode(localStorage.getItem('jwt'));
      if(decoded.exp < Date.now()/1000) this.$router.push('/Login');
      this.user = decoded;
    },
    checkOwner(){
      if (this.getUser() == false) return false;
      if(this.user.fullName == this.data.name || (this.user.fullName == "Admin" && this.user.email == "admin@test.com")){
        return true;
      }
      return false;
    },
    submit(){
      if(!this.checkOwner()){
        alert("you are not the author of this comment, you cannot modify it")
        return
      }
      this.editing = false;
      fetch("http://localhost:5000/api/update_comment",{
        method:"POST",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'JWT ' + localStorage.jwt,
        },
        body: JSON.stringify({
          commentId:this.data._id,
          name:this.data.name,
          title: this.title != "" ? this.title : this.data.title,
          description:this.description != "" ? this.description : this.data.description,
          active:this.data.active
        })
      }).then(result => this.$emit("update"))
    },
    edit(){
      if(!this.checkOwner()){
        alert("you are not the author of this comment, you cannot modify it")
        return
      }
      this.editing = true;
    },
    hide(){
      if(!this.checkOwner()){
        alert("you are not the author of this comment, you cannot modify it")
        return
      }
      let activeValue = !this.data.active
      fetch("http://localhost:5000/api/update_comment",{
        method:"POST",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'JWT ' + localStorage.jwt,
        },
        body: JSON.stringify({
          commentId:this.data._id,
          name:this.data.name,
          title:this.data.title,
          description:this.data.description,
          active:activeValue
        })
      }).then(result => this.$emit("update"))
    },
    del(){
      if(!this.checkOwner()){
        alert("you are not the author of this comment, you cannot modify it")
        return
      }
      fetch("http://localhost:5000/api/delete_comment",{
        method:"POST",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'JWT ' + localStorage.jwt,
        },
        body: JSON.stringify({commentId:this.data._id}),
      }).then(result => this.$emit("update"))
    }
  }
}
</script>
<style>
  .comment{
    border: 15px solid green;
  }
</style>
