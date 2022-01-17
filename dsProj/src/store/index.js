import Vue from 'vue'
import Vuex from 'vuex'
import {default as axios} from "axios";


Vue.use(Vuex)
const url="http://localhost:9090"
const state={

  checked:{

  },
  myText:"",
  result:{}
}


const mutations = {
  UPDATE(state,param){
    let title=param.eachtitle
    let array=param.checkedArray
    if(title==="姓名:"){
      state.checked.checkedName=array
    }
    if(title==="性别:"){
      state.checked.checkedGender=array
    }
    if(title==="民族:"){
      state.checked.checkedEthnicity=array
    }
    if(title==="出生地:"){
      state.checked.checkedBirthPlace=array
    }
    if(title==="案由:"){
      state.checked.checkedCauses=array
    }
    if(title==="相关法院:"){
      state.checked.checkedCourts=array
    }
  },
  sendText(state,input){
    state.myText=input
  },
  CLEARANNOTATION(state){
    state.checked={}
  },
  RENDER(state,obj){
    state.result=obj
  }
}
const actions = {
  getDivision(context){
      var that=this
      var obj
      axios.post(url+'/search/text', {
        input:context.state.myText
              })
              .then(function (response) {
                // var analysisStatus = true
                var name=response.data["name"]
                var causes=response.data["causes"]
                var courts=response.data["courts"]
                var gender=response.data["gender"]
                var ethnicity=response.data["ethnicity"]
                var birthPlace=response.data["birthplace"]
                obj={
                  "name":name,
                  "causes":causes,
                  "courts":courts,
                  "gender":gender,
                  "ethnicity":ethnicity,
                  "birthPlace":birthPlace
                }
              })
              .catch(function (error) {
                console.log(error);
              })
              .then(function () {
                // 总是会执行
                context.commit('RENDER',obj)
              });
  },

  getResultFromUpload(context){
    var obj
    axios.post(url+'/analyze/upload', {
              })
              .then(function (response) {
                // var analysisStatus = true
                var name=response.data["name"]
                var causes=response.data["causes"]
                var courts=response.data["courts"]
                var gender=response.data["gender"]
                var ethnicity=response.data["ethnicity"]
                var birthPlace=response.data["birthplace"]
                obj={
                  "name":name,
                  "causes":causes,
                  "courts":courts,
                  "gender":gender,
                  "ethnicity":ethnicity,
                  "birthPlace":birthPlace
                }
              })
              .catch(function (error) {
                console.log(error);
              })
              .then(function () {
                // 总是会执行
                context.commit('RENDER',obj)
              });
  },

  downLoadAnnotation(context){
    var that=this

     axios.post(url+'/download/annotation', {
        annotation:context.state.checked
              })
              .then(function (response) {
                // var analysisStatus = true
                  if(response.status===200){
                    alert("标注下载成功")
                  }
              })
              .catch(function (error) {
                console.log(error);
              })
              .then(function () {
                // 总是会执行
              });
  }
}
export default  new Vuex.Store({
  state: state,
  mutations: mutations,
  actions: actions,
})
