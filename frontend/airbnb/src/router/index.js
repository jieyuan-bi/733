import { createRouter, createWebHistory } from 'vue-router'
import theHome from '../views/Home.vue'
import ReviewAnalysis from '../views/ReviewAnalysis.vue'

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: theHome,
  },
  {
    path: '/review_analysis',
    name: 'ReviewAnalysis',
    component: ReviewAnalysis,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
