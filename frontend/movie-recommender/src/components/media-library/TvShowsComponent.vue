<template>
    
    <div class="tvshows-wrapper">
      <div class="tvshows-content">
          <div v-if="isLoading">Loading...</div> 

          <div v-else-if="tvShowsData" class="tvshowsInfo">
            <div v-for="tvShow in tvShowsData" :key="tvShow[0]" class="tvshow-item">
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
  </div>
    


</template>



<script>
  import tvShowImage from '@/assets/tvshow.jpeg';
  import axios from 'axios';

export default {

  data(){
      return {
        tvShowsData: [],
        tvShowImage,
          isLoading: true
      }
  },
  methods:{
      async tvShowsDataGet(){
          try {
      const response = await axios.get('/api/tv-shows/')
      console.log("tv shows", response)
      this.tvShowsData = response.data;



    } catch (error) {
      console.error('Movie failed', error.response ? error.response.data : error.message);
      this.$router.push('/login');
  }finally{
      this.isLoading = false;
    }
      },
      async likeTvShow(tvShowID){
        try {
          await axios.post('/api/like-tvshow/', {tvShowID});

      } catch (error) {
        console.error('Like tv show failed', error.response ? error.response.data : error.message);
      }
      }
  },

  mounted() {
  this.tvShowsDataGet();
}
  
}
  </script>


<style>



.tvshowsInfo{
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.tvshow-card{
  background-color: white;
  border-radius: 20px;
  padding: 20px;
}

</style>