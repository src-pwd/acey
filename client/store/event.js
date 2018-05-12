import fetch from 'isomorphic-fetch'

const state = {

}

const mutations = {
}

const actions = {
  predictionBet (state, payload) {
    console.log(payload)
    fetch('http://app.acey.it/api/bets/', {
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
        console.log(el)
      })
    })
  },
  accurateBet (state, payload) {
    console.log(payload)
    fetch('http://app.acey.it/api/accuratebets/', {
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
        console.log(el)
      })
    })
  }
}

export default {
  state,
  actions,
  mutations
}
