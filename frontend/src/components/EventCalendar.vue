<template>
  <FullCalendar v-bind:options="options" />
</template>

<script setup>
import { reactive, ref } from 'vue';
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';
import interactionPlugin from '@fullcalendar/interaction';
import useEvent from '../composables/useEvent.js';

const { getEvents, createEvent, updateEvent, deleteEvent } = useEvent();

const id = ref(10);

const options = reactive({
  plugins: [dayGridPlugin, timeGridPlugin, listPlugin, interactionPlugin],
  initialView: 'timeGridMonth',
  headerToolbar: {
    left: 'prev,next today',
    center: 'title',
    right: 'dayGridMonth,timeGridWeek,listDay',
  },
  editable: true,
  selectable: true,
  weekends: true,
  select: (arg) => {
    id.value = id.value + 1;

    const cal = arg.view.calendar;
    cal.unselect();
    cal.addEvent({
      id: `${id.value}`,
      title: `New event ${id.value}`,
      start: arg.start,
      end: arg.end,
      allDay: true,
    });
  },
  eventClick: (arg) => {
    console.log(arg.event.title);
  },
  events: [],
  eventAdd: (arg) => {
    createEvent({
      id: arg.event.id,
      title: arg.event.title,
      start: arg.event.start,
      end: arg.event.end,
      allDay: arg.event.allDay,
    });
  },
  eventChange: (arg) => {
    updateEvent({
      id: arg.event.id,
      title: arg.event.title,
      start: arg.event.start,
      end: arg.event.end,
      allDay: arg.event.allDay,
    });
  },
  eventRemove: (arg) => {
    deleteEvent({
      id: arg.event.id,
      title: arg.event.title,
      start: arg.event.start,
      end: arg.event.end,
      allDay: arg.event.allDay,
    });
  },
});

options.events = getEvents.value;
</script>
