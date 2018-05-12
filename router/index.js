import Vue from 'vue'
import Router from 'vue-router'

import Authorization from 'views/Authorization'

import Dashboard from 'views/Dashboard'

import Create from 'views/Create'
import CreateRange from 'views/Create/range'
import CreateAccuracy from 'views/Create/accuracy'
import CreateParlay from 'views/Create/parlay'

import UserProfile from 'views/UserProfile'

import Event from 'views/Event'
import ChooseParlay from 'views/Event/voteparlay'

import NotFoundComponent from 'views/NotFoundComponent'

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
        path: '',
        component: 'Create'
      },
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
    component: UserProfile,
    meta: {
      title: 'User\'s dasbhboard'
    }
  }, {
    path: 'event/:id/',
    component: Event,
    meta: {
      title: 'Event'
    }
  },
  {
    path: '/option/:id',
    component: ChooseParlay,
    title: 'Parlay'
  },
  {
    path: '/event',
    redirect: '/dashboard'
  },
  { path: '*', component: NotFoundComponent }
]

export const router = new Router({ mode: 'history', routes })
