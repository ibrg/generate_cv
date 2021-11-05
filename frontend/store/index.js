import axios from 'axios'

// holds your root state
export const state = () => ({
  cv_list: []
})

// contains your actions
export const actions = {
  createCV ({ commit }, data) {
    axios.post('http://localhost:8000/api/cv_list/', data)
  },
  async loadCV ({ commit }) {
    try {
      await axios.get('http://localhost:8000/api/cv_list/')
        .then((response) => {
          commit('setCV', response.data)
        })
    } catch (error) {
      // TODO: return error to template
    }
  }
}

// contains your mutations
export const mutations = {
  CREATE_CV (state, data) {
    state.cv_list = data
  },
  setCV (state, value) {
    state.cv_list = value
  }
}

// your root getters
export const getters = {
  getCV (state) { return state.cv_list }
}
