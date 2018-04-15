import fetch from 'isomorphic-fetch'

const state = {

}

const mutations = {
}

const actions = {
  predictionBet (state, payload) {
    console.log(payload)
    fetch('http://localhost:8000/api/bets/', {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(payload), // data can be `string` or {object}!
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(response => {
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
