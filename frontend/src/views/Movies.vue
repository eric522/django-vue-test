<template>
  <div>
    <i-container>
      <h1>Movies</h1>
      <i-row>
        <i-column v-for="movie in movies" :key="movie.id">
          <i-card>
            <img slot="image" :src="movie.poster" alt="Card Image" />
            <i-button :to="{name:'Detail', params:{'id':movie.id}}" block>Ver</i-button>
          </i-card>
        </i-column>
      </i-row>
    </i-container>
  </div>
</template>
 
<script>
import axios from "axios";

export default {
  name: "Movies",
  data() {
    return {
      movies: []
    };
  },
  methods: {
    getMovies() {
      axios
        .get("http://localhost:8000/api/movies")
        .then(resp => {
          this.movies = resp.data;
        })
        .catch(err => console.log(err));
    }
  },
  mounted() {
    this.getMovies();
  }
};
</script>