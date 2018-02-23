import Vue from 'vue'
import Router from 'vue-router'
import Create from 'views/Create'
import Post from 'views/Post'
import About from 'views/About'
import Accuracy from 'views/Accuracy'
import Play from 'views/Play'
import Range from 'views/Range'
import Event from 'views/Event'
import UserDashboard from 'views/UserDashboard'

Vue.use(Router)

export const routes = [
  {
    path: '/',
    component: Create,
    meta: {
      title: 'Create'
    }
  }, {
    path: '/post/:id',
    component: Post,
    meta: {
      title: 'Post'
    }
  }, {
    path: '/about',
    component: About,
    meta: {
      title: 'About'
    }
  }, {
    path: '/play',
    component: Play,
    meta: {
      title: 'Play'
    }
  }, {
    path: '/range',
    component: Range,
    meta: {
      title: 'Range prediction'
    }
  }, {
    path: '/accuracy',
    component: Accuracy,
    meta: {
      title: 'Accuracy prediction'
    }
  }, {
    path: '/user_dashboard',
    component: UserDashboard,
    meta: {
      title: 'User\'s dashboard'
    }
  }, {
    path: '/event/:id',
    component: Event,
    meta: {
      title: 'Event'
    }
  }
]
export const router = new Router({ mode: 'history', routes })
