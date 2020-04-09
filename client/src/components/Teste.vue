<template>
  <div>
    <button type="button" class="submit">{{ msg }}</button>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Teste',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage(){
      const path = 'http://localhost:5000/api/v1';
      axios.get(path)
        .then((res) => {
            this.msg = res.data;
    })
    .catch((error) => {
          console.error(error);
    });
    },
  created() {
    this.getMessage();
  },
},
}
</script>