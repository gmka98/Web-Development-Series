import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    component: () => import('layouts/Login.vue'),
    children: [
      { path: '', component: () => import('pages/Login.vue') },
    ]
  },
  {
    path: '/dashboard',
    component: () => import('layouts/DashboardUser.vue'),
    children: [
      { path: '', component: () => import('pages/User.vue') },
      { path: 'course', component: () => import('pages/Course.vue') },
      { path: 'calendar', component: () => import('pages/Calendar.vue') },
      { path: 'evaluation', component: () => import('pages/Evaluations.vue') },
    ]
  },
  {
    path: '/admin',
    component: () =>import('layouts/DashboardAdmin.vue'),
    children: [
      {path: '', component: () =>import('pages/Admin.vue')},
      {path: 'student', component: () =>import('pages/Student.vue')},
      {path: 'event', component: () =>import('pages/CalendarAdmin.vue')},
      {path: 'note', component: () =>import('pages/Note.vue')},
      { path: 'course', component: () => import('pages/Course.vue') },




    ]
  },
  

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  },
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('pages/Login.vue')
  },
  {
    path: '/dashboard/:userId',
    name: 'dashboard',
    component: () => import('pages/User.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/admin/:userId',
    name: 'admin',
    component: () => import('pages/Admin.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  }
]

export default routes
