<template>
  <div class="login-signup-page">
    <img :src="logo" alt="Logo" />
    <form @submit.prevent="login">
      <div>
        <input type="email" class="input-field" placeholder="Email" v-model="email" id="email" required>
      </div>
      <div>
        <input type="password" class="input-field" placeholder="Password" v-model="password" id="password" required>
      </div>
      <button type="submit">Login</button>
    </form>

    <a class="login-link" href="/signup">If you do not have an account, signup here!</a>
  </div>
</template>

<script>
import logo from '@/assets/logo.png';
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      logo
    };
  },
  methods: {
    async login() { 
      try {
        const response = await axios.post('/api/login/', {
          email: this.email,
          password: this.password
        });
        console.log('Login successful', response.data);
        this.$router.push('/home');
      } catch (error) {
        console.error('Login failed', error.response ? error.response.data : error.message);
      }
    }
  }
};
</script>
