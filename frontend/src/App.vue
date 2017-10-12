<template>
  <div id="app">
    <img src="./assets/logo.png">
    <hello-api-server/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import HelloApiServer from './components/HelloApiServer'
export default {
  name: 'app',
  components: {
    HelloWorld,
    HelloApiServer
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
