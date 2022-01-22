<template>
  <div id="nav">
    <router-link to="/">Comments</router-link> |
    <div v-if="!token">
      <router-link to="/Login">Login</router-link> |
      <router-link to="/Register">Register</router-link>
    </div>
    <div v-else>
      <router-link v-if="user.fullName != 'Admin'" to="/AddComment">Add Comment</router-link>
      <router-link v-else to="/Admin">Admin vue</router-link>
      {{user.fullName}} |
      <button @click="logout">Log Out</button>
    </div>
  </div>
  <router-view/>
</template>


<script>
import VueJwtDecode from "vue-jwt-decode";
export default{
  name:'NavBar',
  data(){
    return {
      user:{},
      token:''
    }
  },
  mounted(){
    this.getToken();
    this.emitter.on("token_update", ()=>{
      this.getToken();
    });
  },
  methods:{
    getToken(){
      let token = localStorage.getItem('jwt');
      if(token){
        this.getUser();
        this.token = token;
      }
      else this.token = '';
    },
    logout(){
      localStorage.removeItem('jwt');
      this.getToken()
    },
    getUser(){
      let decoded = VueJwtDecode.decode(localStorage.getItem('jwt'));
      if(decoded.exp < Date.now()/1000) this.$router.push('/Login');
      this.user = decoded;
    }
  }
}


</script>
