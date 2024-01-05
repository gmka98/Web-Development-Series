<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column flex flex">

      <q-toolbar class="bg-secondary shadow-2 rounded-borders">
        <q-icon color="white" class="q-mr-sm-" size="40px" name="person" />
        <q-separator vertical inset />
        <div class="q-ml-lg text-white">
          <p class="">200</p>
          <p>Junior</p>
        </div>

        <q-space />
      </q-toolbar>

      <q-toolbar class="bg-secondary shadow-2 rounded-borders">
        <q-icon color="white" class="q-mr-sm" size="40px" name="account_circle" />
        <q-separator vertical inset />
        <div class="q-ml-lg text-white">
          <p class="">20</p>
          <p>Medior</p>
        </div>

        <q-space />
      </q-toolbar>

      <q-toolbar class="bg-secondary shadow-2 rounded-borders">
        <q-icon color="white" class="q-mr-sm" size="40px" name="supervisor_account" />
        <q-separator vertical inset />
        <div class="q-ml-lg text-white">
          <p class="">5</p>
          <p>Senior</p>
        </div>

        <q-space />
      </q-toolbar>
      
    </div>
  </div>
</template>
<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'AdminViews',
  
});
</script>