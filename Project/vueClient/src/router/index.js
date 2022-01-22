import VueJwtDecode from "vue-jwt-decode";
import { createRouter, createWebHistory } from 'vue-router'
import AddComment from '../components/AddComment.vue'
import CommentList from '../components/CommentList.vue'
import NotFound from '../components/NotFound.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Admin from '../components/Admin.vue'

const routes = [
  {
    path: '/',
    name: 'CommentList',
    component: CommentList,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: '/AddComment',
    name: 'Add',
    component: AddComment,
    meta: {
      requiresAuth: true,
    }
  },
  {
    path :'/Login',
    name: 'Login',
    component: Login,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path :'/Register',
    name: 'Register',
    component: Register,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: '/:catchAll(.*)*',
    name: 'NotFound',
    component: NotFound,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: '/Admin',
    name: 'Admin',
    component: Admin,
    meta: {
      requiresAdmin: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

function isAuthenticated(){
  return localStorage.jwt != undefined ? true : false;
}

function isAdmin(){
  if(localStorage.jwt == undefined) return false;
  let decoded = VueJwtDecode.decode(localStorage.getItem('jwt'));
  if(decoded.exp < Date.now()/1000) return false;
  let user = decoded;
  if (user.fullName == "Admin" && user.email == "admin@test.com") return true;
  return false
}

router.beforeEach((to, from, next) =>{
  if (to.matched.some((record) => record.meta.requiresAuth)){
    if(isAuthenticated()){
      next();
      return;
    }
    next('/Login');
    return;
  } else if (to.matched.some((record) => record.meta.requiresAdmin)){
    if(isAdmin()){
      next();
      return;
    }
    next('/Login');
    return;
  }
  next();
})

export default router
