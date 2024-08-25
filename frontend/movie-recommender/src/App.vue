<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>


/*  NAVIGATION */
.header {
  position: sticky; 
  top: 0; 
  background-color: white; 
  border-bottom: 1px solid #ddd; 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  padding: 10px 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
  z-index: 1000; 
}

.logout-btn {
  background-color: #B6C4EF;
  border: none; 
  color: black; 
  padding: 8px 16px;
  font-size: 16px; 
  border-radius: 4px; 
  cursor: pointer; 
  transition: background-color 0.3s ease; 
}

.logout-btn:hover {
  background-color: #B6C4EF; 
}
.nav{
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav a:hover {
  color: #B6C4EF;
}

.nav a {
  text-decoration: none; 
  color: #333;
  font-size: 16px; 
  font-weight: 500;
  transition: color 0.3s ease; 
}

.nav-logo{
  width: 100px;
  height: 50px;
}

/*  FOOTER */
.footer {
  background-color: #f8f9fa; 
  color: #6c757d;
  text-align: center; 
  padding: 20px; 
  border-top: 1px solid #dee2e6; 
  position: relative; 
  bottom: 0; 
  width: 100%; 
  font-size: 14px; 
  box-shadow: 0 -2px 4px rgba(0, 0, 0, 0.1); 
}




/*  LOGIN AND SIGNUP */
.login-link{
  color: #000;
  margin-top: 30px;
}

.input-field{
  font-size: 20px;
  padding-left: 20px;
}

.login-signup-page {
  height: 100vh; 
  background-size: cover; 
  background-position: center; 
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url('@/assets/login-bg.png');
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.login-signup-page input{
  border-radius: 10px;
  border: 1px solid #000;
  background-color: #B6C4EF ;
  height: 45px;
  width: 300px;
  margin-top: 6%;
}

.login-signup-page input::placeholder {
  color: #000;
  opacity: 1;
  font-size: 20px;
}



.login-signup-page button{
  background-color: #000;
  border-radius: 10px;
  color: #B6C4EF;
  font-size: 20px;
  width: 310px;
  height: 45px;
  margin-top: 8%;
  text-transform: uppercase;
  border: 2px solid 000;
  cursor: pointer;
}

.login-signup-page button:hover{
  background-color:#B6C4EF ;
  color: #000;
}


.like-button{
  cursor: pointer;
}


</style>
