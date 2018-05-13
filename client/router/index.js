/*eslint-disable */
import Vue from "vue";
import Router from "vue-router";
import store from "store";
import Authorization from "views/Authorization";

import Dashboard from "views/Dashboard";

import Create from "views/Create";
import CreateRange from "views/Create/range.vue";
import CreateAccuracy from "views/Create/accuracy.vue";
import CreateParlay from "views/Create/parlay.vue";

import UserProfile from "views/UserProfile";

import Event from "views/Event";
import NotFoundComponent from "views/NotFoundComponent";

import Leaderboard from "views/Leaderboard";

Vue.use(Router);

export const routes = [
  {
    path: "/",
    redirect: "/dashboard",
    meta: {
      title: "Dashboard",
      requiresAuth: true
    }
  },
  {
    path: "/login",
    component: Authorization,
    meta: {
      title: "Authorization"
    }
  },
  {
    path: "/dashboard",
    component: Dashboard,
    meta: {
      title: "Dashboard",
      requiresAuth: true
    }
  },
  {
    path: "/create",
    component: Create,
    meta: {
      title: "Create",
      requiresAuth: true
    },
    children: [
      {
        path: "range",
        component: CreateRange,
        meta: {
          requiresAuth: true
        }
      },
      {
        path: "accuracy",
        component: CreateAccuracy,
        meta: {
          requiresAuth: true
        }
      },
      {
        path: "parlay",
        component: CreateParlay,
        meta: {
          requiresAuth: true
        }
      }
    ]
  },
  {
    path: "/profile",
    component: UserProfile,
    meta: {
      title: "User's profile",
      requiresAuth: true
    }
  },
  {
    path: "/event/:id",
    component: Event,
    meta: {
      title: "Event",
      requiresAuth: true
    }
  },
  {
    path: "*",
    component: Dashboard,
    meta: {
      title: "Dashboard",
      requiresAuth: true
    }
  },
  {
    path: "/leaderboard",
    component: Leaderboard,
    meta: {
      title: "Leaderboard",
      requiresAuth: true
    }
  }
];

export const router = new Router({ mode: "history", routes });


router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.state.auth.loggedIn) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next() // make sure to always call next()!
  }
})