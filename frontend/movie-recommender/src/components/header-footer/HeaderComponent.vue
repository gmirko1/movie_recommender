<template>
    <header class="header">
      <div class="logo">
        <router-link to="/home">Home</router-link>
      </div>
      <nav class="nav">
        <router-link to="/movie">Movies</router-link>
        <router-link to="/favourites">Favourites</router-link>
        <router-link to="/profile">Profile</router-link>
        <button @click="handleLogout" class="logout-btn">Logout</button>
      </nav>
      <div class="user-info">
        Welcome!
      </div>
    </header>
  </template>
  
  <script>
  export default {
    methods: {
      async handleLogout() {
        try {
          const response = await fetch('/api/logout', { method: 'POST' });
          if (response.ok) {
            this.$router.push('/login'); 
          } else {
            console.error('Logout failed');
          }
        } catch (error) {
          console.error('Logout error:', error);
        }
      }
    }
  };
  </script>