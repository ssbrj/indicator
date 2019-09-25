<template>
  <b-navbar class="has-shadow has-text-weight-bold" fixed-top>
    <template slot="brand">
      <b-navbar-item href="/">
        <img
          src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
          alt="Lightweight UI components for Vue.js based on Bulma"
        >
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item>
        <b-field>
          <b-input style="width: 30em;"
            type="search"
            icon="magnify">
          </b-input>
        </b-field>
      </b-navbar-item>
    </template>
    <template slot="end">
      <b-navbar-item href="#">
        Home
      </b-navbar-item>
      <b-navbar-item href="#">
        About
      </b-navbar-item>
      <b-navbar-item href="#">
        Log in
      </b-navbar-item>
      <b-navbar-item href="#">
        Sign up
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    msg: String
  }
};
</script>
