<template>

      <HeaderComponent />
      <div class="media-wrapper">
      <h1>Media Library</h1>

        <div class="movie-wrapper">
          <h2>Movies</h2>
          <MovieComponent />
        </div>

        <div class="tvshow-wrapper">
          <h2>Tv show</h2>
          <TvShowsComponent />

        </div>

        <div class="book-wrapper">
          <h2>Books </h2>
          <BooksComponent />

        </div>

       </div>
      <FooterComponent />

  </template>
  

  <script>
  import HeaderComponent from './header-footer/HeaderComponent.vue';
  import FooterComponent from './header-footer/FooterComponent.vue';
  import MovieComponent from './media-library/MovieComponent.vue';
  import TvShowsComponent from './media-library/TvShowsComponent.vue';
  import BooksComponent from './media-library/BooksComponent.vue';

  export default {
    components: {
      HeaderComponent, 
      FooterComponent,
      MovieComponent,
      TvShowsComponent,
      BooksComponent,
    }
}
    </script>

