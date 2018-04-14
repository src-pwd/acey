/*eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import store from 'store'
import Authorization from 'views/Authorization'

import Dashboard from 'views/Dashboard'

import Create from 'views/Create'
import CreateRange from 'views/Create/range.vue'
import CreateAccuracy from 'views/Create/accuracy.vue'
import CreateParlay from 'views/Create/parlay.vue'

import UserDashboard from 'views/UserDashboard'

import Event from 'views/Event'

Vue.use(Router)

export const routes = [
  
  {
    path: '/',
    redirect: '/dashboard',
    meta: {
      title: 'Dashboard'
    }
  },
  {
    path: '/login',
    component: Authorization,
    meta: {
      title: 'Authorization'
    }
  },
  { 
    path: '/dashboard',
    component: Dashboard,
    meta: {
      title: 'Dashboard',
      requiresAuth: true
    }
  },
  {
    path: '/create',
    component: Create,
    meta: {
      title: 'Create',
      requiresAuth: true
    },
    children: [
      {
        path: 'range',
        component: CreateRange
      },
      {
        path: 'accuracy',
        component: CreateAccuracy
      },
      {
        path: 'parlay',
        component: CreateParlay
      }
    ]
  },
  {
    path: '/user_dashboard',
    component: UserDashboard,
    meta: {
      title: "User's dasbhboard",
      requiresAuth: true
    }
  },
  {
    path: '/event/:id',
    component: Event,
    meta: {
      title: 'Event',
      requiresAuth: true
    }
  },
]

export const router = new Router({ mode: 'history', routes })

console.log(store)

router.beforeEach((to, from, next) => {
  if (
    to.matched.some(record => record.meta.requiresAuth) &&
    !store.state.auth.loggedIn
  ) {
    next({ path: '/login', query: { redirect: to.fullPath }})
  } else {
    next()
  }
})
