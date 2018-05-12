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

Vue.use(Router)

const withPrefix = (prefix, routes) => 
    routes.map( (route) => {
        route.path = prefix + route.path;
        return route;
    });

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
  ...withPrefix('/create',[
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
    ]),
  {
    path: '/create',
    component: Create,
    meta: {
      title: 'Create'
    }
  }, {
    path: '/user_dashboard',
    component: UserProfile,
    meta: {
      title: 'User\'s dasbhboard'
    }
  }, {
    path: '/event/:id/',
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
  {
    path: '*',
    redirect: '/'
  }
]

export const router = new Router({ mode: 'history', routes })
