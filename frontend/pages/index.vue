<template>
  <div>
    {{ message}}
    <ul>
      <li v-for="cv in data" :key='cv.id'>
        {{ cv}}
      </li>
    </ul>
  </div>
</template>

<script>
const axios = require('axios').default;
export default {
  data() {
    return {
      message: 'Hello world',
      data: []
    }
  },
  mounted() {
    this.startInterval();
  },
  methods: {
    startInterval() {
       setInterval(() => {
        this.message ='Goodby'
      }, 2000);
    },
    getData(format) {
      let obj_list = axios.get(`http://localhost:8000/`)
      .then((response) => {
         console.log(response);
        this.data = obj_list;

      })
    }
  }
}
</script>
