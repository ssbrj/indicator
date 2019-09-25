<template>
  <footer class="footer">
    <div class="content has-text-centered">
      <p>
        <span class="has-text-weight-bold">Indicator</span> by <a href="https://sbrj.org" class="has-text-weight-bold">Sean Sobieraj</a>. The source code is licensed
        <a href="http://opensource.org/licenses/mit-license.php" class="has-text-weight-bold">MIT</a>. The website content
        is licensed <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" class="has-text-weight-bold">CC BY NC SA 4.0</a>.
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  props: {
    msg: String
  }
}
</script>
