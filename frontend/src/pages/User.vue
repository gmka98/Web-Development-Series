<template>
  <div class="date-today">
    <span class="dash">DASHBOARD</span>
    <span>{{ currentDate }}</span>
  </div>
  <h4>LAST EVALUATION</h4>
  <div>
    <h1>{{user.name}}</h1>
    <p>Presence: {{user.presence}}</p>
    <user-presence-rate :presence="user.presence"></user-presence-rate>
  </div>
  <div class="course-event">
    <h4>NEXT COURSE</h4>

    <div class="exercice">
      <p>Level 3 - Collaboration</p>
      <span>Being a team player</span><span> -----> </span> <span>settings boundaries</span>
      <br>
      <span>Software</span><span> -----> </span> <span>Branching models</span>
      <br>
    </div>
    <h4>Event</h4>
    <div>
      <div class="to-know">
        <div>
          Gael   Internship follow-up
        </div>
        <div>09:30 AM - 10:00 AM</div>
      </div>
      <div class="to-know">
        <div>
          Next Event
        </div>
        <div>{{ nextEvent }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import UserPresenceRate from '../components/UserPresenceRate.vue';
import axios from 'axios'
import Calendar from './Calendar.vue'

export default defineComponent({
  name: 'User',
  components: {
    UserPresenceRate,
    Calendar
  },
  data() {
    return {
      user: {
      name: 'Gael Mukendi Kabongo',
      presence: 100,
      activeParticipation: null,
      behavior: null,
      acquisition: null,
      comments: null
    },
      evaluations: [],
      currentDate: '',
      lastEvaluation: null
    };
  },
  props: {
    nextEvent: {
      type: String,
      required: true
    }
  },
  mounted() {
  // Get the current date and time
  const now = new Date();

  // Define an array of weekday names
  const weekdayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

  // Extract the day of the week from the current date
  const dayOfWeekIndex = now.getDay();

  // Get the name of the day of the week
  const dayOfWeekName = weekdayNames[dayOfWeekIndex];

  // Extract the day, month, and year from the current date
  const day = now.getDate();
  const month = now.toLocaleString('default', { month: 'long' });
  const year = now.getFullYear();

  // Get the user's location
  axios.get('https://ipapi.co/json/')
    .then(response => {
      // Extract the user's timezone from the response
      const timezone = response.data.timezone;

      // Set the formatted date string based on the user's timezone
      const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        timeZone: timezone,
        timeZoneName: 'short'
      };
      this.currentDate = now.toLocaleDateString(undefined, options).replace(',', '');
    })
    .catch(error => {
      console.log(error);
      // Set the formatted date string using the default format
      this.currentDate = `${dayOfWeekName} ${day} ${month} ${year}`;
    });

  // Fetch last evaluation data
  axios.get('http://localhost:8000/last_evaluation')
    .then(response => {
      // Update user object with evaluation data
      this.user.activeParticipation = response.data.activeParticipation;
      this.user.behavior = response.data.behavior;
      this.user.acquisition = response.data.acquisition;
      this.user.comments = response.data.comments;
    })
    .catch(error => {
      console.log(error);
    });
}
});
</script>
