<template class="">
  <div class="q-pa-md q-gutter-sm">
    <q-banner rounded class="bg-green-8 text-white">
     <div class="flex justify-between ">
      <div>DASHBOARD</div>
      <div>{{ formattedDate }}</div>
     </div> 
      
    </q-banner>
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
