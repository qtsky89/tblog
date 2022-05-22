import { RouteRecordRaw } from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'root',
        path: '',
        component: () => import('pages/IndexPage.vue'),
      },
    ],
  },
  {
    path: '/create',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'create',
        path: '',
        component: () => import('pages/CreatePage.vue'),
      },
    ],
  },
  {
    path: '/update/:id',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'update',
        path: '',
        component: () => import('pages/UpdatePage.vue'),
      },
    ],
  },
  {
    path: '/post/:id',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { name: 'read', path: '', component: () => import('pages/ReadPage.vue') },
    ],
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    name: 'notfound',
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
