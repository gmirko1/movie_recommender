<template>
    
    <div class="book-wrapper">
      <div class="book-content">
          <div v-if="isLoading">Loading...</div> 

          <div v-else-if="booksData" class="booksInfo">
            <div v-for="book in booksData" :key="book[0]" class="book-item">
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
    


</template>



<script>
  import bookImage from '@/assets/book.jpeg';
  import axios from 'axios';

export default {

  data(){
      return {
        booksData: [],
        bookImage,
          isLoading: true
      }
  },
  methods:{
      async bookData(){
          try {
      const response = await axios.get('/api/books/')
      this.booksData = response.data;


    } catch (error) {
      console.error('Movie failed', error.response ? error.response.data : error.message);
      this.$router.push('/login');
  }finally{
      this.isLoading = false;
    }
      },
      async likeBook(bookID){
        try {
          await axios.post('/api/like-book/', {bookID});

      } catch (error) {
        console.error('Like book failed', error.response ? error.response.data : error.message);
      }
      }
  },

  mounted() {
  this.bookData();
}
  
}
  </script>


<style>
.booksInfo{
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.book-card{
  background-color: white;
  border-radius: 20px;
  padding: 20px;
}

</style>