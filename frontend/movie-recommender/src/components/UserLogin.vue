<template>
  <div class="login-wrapper">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      email: '',
      password: ''
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
