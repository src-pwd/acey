import fetch from 'isomorphic-fetch'
import store from './index'

const state = {
  details: {}
}

const getters = {}

const mutations = {
  aboutUser (state, value) {
    state.details = value
  }

}

const actions = {
  getUserInfo (state) {
    console.log(store.state.auth.token)
    fetch('http://app.acey.it/api/users/username/', {
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
