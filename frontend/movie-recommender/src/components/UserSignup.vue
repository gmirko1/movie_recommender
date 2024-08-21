<template>
  <div class="signup-wrapper">
    <h1>Signup</h1>
    <form @submit.prevent="signup">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" required>
      </div>
      <div>
        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" v-model="confirmPassword" id="confirmPassword" required>
      </div>
      <button type="submit">Signup</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: ''
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

