<template>
<div>
<div class="CaseText">
  <el-input
  type="textarea"
  :autosize="{ minRows:8, maxRows: 100}"
  placeholder="请输入或点击案钮上传判决文书"
   size="medium"
  v-model="Case">
</el-input>
</div>

 <div class="Upload">


   <el-upload
  class="upload-demo"
  drag
  action="http://localhost:9090/download"
  :on-exceed="exceed"
  :limit="1"
  multiple>
  <i class="el-icon-upload"></i>
  <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em>
  <br>只能上传txt文件，且不超过xxxkb
  </div>
  <div class="el-upload__tip" slot="tip"></div>
</el-upload>


 </div>
  <div class="emitButton">
    <el-button type="primary" :loading="analyzeStatus" @click="analyze">分析上传的文件</el-button>
  </div>
   <!--    清除浮动-->
    <div style="clear: both">

    </div>
  </div>

</template>

<script>
const url="http://localhost:9090"
export default {
  name: "MyText",
  data(){
    return{
      Case:"",
      analyzeStatus:false,
    }
  },
  methods:{
    exceed(){
      console.log("超出数量限制")
      this.$alert('超出文件数量限制', '提示', {
          confirmButtonText: '确定',
        });
    },
    analyze(){
      var that=this
    }
  }
}
</script>

<style scoped>
.CaseText{
    width: 800px;
    margin-left: 250px;
    margin-top: 10px;
    float: left;
}
.Upload{
  float: right;
  margin-top: 10px;
  margin-right: 90px;
}
</style>
