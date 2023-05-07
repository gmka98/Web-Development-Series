<template>
  <div>
    <h1>Evaluations Page</h1>
    <evaluation-list :evaluations="evaluations"></evaluation-list>
  </div>
</template>

<script>
import EvaluationList from '../components/EvaluationList.vue';

export default {
  name: 'Evaluations',
  components: {
    EvaluationList
  },
  data() {
    return {
      evaluations: [
        {
          date: '2023-04-01',
          activeParticipation: 'Yes',
          behavior: 'Good',
          acquisition: 'Yes',
          comments: 'Keep up the good work!'
        },
        {
          date: '2023-04-15',
          activeParticipation: 'Yes',
          behavior: 'Neutral',
          acquisition: 'Partial',
          comments: 'Work on improving your knowledge acquisition'
        },
        // Add more evaluations as needed
      ]
    }
  }
}
</script>
