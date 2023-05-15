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
import axios from 'axios';

export default {
  data() {
    return {
      calendar: null,
      events: [], // array of event objects
      newEvent: {
        title: '',
        start: '2023-05-25T19:00:00',
        end: '2023-05-25T23:00:00',
        // other event properties
      },
    };
  },
  mounted() {
    this.calendar = new Calendar(this.$refs.calendar, {
      plugins: [ dayGridPlugin ],
      events: this.events,
      editable: true,
      selectable: true,
      // other calendar options
    });
    this.calendar.on('dateClick', this.handleDateClick);
    this.calendar.render();
  },
  methods: {
    addEvent() {
      this.events.push(this.newEvent);
      this.newEvent = { title: '' }; // clear the form
      this.calendar.refetchEvents(); // update the calendar
      this.calendar.renderEvent(this.newEvent); // render the new event on the calendar
    },
    handleDateClick(info){
      const newEvent = {
        title: 'New Event',
        start: info.dateStr,
        end: info.dateStr,
      };
      this.calendar.addEvent(newEvent);
    }
  },
};
</script>
