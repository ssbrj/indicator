<template>
  <div id="app">
    <div>
      <vue-headful
        title="Indicator"
        description="=Indicator"
        />
    </div>
    <NavBar></NavBar>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  components: {
    NavBar,
    Footer
  }
}
</script>
