    export const ADD_RANGE = 'ADD_RANGE'
    export const DELETE_RANGE = 'DELETE_RANGE'
    export const SAVE_RANGE_PRED = 'SAVE_RANGE_PRED'

    const state = {
      ranges: [
        {
          name: '',
          priceFrom: null,
          priceTo: null
        },
        {
          name: '',
          priceFrom: null,
          priceTo: null
        }
      ],
      name: '',
      description: '',
      expired: ''
    }

    const mutations = {
      updateName (state, name) {
        state.name = name
      },
      updateDesc (state, desc) {
        state.description = desc
      },
      updateExp (state, exp) {
        state.expired = exp
      },
      [ADD_RANGE] (state, range) {
        if (state.ranges.length < 5) {
          state.ranges.push({
            name: '',
            priceFrom: null,
            priceTo: null
          })
        }
      },
      itemName (state, payload) {
        state.ranges[payload[1]].name = payload[0]
      },
      itemPriceFrom (state, payload) {
        state.ranges[payload[1]].priceFrom = Number(payload[0])
      },
      itemPriceTo (state, payload) {
        state.ranges[payload[1]].priceTo = Number(payload[0])
      },
      deleteRange (state, item) {
        state.ranges = state.ranges.filter(el => el.name !== item)
      },
      [SAVE_RANGE_PRED] (state) {}
    }

    const actions = {
      addNewRange ({ commit }) {
        commit({ type: ADD_RANGE })
      },

      saveRangePrediction ({ commit }) {
        commit({ type: SAVE_RANGE_PRED })
      }
    }

    export default {
      state,
      actions,
      mutations
    }
