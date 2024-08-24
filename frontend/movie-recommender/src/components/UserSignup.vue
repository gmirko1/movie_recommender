<template>
  <div class="login-signup-page">
    <img :src="logo" alt="Logo" />
    <form @submit.prevent="signup">
      <div>
        <input type="email" class="input-field" placeholder="Email" v-model="email" id="email" required>
      </div>
      <div>
        <input type="password"  class="input-field" placeholder="Password" v-model="password" id="password" required>
      </div>
      <div>
        <input type="password" class="input-field" placeholder="Confirm Password" v-model="confirmPassword" id="confirmPassword" required>
      </div>
      <button type="submit">Signup</button>

    </form>
    <a class="login-link" href="/login">Already have an account? Login</a>

  </div>
</template>

<script>

import logo from '@/assets/logo.png';

export default {
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      logo,
    };
  },
  methods: {
    signup() {
      if (this.password !== this.confirmPassword) {
        alert('Passwords do not match!');
        return;
      }
      console.log('Signing up with', this.email, this.password);
    }
  }
};
</script>

