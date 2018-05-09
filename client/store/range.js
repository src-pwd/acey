import fetch from 'isomorphic-fetch'
import store from './index'
export const ADD_RANGE = 'ADD_RANGE'
export const DELETE_RANGE = 'DELETE_RANGE'
export const SAVE_RANGE_PRED = 'SAVE_RANGE_PRED'

const state = {
  options: [
    {
      sum_from: null,
      sum_to: null
    },
    {
      sum_from: null,
      sum_to: null
    }
  ],
  name: '',
  description: '',
  expired: '',
  type: 'Prediction',
  currency_pair: '',
  exchange: '',
  created: false
}

const mutations = {
  updateName (state, name) {
    state.name = name
  },
  updateCreated (state) {
    state.created = true
    state.options = [
      {
        sum_from: null,
        sum_to: null
      },
      {
        sum_from: null,
        sum_to: null
      }
    ]
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
  updatePair (state, exp) {
    state.currency_pair = exp
  },
  updateExchange (state, exp) {
    state.exchange = exp
  },
  [ADD_RANGE] (state, range) {
    if (state.options.length < 5) {
      state.options.push({
        name: '',
        sum_from: null,
        sum_to: null
      })
    }
  },
  itemPriceFrom (state, payload) {
    state.options[payload[1]].sum_from = Number(payload[0])
  },
  itemPriceTo (state, payload) {
    state.options[payload[1]].sum_to = Number(payload[0])
  },
  deleteRange (state, item) {
    state.options = state.options.filter(el => el.name !== item)
  },
  [SAVE_RANGE_PRED] (state) {}
}

const actions = {
  addNewRange ({ commit }) {
    commit({ type: ADD_RANGE })
  },

  saveRangePrediction ({ commit }) {
    console.log('lol')
    console.log(state)

    const data = {
      creator: store.state.auth.username,
      currency_pair: state.currency_pair,
      description: state.description,
      exchange: state.exchange,
      expired: state.expired,
      name: state.name,
      options: state.options
    }
    fetch('http://app.acey.it/api/predictions/', {
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
