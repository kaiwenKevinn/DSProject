<template>
  <div>

     <div class="Item">
        <MyItem  :items="property.name" :eachtitle="'姓名:'"/>
        <MyItem  :items="property.gender" :eachtitle="'性别:'"/>
        <MyItem  :items="property.ethnicity" :eachtitle="'民族:'"/>
        <MyItem  :items="property.birthPlace" :eachtitle="'出生地:'"/>
        <MyItem  :items="property.causes" :eachtitle="'案由:'"/>
        <MyItem :items="property.courts" :eachtitle="'相关法院:'"/>
     </div>

      <div class="Down">
          <el-button type="primary" :loading="dowloadingStatus" @click="download">下载案例与标注</el-button>
      </div>
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
        checkedClear:false,
        analysisStatus:false,
        dowloadingStatus:false,
    }
  },
  computed:{
    property(){
      return this.$store.state.result
    }
  },
  methods:{
    load(){
      this.$store.dispatch('getDivision')
      this.analysisStatus=true
      setTimeout(()=>{
                      this.analysisStatus=false
                      // console.log(that.analysisStatus)
                    },3000)

    },

    download(){
      this.$store.dispatch('downLoadAnnotation')

      // this.$store.commit("CLEARANNOTATION")
      this.checkedClear=true

       setTimeout(()=>{
                    // this.checkedClear=false
                      this.$notify({
                    title: '成功',
                    message: '案例与标注已下载成功，请前往FILES目录查看',
                    type: 'success',
                     duration:5000
                    });
                    },200)

    },
    }


}
</script>

<style scoped>
 /*.analyze{*/
 /*  margin-left: 250px;*/
 /*  margin-top: -40px;*/
 /*  !*position: relative;*!*/
 /*      display: inline-block;*/
 /*}*/
.Down{
   margin-top: 30px;
   margin-left: 250px;
}
</style>
