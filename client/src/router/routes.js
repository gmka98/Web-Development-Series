
const routes = [
  {
    path: '',
    component: () => import('layouts/HomeLayout.vue'),
    children: [
      { path: '', component: () => import('pages/HomePage.vue') }
    ]
  },
  {
    path: '/user',
    component: () => import('layouts/UserLayout.vue'),
    children: [
      { path: '', component: () => import('pages/UserPage.vue') },
      { path: 'course', component: () => import('pages/UserPage.vue') },
      { path: 'event', component: () => import('pages/UserPage.vue') },

    ]
  },
  {
    path: '/admin',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/AdminPage.vue') }
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
