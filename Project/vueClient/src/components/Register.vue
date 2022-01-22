<template>

Name : <input v-model="name" type ="text"/>
Email : <input v-model="email" type="email"/>
Password : <input v-model="password" type="password"/>
<button @click="register">Regitser</button>

</template>
<script>

export default {
  name: 'Register',
  data(){
    return {
      name:'',
      email:'',
      password:''
    }
  },
  methods:{
    register(){
      fetch("http://localhost:5000/auth/register",{
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email:this.email, password:this.password, fullName:this.name})
      })
    }
  }
}
</script>
