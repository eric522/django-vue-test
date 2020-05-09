<template>
  <div>
    <i-navbar>
      <i-navbar-brand :to="{name:'Home'}">Testing Logo</i-navbar-brand>
      <i-navbar-items>
        <i-nav>
          <i-nav-item :to="{name:'Home'}">Home</i-nav-item>
          <i-nav-item :to="{name:'Movies'}">Movies</i-nav-item>
        </i-nav>
      </i-navbar-items>
    </i-navbar>
    <router-view></router-view>
  </div>
</template>

<style>
</style>
