<template>
  <q-layout view="hHh Lpr lff">
    <q-header reveal bordered class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />
        <q-toolbar-title>
          <q-avatar>
            <img src="../../public/adimian-logo.jpg" />
          </q-avatar>
          Development Profesionnal Series
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="leftDrawerOpen" side="left" behavior="desktop" elevated>
      <!-- drawer content -->
      <div>
        <img src="../../public/Junior.jpg" />
        <h1>Junior</h1>
        <hr />
        <a href="/dashboard">Dashboard</a>
        <br>
        <a href="dashboard/course">Course</a>
        <br>
        <a href="dashboard/calendar">Calendar</a>
        <br>
        <a href="dashboard/evaluation">Evaluation</a>
        <br>
        <a href="https://slack.com/intl/fr-be/">Message</a>

        <hr />
        <a href="/">Log out</a>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'

const linksList = [
  {
    title: 'Profil',
    caption: 'quasar.dev',
    icon: 'school',
    link: '/'
  },
  {
    title: 'Course',
    caption: 'Exercices',
    icon: 'code',
    link: '/course'
  },
  {
    title: 'Event',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: '/event'
  },
  {
    title: 'Message',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://slack.com/intl/fr-be/'
  },
]

export default defineComponent({
  name: 'MainLayout',

  setup() {
    const leftDrawerOpen = ref(false)

    function toggleLeftDrawer() {
      leftDrawerOpen.value = !leftDrawerOpen.value
    }

    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer,
    }
  },
})
</script>
