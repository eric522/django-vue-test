<template>
  <div>
    <i-container v-if="!isLoading">
        <i-row>
            <i-column>
                <img :src="movie.poster" class="image -polaroid" alt="Polaroid">
            </i-column>
            <i-column>
              <h1>{{movie.title}}</h1>
              <h5>Release Date</h5>
              <p>
                {{movie.release_date}}
              </p>
              <h5>Sinopsis:</h5>
              <p>
                {{movie.overview}}
              </p>
              <i-button-group>
                <i-button v-for="tag in movie.tags" :key="tag.id">
                  {{tag.name}}
                </i-button>
              </i-button-group>
            </i-column>
        </i-row>
    </i-container>
    <i-container v-if="isLoading">
        <i-row center middle>
            <i-column>
                <i-loader size="lg" variant="dark"></i-loader>
            </i-column>
        </i-row>
    </i-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Detail",
  data() {
    return {
      movie: {},
      isLoading:true,
    };
  },
  methods: {
    getMovie() {
      var paramId = this.$route.params.id;
      axios.get(`http://localhost:8000/api/movies/${paramId}`).then(resp => {
        this.movie = resp.data
      })
      .catch(err => console.log(err))
      .finally(() => this.isLoading= false)
    }
  },
  mounted() {
    setTimeout(this.getMovie,3000)
  }
};
</script>

<style>
</style>