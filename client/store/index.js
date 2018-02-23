import Vue from 'vue'
import Vuex from 'vuex'
import ui from './ui'
import range from './range'
import accuracy from './accuracy'
import eventsDashboard from './eventsdashboard'
import user from './user'
import event from './event'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    ui,
    range,
    accuracy,
    eventsDashboard,
    user,
    event
  },
  strict: true
})

export default store
