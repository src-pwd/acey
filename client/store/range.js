import fetch from 'isomorphic-fetch'
import store from './index'
export const ADD_RANGE = 'ADD_RANGE'
export const DELETE_RANGE = 'DELETE_RANGE'
export const SAVE_RANGE_PRED = 'SAVE_RANGE_PRED'

const state = {
  options: [],
  name: '',
  description: '',
  expired: '',
  type: 'Prediction',
  currency_pairin: 'DASH',
  currency_pairout: 'XMR',
  exchange: 'bitfinex',
  created: false,
  errors: {}
}

const mutations = {
  updateName (state, name) {
    state.name = name
  },
  updateCreated (state) {
    state.created = true
    state.options = []
    state.name = ''
    state.description = ''
    state.expired = ''
    state.currency_pair = ''
    state.exchange = ''
  },
  updateDesc (state, desc) {
    state.description = desc
  },
  updateExp (state, exp) {
    state.expired = exp
  },
  updatePairIn (state, exp) {
    state.currency_pairin = exp
  },
  updatePairOut (state, exp) {
    state.currency_pairout = exp
  },
  updateExchange (state, exp) {
    state.exchange = exp
  },
  updateOptions (state, options) {
    state.options = options
  },
  updateErrors (state, item) {
    state.errors = item
  }
}

const actions = {
  saveRangePrediction ({ commit }) {
    const data = {
      creator: store.state.auth.username,
      currency_pair: state.currency_pairin + '/' + state.currency_pairout,
      description: state.description,
      exchange: state.exchange,
      expired: state.expired,
      name: state.name,
      options: state.options
    }
    fetch('http://localhost:8000/api/predictions/', {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }

    }).then(response => {
      if (!response.ok) {
        response.json().then(el => {
          this.commit('updateErrors', el)
        })
        return
      }
      response.json().then(() => {
        this.commit('updateCreated')
      })
    })
  }
}

export default {
  state,
  actions,
  mutations
}
