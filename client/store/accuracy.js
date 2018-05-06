import fetch from 'isomorphic-fetch'
import store from './index'
export const ADD_RANGE = 'ADD_RANGE'
export const DELETE_RANGE = 'DELETE_RANGE'
export const SAVE_RANGE_PRED = 'SAVE_RANGE_PRED'

const state = {
  name: '',
  description: '',
  expired: '',
  type: 'AccuratePrediction',
  currency_pair: '',
  exchange: '',
  created: false
}

const mutations = {
  updateNameAcc (state, name) {
    state.name = name
  },
  updateCreatedAcc (state) {
    state.name = ''
    state.description = ''
    state.expired = ''
    state.currency_pair = ''
    state.exchange = ''
    state.created = true
  },
  updateDescAcc (state, desc) {
    state.description = desc
  },
  updateExpAcc (state, exp) {
    state.expired = exp
  },
  updatePairAcc (state, exp) {
    state.currency_pair = exp
  },
  updateExchangeAcc (state, exp) {
    state.exchange = exp
  }
}

const actions = {

  saveAccuracy ({ commit }) {
    const data = {
      creator: store.state.auth.username,
      currency_pair: state.currency_pair,
      description: state.description,
      exchange: state.exchange,
      expired: state.expired,
      name: state.name,
      type: state.type
    }
    fetch('http://localhost:8000/api/events/', {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }

    }).then(response => {
      if (!response.ok) {
        response.json().then(el => window.alert(el))
        return
      }
      response.json().then(() => {
        this.commit('updateCreatedAcc')
      })
    })
  }

}

export default {
  state,
  actions,
  mutations
}
