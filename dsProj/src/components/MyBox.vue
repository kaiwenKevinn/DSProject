<template>
  <div>
    <div class="analyze">
          <el-button type="primary" :loading="analysisStatus" @click="load">点击加载</el-button>
      </div>

     <div class="Item">
        <MyItem :items="name" :eachtitle="'姓名:'"/>
        <MyItem :items="gender" :eachtitle="'性别:'"/>
        <MyItem :items="ethnicity" :eachtitle="'民族:'"/>
        <MyItem :items="birthPlace" :eachtitle="'出生地:'"/>
        <MyItem :items="causes" :eachtitle="'案由:'"/>
        <MyItem :items="courts" :eachtitle="'相关法院:'"/>
     </div>

  <el-button @click="show">

  </el-button>

  </div >
</template>

<script>
import MyItem from "./MyItem";
const url="http://localhost:9090"
const axios = require('axios').default;
export default {
  name: "MyBox",
   components:{
    MyItem,
  },
  data(){
    return{
        analysisStatus:false,
        name:[],
        gender:[],
        ethnicity:[],
        birthPlace:[],
        causes:[],
        courts:[],
        checked:[

        ]
    }
  },
  methods:{
    load(){
      var that=this
      axios.get(url+'/search', {
                params: {
                  // ID: 12345
                }
              })
              .then(function (response) {
                // console.log(response)
                that.analysisStatus = true
                that.name=response.data["name"]
                that.causes=response.data["causes"]
                that.courts=response.data["courts"]
                that.gender=response.data["gender"]
                that.ethnicity=response.data["ethnicity"]
                that.birthPlace=response.data["birthplace"]
              })
              .catch(function (error) {
                console.log(error);
              })
              .then(function () {
                setTimeout(()=>{
                      that.analysisStatus=false
                      // console.log(that.analysisStatus)
                    },2000)
              });


    }
    ,
    beforeCreate(){
      this.$bus.$on('please',(data)=>{
        console.log(data)
      })
    },
    show(){
      this.checked.push(1)
      this.$bus.$emit('please','lastTime')
    },
    beforeDestroy (){
      this.$bus.$off('FromItem')
    }

  }

}
</script>

<style scoped>
 .analyze{
   margin-left: 250px;
   position: relative;
 }

</style>
