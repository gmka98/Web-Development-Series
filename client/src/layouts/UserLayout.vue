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
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
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
        class="bg-green-9"
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
    </div>            
    <div class="text-center text-white"> Junior </div>
    </div>
  </div>
    <hr>
      <q-scroll-area class="" style="height: calc(100% - 150px); margin-top: 10px; border-right: 1px solid #115325">
        <q-list>
  <template v-for="(menuItem, index) in menuList" :key="index">
    <q-item class="text-white" clickable :active="menuItem.label === 'Outbox'" v-ripple>
      <q-item-section avatar class="">
        <q-icon :name="menuItem.icon" />
      </q-item-section>
      <q-item-section class="">
        {{ menuItem.label }}
      </q-item-section>
    </q-item>
    <q-separator :key="'sep' + index" v-if="menuItem.separator" />
  </template>
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
      </q-page-container>                                                                                                                                                                                   21
    </q-layout>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue'
  
  const menuList = [
  {
    icon: 'account_circle',
    label: 'Profile',
    separator: false
  },
  {
    icon: 'event',
    label: 'Event',
    separator: false
  },
  {
    icon: 'work',
    label: 'Course',
    separator: false
  },
  {
    icon: 'chat',
    label: 'Message',
    separator: true
  },
  
]
  
  
export default defineComponent({
  name: 'UserLayout',
  setup() {
    const leftDrawerOpen = ref(false)

    return {
      menuList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>