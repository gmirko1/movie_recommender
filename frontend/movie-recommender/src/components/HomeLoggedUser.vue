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
  import axios from 'axios';

  
  export default {
    components: {
      HeaderComponent, 
      FooterComponent,
    },
    methods:
    {
        async handleHome() {
        try {
            const response = await axios.get('/api/home/');
            console.log(response)
            if (response.status === 200) {
                this.$router.push('/home');
            } else {
                this.$router.push('/login');
            }
        } catch (error) {
            console.error('Home error:', error);

            this.$router.push('/login');
        }
    }
    },
    mounted() {
    this.handleHome();
  }
  };

  </script>
