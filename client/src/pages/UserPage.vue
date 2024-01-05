<template class="">
  <div class="q-pa-md q-gutter-sm">
    <q-banner rounded class="bg-green-8 text-white">
     <div class="flex justify-between ">
      <div>DASHBOARD</div>
      <div>{{ formattedDate }}</div>
     </div> 
      
    </q-banner>
    <div class="">
    Last Evaluations
    <q-banner rounded class="bg-green-8 text-white">
      <p class="q-mb-xl ">Overall attendance rate: 79.63% </p>
      <p>Active participation in the course </p>
      <p>Behavior during the lesson:  {{good}}  </p>
      <p class="q-mb-xl">Acquisition of knowledge:  {{partial}} </p>
    </q-banner>
  </div>
  <div class="flex justify-between q-pb-xl q-py-lg">
    <div>
      <p>Next Course</p>
      <q-banner rounded class="bg-green-8 text-white">
        <p>Level 3 - Collaboration</p>
        <p></p>
      </q-banner>
    </div>
  <div>
    <p>Next Event</p>
      <q-banner rounded class="bg-green-8 text-white">
        <p>23 April</p>
        <p>04:00 pm</p>
      </q-banner>
  </div>
</div>
    
  </div>
</template>

<script>
import { defineComponent } from 'vue'


export default defineComponent({
  name: 'IndexPage',
  data() {
    return {
      formattedDate: this.formatDate(),
    }
  },
  methods: {
    formatDate() {
      const timeStamp = Date.now()
      // Use Intl.DateTimeFormat for formatting based on user's locale
      const formattedDate = new Intl.DateTimeFormat(undefined, {
        year: 'numeric',
        month: 'numeric',
        month: 'long',
        day: 'numeric',
        weekday: 'long',
      }).format(timeStamp)

      return formattedDate
    },
  },
})
</script>
