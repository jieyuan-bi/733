import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
// import User from '../views/User.vue'
// import Login from '../views/Login.vue'
// import Signup from '../views/Signup.vue'
// import Manage from '../views/Manage.vue'

const routes = [
  {
    path: '/home/',
    name: 'Home',
    component: Home,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
