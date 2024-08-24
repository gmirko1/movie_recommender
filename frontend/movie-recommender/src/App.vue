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


</style>
