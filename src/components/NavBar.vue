<template>
  <b-navbar class="has-shadow has-text-weight-bold" id="navbar-border-top" fixed-top>
    <template slot="brand">
      <b-navbar-item href="/">
        <img
          src="static/indicator-logo.png"
          alt="x"
        >
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item id="navbar-search">
        <b-field>
          <b-input style="width: 35em;"
            type="search"
            icon="magnify">
          </b-input>
        </b-field>
      </b-navbar-item>
    </template>
    <template slot="end">
      <b-navbar-item href="#">
        Indicators
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
}
</script>
