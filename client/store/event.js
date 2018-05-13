import fetch from 'isomorphic-fetch'

const state = {

}

const mutations = {
}

const actions = {
  predictionBet (state, payload) {
    fetch('http://localhost:8000/api/bets/', {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(payload), // data can be `string` or {object}!
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      if (!response.ok) {
        response.json().then(el => window.alert(el))
        return
      }
      response.json().then(el => {
      })
    })
  },
  accurateBet (state, payload) {
    fetch('http://localhost:8000/api/accuratebets/', {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(payload), // data can be `string` or {object}!
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      if (!response.ok) {
        response.json().then(el => window.alert(el))
        return
      }
      response.json().then(el => {
      })
    })
  }
}

export default {
  state,
  actions,
  mutations
}
