import { createRouter, createWebHistory } from 'vue-router'
import Layout from '@/layout/Layout'

const routes = [
  {
    path: '',
    name: 'Layout',
    component: Layout,
    redirect: "/home",
    children: [
      {
        path: 'home',
        name: 'Home',
        component: () => import("@/views/Home"),
      },
    ]
  },
  {

  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
