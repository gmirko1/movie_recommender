<template>
    
    <div class="movie-wrapper">
      <div class="movie-content">
          <div v-if="isLoading">Loading...</div> 

          <div v-else-if="moviesData" class="moviesInfo">
            <div v-for="movie in moviesData" :key="movie[0]" class="movie-item">
              <div class="movie-card">
                <img class="movie-image" :src="movieImage" alt="movie" />
                <p><b>{{ movie[1] }}</b></p>
                <p>{{ movie[3] }}</p>
                <p>{{ movie[2] }}</p>
                <button class="like-button" @click="likeMovie(movie[0])">❤️</button>

            </div>
          </div>
          


      </div>


      
    </div>
  </div>
    


</template>



<script>
  import movieImage from '@/assets/movie.jpeg';
  import axios from 'axios';

export default {

  data(){
      return {
            moviesData: [],
            movieImage,
          isLoading: true
      }
  },
  methods:{
      async movieData(){
          try {
      const response = await axios.get('/api/movies/')
      console.log(response)
      this.moviesData = response.data;


    } catch (error) {
      console.error('Movie failed', error.response ? error.response.data : error.message);
      this.$router.push('/login');
  }finally{
      this.isLoading = false;
    }
      },
      async likeMovie(movieID){
        try {
          await axios.post('/api/like-movie/', {movieID});

      } catch (error) {
        console.error('Like movie failed', error.response ? error.response.data : error.message);
      }
      }
  },

  mounted() {
  this.movieData();
}
  
}
  </script>


