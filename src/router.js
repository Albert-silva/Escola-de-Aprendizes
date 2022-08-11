import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.VUE_APP_BASE_URL,
  routes: [
    // Login
    {
      path: '/',
      redirect: 'login'
    },
    {
      path: '/login',
      component:  () => import('@/pages/Login')
    }
  ]
})

export default router