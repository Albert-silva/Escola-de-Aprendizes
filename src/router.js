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
    },
    {
      path: '/dash',
      component:  () => import('@/pages/Dashboard'),
      children: [
        {
          path: 'users',
          component:  () => import('@/pages/Users')
        },
        {
          path: 'profile',
          component:  () => import('@/pages/Profile')
        },
        {
          path: 'conteudo',
          component:  () => import('@/pages/Conteudo')
        },
        {
          path: 'add-conteudo',
          component:  () => import('@/pages/AddConteudo')
        },
        {
          path: 'edit-conteudo/:id',
          component:  () => import('@/pages/UpdateConteudo')
        },
        {
          path: 'criaalunoconteudo',
          component:  () => import('@/pages/AlunoConteudo')
        },
      ]
    }
  ]
})

export default router