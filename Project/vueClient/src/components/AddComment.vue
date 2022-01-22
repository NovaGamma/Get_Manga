<template>
 <div>
   Name: {{user.fullName}}
   <br>
   Title:
   <input v-model="title" type="text" placeholder="title"/><br>
   Review:
   <input v-model="description" type="text" placeholder="your review"/>
   <button @click="submit">Submit</button>
 </div>
</template>

<script>
import VueJwtDecode from "vue-jwt-decode";
export default {
 name: 'AddComment',
 data(){
   return {
     name:'',
     title:'',
     description:'',
     jwt:'',
     user:{}
   }
 },
 mounted(){
   if(localStorage.jwt){
     this.jwt = localStorage.jwt;
   }
   let decoded = VueJwtDecode.decode(localStorage.jwt);
   if(decoded.exp < Date.now()/1000) this.$router.push('/Login');
   this.user = decoded;
 },
 methods:{
    submit(){
      let data = {name:this.user.fullName,title:this.title,description:this.description}
      fetch("http://localhost:5000/api/create_comment",{
        method:'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'JWT ' + localStorage.jwt,
        },
        body: JSON.stringify(data),
        }
      )
      this.$router.push("/");
    }
  }
}
</script>
<style>
  input{
    margin:10px;
  }
</style>
