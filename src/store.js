import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: JSON.parse(localStorage.getItem('user')),
  },
  mutations: {
    SET_USER (state, payload) {
      state.user = payload
      localStorage.setItem('user', JSON.stringify({ _id: state.user._id, name: state.user.name }))
    },
  },
  actions: {
  },
})
