<template>
  <h1>Admin</h1>
  <div class="Total">
    <div class="Users">
      Users {{juniorCount + mediorCount + seniorCount}}
    </div>
    <div class="Junior">
      Junior {{ juniorCount }}
    </div>
    <div class="Medior">
      Medior {{ mediorCount }}
    </div>
    <div class="Senior">
      Senior {{ seniorCount }}
    </div>
  </div>
  <div>Classes</div>
  <div>Course</div>
  <div>Event</div>
  <div class="Meet">Meet</div>
  <div class="Task">Task list</div>
  <div class="guest">guest</div>
</template>
<style>
.Total{

}
</style>

<script>
import axios from 'axios';

export default {
  name: 'Admin',
  data() {
    return {
      juniorCount: 15,
      mediorCount: 10,
      seniorCount: 30,
    };
  },
  mounted() {
    this.fetchUserCounts();
  },
  methods: {
    fetchUserCounts() {
      axios.get('/api/users')  // Replace '/api/users' with your actual API endpoint
        .then(response => {
          const { junior, medior, senior } = response.data;
          this.juniorCount = junior;
          this.mediorCount = medior;
          this.seniorCount = senior;
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>
