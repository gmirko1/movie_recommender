<template>
      <HeaderComponent />
      
      <div class="profile-wrapper">
        <div class="profile-content">
            <h1>Your profile</h1>
            <div v-if="isLoading">Loading...</div> 

            <div v-else-if="userProfile" class="user-info-wrapper">
                <img class="user-image" :src="userImage" alt="Logo" />

                <p>{{ userData.user_email }}</p>

                <p>Profile created at:</p>
                <p>{{ userData.time_created }}</p>

                <hr>
            </div>
            
            <a href="/favourites">
            <div class="favourites-wrapper">
                <div class="favourites">
                <p class="favourites-p"> My favourites</p>
                </div>
            </div>
        </a>

        </div>


        
      </div>
      


      <FooterComponent />
  </template>



  

  <script>
    import userImage from '@/assets/user.png';
    import axios from 'axios';
  import HeaderComponent from './header-footer/HeaderComponent.vue';
  import FooterComponent from './header-footer/FooterComponent.vue';
  
  export default {
    components: {
      HeaderComponent, 
      FooterComponent,
    },
    data(){
        return {
            userData: null,
            userImage,
            isLoading: true
        }
    },
    methods:{
        async userProfile(){
            try {
        const response = await axios.get('/api/user-profile/')
       
        if (response.status === 200) {
            this.userData = response.data;
            } else {
                this.$router.push('/login');
            }
      } catch (error) {
        console.error('User profile failed', error.response ? error.response.data : error.message);
        this.$router.push('/login');
    }finally{
        this.isLoading = false;
      }
        }
    },

    mounted() {
    this.userProfile();
  }
    
}
    </script>


<style>



.profile-wrapper a{
    text-decoration: none;
    color: #000;
}

.favourites-p{
    font-size: 50px;
    text-align: center;
}



.favourites-wrapper{
    display: flex;
    align-items: center;
    justify-content: center;
}

.favourites{
    background-color: #D5DDF4;
    height: 200px;
    width: 400px;
    margin-top: 5%;
    border-radius: 20px;
}

.user-info-wrapper{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.profile-wrapper{
    display: flex;
    align-items: center;
    justify-content: center;
}

.profile-content{
    background-color: #B6C4EF;
    width: 600px;
    height: 700px;
    border-radius: 20px;
    padding: 20px;
    margin: 30px 0 30px 0;
}

.user-image{
    width: 100px;
    height: 100px;
}
</style>