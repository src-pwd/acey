/*eslint-disable*/

import fetch from 'isomorphic-fetch'
import store from './index'
import { router } from '../router' // Vue Router


const state = {
  details: JSON.parse(localStorage.getItem('about')) || {}
}

const getters = {}

const mutations = {

  aboutUser (state, value) {
    state.details = value
    localStorage.setItem('about', JSON.stringify(state.details))
  }

}

const actions = {
  getUserInfo (state) {
    fetch('http://app.acey.it/api/users/username/', {
      method: 'get',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'JWT ' + store.state.auth.jwt
      }
    }).then(
      el => el.json().then(el => {
        if(el.detail) {
          store.commit('removeToken')  
        }
     
      this.commit('aboutUser', el)
      }
      )
    )
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}
