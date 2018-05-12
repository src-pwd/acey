import fetch from 'isomorphic-fetch'
import store from './index'

const state = {
  name: '',
  description: '',
  expired: '',
  type: 'Parlay',
  currency_pairIn: 'DASH',
  currency_pairOut: 'XMR',
  exchange: 'bitfinex',
  created: false,
  errors: {}
}

const mutations = {
  updateNamePar (state, name) {
    state.name = name
  },
  updateCreatedPar (state) {
    state.name = ''
    state.description = ''
    state.expired = ''
    state.currency_pair = ''
    state.exchange = ''
    state.created = true
  },
  updateDescPar (state, desc) {
    state.description = desc
  },
  updateExpPar (state, exp) {
    state.expired = exp
  },
  updatePairParIn (state, exp) {
    state.currency_pairIn = exp
  },
  updatePairParOut (state, exp) {
    state.currency_pairOut = exp
  },
  updateExchangePar (state, exp) {
    state.exchange = exp
  },
  updateErrors (state, item) {
    state.errors = item
  }
}

const actions = {

  savePar ({ commit }) {
    const data = {
      creator: store.state.auth.username,
      currency_pair: state.currency_pairIn + '/' + state.currency_pairOut,
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
        response.json().then(el => {
          this.commit('updateErrors', el)
        })
        return
      }
      response.json().then(() => {
        this.commit('updateCreatedPar')
      })
    })
  }

}

export default {
  state,
  actions,
  mutations
}
