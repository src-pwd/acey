/*eslint-disable*/

import fetch from 'isomorphic-fetch'
import store from './index'

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
    console.log(store.state.auth.token)
    fetch('http://localhost:8000/api/users/username/', {
      method: 'get',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'JWT ' + store.state.auth.jwt
      }
    }).then(
      el => el.json().then(el => this.commit('aboutUser', el))
      )
  }
}

export default {
  state,
  actions,
  mutations,
  getters
}
