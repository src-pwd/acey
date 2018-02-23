export const ADD_RANGE = 'ADD_RANGE'
export const DELETE_RANGE = 'DELETE_RANGE'
export const SAVE_RANGE_PRED = 'SAVE_RANGE_PRED'

const state = {
  name: '',
  description: '',
  expired: ''

}

const mutations = {
  updateNameAcc (state, name) {
    state.name = name
  },
  updateDescAcc (state, desc) {
    state.description = desc
  },
  updateExpAcc (state, exp) {
    state.expired = exp
  }
}

const actions = {}

export default {
  state,
  actions,
  mutations
}
