<template>
    <div class="home-wrapper">
      <HeaderComponent />
      <h1>Profile</h1>
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
    }
}
    </script>