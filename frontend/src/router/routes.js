
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
      {path: 'calendar', component: () => import('pages/Calendar.vue')},

      {path: 'evaluation', component: () => import('pages/Evaluations.vue')}
    ]
  },
  {
    path: '/admin',
    component: () =>import('layouts/DashboardAdmin.vue'),
    children: [
      {path: '', component: () =>import('pages/Admin.vue')},
      {path: 'student', component: () =>import('pages/Student.vue')},
      {path: 'event', component: () =>import('pages/Event.vue')}


    ]
  },
  

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
