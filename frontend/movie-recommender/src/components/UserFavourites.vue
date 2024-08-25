<template>

      <HeaderComponent />

      <h1>Your favourites</h1>
      <div class="your-favourites">
      <div class="movie-wrapper">
        <h2>Movies</h2>
        <div v-if="isLoading">Loading...</div> 

        <div v-else-if="likedMovies" class="moviesInfo">
          <div v-for="movie in likedMovies" :key="movie[0]" class="movie-item">
            <div class="movie-card">
              <img class="movie-image" :src="movieImage" alt="movie" />
              <p><b>{{ movie[1] }}</b></p>
              <p>{{ movie[3] }}</p>
              <p>{{ movie[2] }}</p>
              <button class="like-button" @click="dislikeMovie(movie[0])">❤️</button>

          </div>
        </div>
    </div>
          
      </div>

      <div class="tvshow-wrapper">
        <h2>Tv shows</h2>
        <div v-if="isLoading">Loading...</div> 
        <div v-else-if="likedTvShows" class="tvshowsInfo">
          <div v-for="tvShow in likedTvShows" :key="tvShow[0]" class="tvshow-item">
            <div class="tvshow-card">
              <img class="tvshow-image" :src="tvShowImage" alt="tvshow" />
              <p><b>{{ tvShow[1] }}</b></p>
              <p>{{ tvShow[3] }}</p>
              <p>{{ tvShow[2] }}</p>
              <button type="submit" class="like-button" @click="likeTvShow(tvShow[0])">❤️</button>

          </div>
        </div>
    </div>



      </div>

      <div class="book-wrapper">
        <h2>Books </h2>
        <div v-if="isLoading">Loading...</div> 
        <div v-else-if="likedBooks" class="booksInfo">
          <div v-for="book in likedBooks" :key="book[0]" class="book-item">
            <div class="book-card">
              <img class="book-image" :src="bookImage" alt="book" />
              <p><b>{{ book[1] }}</b></p>
              <p>{{ book[3] }}</p>
              <p>{{ book[2] }}</p>
              <button class="like-button"  @click="likeBook(book[0])">❤️</button>

          </div>
        </div>

    </div>


      </div>

    
      </div>
      <FooterComponent />

  </template>
  

  <script>
    import axios from 'axios';
    import movieImage from '@/assets/movie.jpeg';
    import tvShowImage from '@/assets/tvshow.jpeg';
    import bookImage from '@/assets/book.jpeg';

  import HeaderComponent from './header-footer/HeaderComponent.vue';
  import FooterComponent from './header-footer/FooterComponent.vue';
  
  export default {
    components: {
      HeaderComponent, 
      FooterComponent,

    },
    data(){
      return {
        likedMovies: [],
          movieImage,
          isLoading: true,
          likedTvShows: [],
          tvShowImage,
          bookImage
      }
  },

    methods:{
      async getLikesMovies(){
        try {
        const response = await axios.get('/api/likes-movies/')
       
        if (response.status === 200) {
            this.likedMovies = response.data;
            
            } else {
                this.$router.push('/login');
            }
      } catch (error) {
        console.error('Get likes movies failed', error.response ? error.response.data : error.message);
        this.$router.push('/login');
    }finally{
        this.isLoading = false;
      }
      },
      async getLikesTvShows(){
        try {
        const response = await axios.get('/api/likes-tvshows/')
       
        if (response.status === 200) {
            this.likedTvShows = response.data;
            
            } else {
                this.$router.push('/login');
            }
      } catch (error) {
        console.error('Get likes tvshows failed', error.response ? error.response.data : error.message);
        this.$router.push('/login');
    }finally{
        this.isLoading = false;
      }
      },
      async getLikesBooks(){
        try {
        const response = await axios.get('/api/likes-books/')
       
        if (response.status === 200) {
            this.likedBooks = response.data;
            
            } else {
                this.$router.push('/login');
            }
      } catch (error) {
        console.error('Get likes books failed', error.response ? error.response.data : error.message);
        this.$router.push('/login');
    }finally{
        this.isLoading = false;
      }
      }
    }, 
    mounted() {
    this.getLikesMovies();
    this.getLikesTvShows();
    this.getLikesBooks();
  }
}
    </script>

<style>
.your-favourites{
  display:flex;
  flex-direction: column;
}
</style>
