<template>
2 accounts : a@test.com test
            admin@test.com admin


Email : <input v-model="email" type="email">
Password : <input v-model="password" type="password">
<button @click="login">Login</button>

</template>
<script>

export default {
  name: 'Login',
  data(){
    return {
      email:'',
      password:''
    }
  },
  methods:{
    login(){
      fetch("http://localhost:5000/auth/login",{
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email:this.email, password:this.password})
      })
      .then(response => response.json())
      .then(data => {
        if(data.token){
          localStorage.setItem('jwt', data.token);
          this.emitter.emit("token_update")
          this.$router.push("/");
        }
        else{
          alert(data.message);
        }
      });
    }
  }
}
</script>
