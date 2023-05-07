<template>
    <div>
      <div ref="calendar"></div>
      <form @submit.prevent="addEvent">
        <input type="text" v-model="newEvent.title">
        <button type="submit">Add Event</button>
      </form>
    </div>
  </template>
  
  <script>
  import { Calendar } from '@fullcalendar/core';
  import dayGridPlugin from '@fullcalendar/daygrid';
  
  export default {
    data() {
      return {
        calendar: null,
        events: [], // array of event objects
        newEvent: {
          title: '',
          // other event properties
        },
      };
    },
    mounted() {
      this.calendar = new Calendar(this.$refs.calendar, {
        plugins: [ dayGridPlugin ],
        events: this.events,
        // other calendar options
      });
      this.calendar.render();
    },
    methods: {
      addEvent() {
        this.events.push(this.newEvent);
        this.newEvent = { title: '' }; // clear the form
        this.calendar.refetchEvents(); // update the calendar
      },
    },
  };
  </script>
  