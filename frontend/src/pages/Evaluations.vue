<template>
  <div>
    <h1>Evaluations Page</h1>
    <evaluation-list :evaluations="evaluations"></evaluation-list>
  </div>
</template>

<script>
import EvaluationList from '../components/EvaluationList.vue';
import axios from 'axios';

export default {
  name: 'Evaluations',
  components: {
    EvaluationList
  },
  data() {
    return {
      evaluations: []
    }
  },
  mounted(){
    this.fetchEvaluations();
  },
  methods: {
    fetchEvaluations(){
      axios.get('/api/users/{user_id}/evaluations')
      .then(response =>{
        this.evaluations = response.data;
      })
      .catch(error => {
        console.error('Error fetching evaluations:', error);
      });
    }
  }
}
</script>
