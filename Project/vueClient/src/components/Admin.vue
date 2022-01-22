<template>
 <div>
   <input v-model="searched" type="text" placeholder="Search"/>
   <button @click="getComments">Search</button>
   <Comment class="comment" v-for="(comment,index) in list" :key="index" :data="comment" @update="getComments"/>
 </div>
</template>

<script>
import Comment from './Comment'
export default {
  name: 'Admin',
  data(){
    return {
      list:[],
      searched:'',
      jwt:''
    }
  },
  components:{Comment},
  created(){
    this.getComments();
  },
  methods:{
    getComments(){
      if(this.searched != ''){
        this.search();
      }
      else{
        fetch("http://localhost:5000/api/comments")
          .then(response => response.json())
          .then(data => {this.list = data.reverse()});
      }
    },
    search(){
      fetch("http://localhost:5000/api/comments_by_name?name="+this.searched)
      .then(response => response.json())
      .then(data => {this.list = data});
    }
  }
}
</script>
