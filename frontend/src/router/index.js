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
    name: 'Home',
    component: HomeView
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

router.beforeEach((to, from, next) => {
  document.title = `Finance - ${to.name}`
  next()
})

export default router
