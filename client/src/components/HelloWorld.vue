<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex>
        <!-- Main form --><form>
          <v-text-field
            v-model="sepalWidth"
            label="Initial Date"
            required
          ></v-text-field>
          <v-text-field
            v-model="sepalLength"
            label="Current Date"
            required
          ></v-text-field>
          <v-text-field
            v-model="petalWidth"
            label="CDB Rate"
            required
          ></v-text-field><v-btn @click="submit">submit</v-btn>
          <v-btn @click="clear">clear</v-btn>
        </form><br/>
        <br/><h1 v-if="predictedClass">Predicted Class is: {{ predictedClass }}</h1><!-- END: IMPORTANT PART! -->
      </v-flex>
    </v-layout>
  </v-container>

</template>

<script>
  import axios from 'axios'
  export default {
    name: 'HelloWorld',
    data: () => ({
      sepalLength: '',
      sepalWidth: '',
      petalLength: '',
      petalWidth: '',
      predictedClass : ''
    }),
    methods: {
    submit () {
      axios.get('http://127.0.0.1:5000/', {
        sepal_length: this.sepalLength,
        sepal_width: this.sepalWidth,
        petal_length: this.petalLength,
        petal_width: this.petalWidth
      })
      .then((response) => {
        this.predictedClass = response.data.class
      }).catch(error => console.log(error))
    },
    clear () {
      this.sepalLength = ''
      this.sepalWidth = ''
      this.petalLength = ''
      this.petalWidth = ''
    }
  }
}
</script>