import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/views/home'
import Login from '@/views/login'
import Register from '@/views/register'
import User from '@/views/user'
import Contacts from '@/views/contacts'
import Explore from '@/views/explore'

Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', redirect: { name: 'home' } },
    { path: '/home', name: 'home', component: Home },
    { path: '/login', name: 'login', component: Login },
    { path: '/register', name: 'register', component: Register },
    { path: '/user', name: 'user', component: User },
    { path: '/contacts', name: 'contacts', component: Contacts },
    { path: '/explore', name: 'explore', component: Explore },
  ]
})
