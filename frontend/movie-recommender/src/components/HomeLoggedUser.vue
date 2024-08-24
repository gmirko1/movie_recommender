<template>
    <div class="home-wrapper">
      <HeaderComponent />
      <h1>Home</h1>
      <FooterComponent />
    </div>
  </template>
  
  <script>
  import HeaderComponent from './header-footer/HeaderComponent.vue';
  import FooterComponent from './header-footer/FooterComponent.vue';
  
  export default {
    components: {
      HeaderComponent, 
      FooterComponent,
    },
    methods:
    {
      async handleHome() {
        try {
          const response = await fetch('/api/home', { method: 'GET' });
          if (response.ok) {
            this.$router.push('/home'); 
          } else {
            console.error('Home failed');
          }
        } catch (error) {
          console.error('Home error:', error);
        }
      }
    }
  };

  </script>
