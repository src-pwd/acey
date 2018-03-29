import Vue from 'vue'
import Router from 'vue-router'

import Authorization from 'Views/Authorization'

import Dashboard from 'Views/Dashboard'

import Create from 'Views/Create'
import CreateRange from 'Views/Create/range.vue'
import CreateAccuracy from 'Views/Create/accuracy.vue'
import CreateParlay from 'Views/Create/parlay.vue'

import UserDashboard from 'Views/UserDashboard'

import Event from 'views/Event'

Vue.use(Router)

export const routes = [
  {
    path: '/',
    component: Authorization,
    meta: {
      title: 'Authorization'
    }
  }, {
    path: '/dashboard',
    component: Dashboard,
    meta: {
      title: 'Dashboard'
    }

  },
  {
    path: '/create',
    component: Create,
    meta: {
      title: 'Create'
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
  }, {
    path: '/user_dashboard',
    component: UserDashboard,
    meta: {
      title: 'User\'s dasbhboard'
    }
  }, {
    path: '/event/:id',
    component: Event,
    meta: {
      title: 'Event'
    }
  },
  {
    path: '/event',
    redirect: '/dashboard'
  }
]

export const router = new Router({ mode: 'history', routes })
