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
      <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #115325">
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
      <q-img class="absolute-top  bg-green-9 "  style="height: 150px" border-bottom: 1px solid text-white ; >
          <div class="absolute-bottom bg-transparent">
            <q-avatar  size="56px" class="q-mb-sm">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png" class="mx-auto">
            </q-avatar>
            <div class="text-weight-bold">Grade</div>
            <div> email </div>
          </div>
        </q-img>
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