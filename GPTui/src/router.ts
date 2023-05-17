import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import DiagnosisComponent from './components/Diagnosis.vue'
const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/',
    component: DiagnosisComponent
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router