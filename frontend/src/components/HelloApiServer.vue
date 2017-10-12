<template>
  <div class="hello-api-server">
    <h1>{{ msg }}</h1>

  </div>
</template>

<script>
import {HTTP} from '../js/http-common';

export default {
  name: 'HelloApiServer',
  data () {
    return {
      msg: ''
    }
  },

  created() {
      HTTP.get('helloworld')
      .then(response => {
        this.msg = response.data;
      })
      .catch(e => {
        this.msg = e.message;
      })
    }
}
</script>
