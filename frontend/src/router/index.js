import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthView from '@/views/AuthView'
import HistoryView from '@/views/HistoryView'

const routes = [
  {
    path: '/auth',
    name: 'Auth',
    component: AuthView
  },
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/components/RegisterVue.vue')
  },
  {
    path: '/history',
    name: 'History',
    component: HistoryView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
