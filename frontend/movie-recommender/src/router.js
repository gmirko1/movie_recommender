import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from './components/UserLogin.vue';
import UserSignup from './components/UserSignup.vue';
import HomeLoggedUser from './components/HomeLoggedUser.vue'
import UserProfile from './components/UserProfile.vue';
import UserFavourites from './components/UserFavourites.vue';
import MovieList from './components/MovieList.vue';

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
      path: '/home',
      name: 'HomeLoggedUser',
      component: HomeLoggedUser
    },
    {
      path: '/profile',
      name: 'UserProfile',
      component: UserProfile
    },
    {
      path: '/favourites',
      name: 'UserFavourites',
      component: UserFavourites
    },
    {
      path: '/movies',
      name: 'MovieList',
      component: MovieList
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