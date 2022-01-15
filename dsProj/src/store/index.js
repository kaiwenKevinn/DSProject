import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state={
  checkedName:[],
  checkedEthnicity:[],
  checkedGender:[],
  checkedCourts:[],
  checkedCauses:[],
  checkedBirthPlace:[]
}


const mutations = {
  UPDATE(state,param){
    let title=param.eachtitle
    let array=param.checkedArray
    if(title==="姓名:"){
      state.checkedName=array
    }
    if(title==="性别:"){
      state.checkedGender=array
    }
    if(title==="民族:"){
      state.checkedEthnicity=array
    }
    if(title==="出生地:"){
      state.checkedBirthPlace=array
    }
    if(title==="案由:"){
      state.checkedCauses=array
    }
    if(title==="相关法院:"){
      state.checkedCourts=array
    }
  }

}
const actions = {

}
export default  new Vuex.Store({
  state: state,
  mutations: mutations,
  actions: actions,
})
