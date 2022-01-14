<template>
  <div>
     <div class="Item">
        <MyItem />
        <MyItem/>
        <MyItem/>
        <MyItem/>
        <MyItem/>
        <MyItem/>
     </div>

      <div class="analyze">
          <el-button type="primary" :loading="analysisStatus" @click="load">加载中</el-button>
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
        analysisStatus:false,
        criminal:[],
        sex:[],
        ethnicity:[],
        birthPlace:[],
        cause:[],
        court:[]
    }
  },
  methods:{
    load(){
      axios.get(url+'/user', {
                params: {
                  ID: 12345
                }
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              })
              .then(function () {
                // 总是会执行
              });
    }
  }

}
</script>

<style scoped>

</style>
