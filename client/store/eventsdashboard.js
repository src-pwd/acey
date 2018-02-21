import store from './index.js' // path to your Vuex store

const state = {
  events: [
    {
      id: 35,
      name: 'kek',
      description: 'kekcoin will grow 505%',
      peoplesVoted: 345005,
      aceyVoted: 505445,
      ends: '34543-3241-23PM',
      type: 'accuracy'
    },
    {
      id: 47,
      name: 'lol',
      description: 'lolicon is best, will grow 10%',
      peoplesVoted: 2314324,
      aceyVoted: 435439593548934,
      ends: '34543-3241-23PM',
      type: 'range'

    },
    {
      id: 52,
      name: 'pizda',
      description: 'will not grow, will deep to 4500 satoshi',
      peoplesVoted: 32452345,
      aceyVoted: 3223142314,
      ends: '34543-3241-23PM',
      type: 'accuracy'
    },
    {
      id: 33,
      name: 'huy',
      description: 'nu tut vse yasno',
      peoplesVoted: 32453245,
      aceyVoted: 43589234958,
      ends: '34543-3241-23PM',
      type: 'accuracy'
    }
  ]
}

const getters = {
  currentEvent: state => {
    const event = state.events.find(el => el.id === Number(store.state.route.params.id))
    return event
  }
}

const mutations = {}

const actions = {}

export default {
  state,
  actions,
  mutations,
  getters
}
