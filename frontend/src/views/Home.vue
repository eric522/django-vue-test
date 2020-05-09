<template>
  <div>
    <i-container>
      <h1 class="_text-center">
        Hello World
      </h1>
      <p class="_text-center">
        <img src="../assets/logo.png" class="image -responsive" alt="Vue Logo">
      </p>
      <p class="_text-center">
        <i-button outline variant="primary" :to="{name:'Movies'}">Visit</i-button>
      </p>
    </i-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
}
</script>
