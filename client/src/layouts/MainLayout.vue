<template>
  <q-layout 
  view="lHh Lpr lFf"
  >
    <q-header elevated>
      <q-toolbar
      class="bg-green-9">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Professional Development Series
        </q-toolbar-title>
       
        <div class="flex flex-center">
          <div>
          
          <img
          alt="Adimian logo"
          src="~assets/Adimian.png"
          style="width: 100px; height: 75px"
          >
          </div>
        </div>
      
       
      
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class=" bg-green-9"
    >
    <div class="q-py-lg">
    <div class="q-mx-xl">
      <q-btn rounded color="white">
      <q-avatar
      round
      color="white"
      size="100px"
      class="overlapping q-mx-lg "
      :style="`center: 50px`"
    >
      <img 
      src="https://cdn.quasar.dev/img/avatar.png" class="">
    </q-avatar>
  </q-btn>
    <div>
      <q-badge  color="red" rounded class="" />
      <span class="text-white text-center">Admin</span>
    </div>            
    <div class="text-center text-white"> email </div>
    </div>
  </div>
    <hr>
    <q-scroll-area class="fit  ">
          <q-list padding class="menu-list border-2 border-solid border-white ">
            <q-item clickable v-ripple class="text-white">
              <q-item-section avatar>
                <q-icon name="dashboard" />
              </q-item-section>

              <q-item-section>
                Dashboard
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple class="text-white">
              <q-item-section avatar>
                <q-icon name="person" />
              </q-item-section>

              <q-item-section>
                Profile
              </q-item-section>
            </q-item>

            <q-item active clickable v-ripple class="text-white">
              <q-item-section avatar>
                <q-icon name="school" />
              </q-item-section>

              <q-item-section>
                Classes
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple class="text-white">
              <q-item-section avatar>
                <q-icon name="local_library" />
              </q-item-section>

              <q-item-section>
                Courses
              </q-item-section>
            </q-item>

            <q-item clickable v-ripple class="text-white">
              <q-item-section avatar>
                <q-icon name="notes" />
              </q-item-section>

              <q-item-section>
                Evaluations
              </q-item-section>
            </q-item>
            <q-item clickable v-ripple class="text-white">
              <q-item-section avatar>
                <q-icon name="event" />
              </q-item-section>

              <q-item-section>
                Event
              </q-item-section>
            </q-item>
            <q-item clickable v-ripple class="text-white">
              <q-item-section avatar>
                <q-icon name="drafts" />
              </q-item-section>

              <q-item-section>
                Messages
              </q-item-section>
            </q-item>
          </q-list>
        </q-scroll-area>
       

        <a href="/">
      <div class="absolute-bottom text-center text-white hover:text-black">
        <q-icon name="logout" size="2em"/>
        LOG OUT
      </div>
       </a>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLinkVue from 'src/components/EssentialLink.vue'

const menuList = [
  {
    icon: 'inbox',
    label: 'Inbox',
    separator: true
  },
  {
    icon: 'send',
    label: 'Outbox',
    separator: false
  },
  {
    icon: 'delete',
    label: 'Trash',
    separator: false
  },
  {
    icon: 'error',
    label: 'Spam',
    separator: true
  },
  {
    icon: 'settings',
    label: 'Settings',
    separator: false
  },
  {
    icon: 'feedback',
    label: 'Send Feedback',
    separator: false
  },
  {
    icon: 'help',
    iconColor: 'primary',
    label: 'Help',
    separator: false
  }
]
  
export default {
  setup (){
    const leftDrawerOpen = ref(false)

    return {
      drawer: ref(false),
      menuList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      fitModes: [ 'cover' ]

    }
  }
}
</script>