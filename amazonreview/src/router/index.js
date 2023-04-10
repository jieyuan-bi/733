import { createRouter, createWebHistory } from 'vue-router'
import theHome from '../views/Home.vue'
import ReviewAnalysis from '../views/ReviewAnalysis.vue'
import Recommend from '../views/Recommend.vue'
import SentimentAnalysis from '../views/Sentiment.vue'
import ReviewSummarization from '../views/Summarization.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: theHome,
  },
  {
    path: '/review_analysis',
    name: 'ReviewAnalysis',
    component: ReviewAnalysis,
  },
  {
    path: '/recommend',
    name: 'theRecommend',
    component: Recommend,
  },
  {
    path: '/sentiment',
    name: 'Sentiment',
    component: SentimentAnalysis,
  },
  {
    path: '/summarization',
    name: 'Summarization',
    component: ReviewSummarization,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
