import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from './components/UserLogin.vue';
import UserSignup from './components/UserSignup.vue';


const routes = [
    {
      path: '/login',
      name: 'UserLogin',
      component: UserLogin
    },
    {
      path: '/signup',
      name: 'UserSignup',
      component: UserSignup
    },
    {
        path: '/:catchAll(.*)', 
      redirect: '/login'
    }
  ];


// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;