<template>

      <HeaderComponent />
      <div class="home-wrapper">
      <h1>Find your next movie, book or tv show</h1>

      <div class="recommendor-wrapper">
        <form @submit.prevent="submitForm">
          <div class="dropdown-wrapper">
            <label for="genre">Choose a Genre:</label>
            <select v-model="genre" id="genre" class="dropdown" required>
              <option value="" disabled>Select a genre</option>
              <option v-for="genre in genres" :key="genre" :value="genre">{{ genre }}</option>
            </select>
          </div>
          
          <div class="dropdown-wrapper">
            <label for="media_type">Choose a Media Type:</label>
            <select v-model="media_type" id="media_type" class="dropdown"  required>
              <option value="" disabled>Select media type</option>
              <option value="movie">Movie</option>
              <option value="tv_show">TV Show</option>
              <option value="book">Book</option>
            </select>
          </div>
          
          <button type="submit" @click="getRecommendation()">Get Recommendation</button>
        </form>

        <div class="recommendation-wrapper" v-if="recommendationData">
          <h2>Recommendation:</h2>

          <div v-if="isLoading">Loading...</div> 
          <div v-else-if="recommendationData" class="recommendationInfo">
              <div class="recommendation-card">
                <img class="recommendation-image" :src="mediaImage" alt="recommendation" />
                <p><b>{{ recommendationData.Genre }}</b></p>
                <p>{{ recommendationData.Name  }}</p>
                <p>{{ recommendationData.Year }}</p>

          </div>
      </div>
        </div>
      </div>

      <div class="media-library">
          <p>Check our media library for inspiration</p>
          <a href="/media-library"><button>Media library</button></a>
      </div>
    </div>
      <FooterComponent />

  </template>
  
  <script>
  import HeaderComponent from './header-footer/HeaderComponent.vue';
  import FooterComponent from './header-footer/FooterComponent.vue';
  import axios from 'axios';
  import mediaImage from '@/assets/media.jpeg';
  
  export default {
    components: {
      HeaderComponent, 
      FooterComponent,
    },
    data(){
      return {
      genre: '',
      media_type: '',
      genres: ['drama', 'crime', 'action', 'science fiction', 'fantasy', 'comedy'],
      recommendationData: [],
      mediaImage
      };
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
    },
    async getRecommendation(){
      try {
      const response = await axios.post('/api/recommendation/', {
        genre: this.genre, 
        type:this.media_type
      })
      this.recommendationData = response.data;


    } catch (error) {
      console.error('Recommendation failed', error.response ? error.response.data : error.message);
      this.$router.push('/login');
  }finally{
      this.isLoading = false;
    }
    }

    },
    mounted() {
    this.handleHome();
  }
  };

  </script>


<style>

.recommendation-wrapper{
  margin-top: 30px;
}

.dropdown-wrapper{
  display:flex;
  flex-direction: column;
}

.dropdown-wrapper label{
  font-size: 18px;
  font-weight: 800;
  margin-top: 20px;
}

.recommendor-wrapper{
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #d8def2;
  border-radius: 20px;
  padding: 20px;
}

.dropdown{
  font-size: 20px;
  padding: 8px;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
  color: #333;
  width: 100%;
  max-width: 300px;
  outline: none;
  cursor: pointer;
  margin-top: 10px;

}

.recommendationInfo{
  background-color:#B6C4EF ;
  width: 300px;
  height: 400px;
  padding: 20px;
  display:flex;
  justify-content: center;
  border-radius: 20px;
}

.media-library{
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color:#000000 ;
  height: 300px;
  color: white;
}

.media-library p{
  font-size: 40px;
}

.media-library button{
  width: 200px;
  height: 50px;
  border-radius: 30px;
  font-size: 20px;
  border: 2px solid white;
  cursor: pointer;
}

.media-library button:hover{
  background-color:#000000 ;
  color: white;
}


</style>