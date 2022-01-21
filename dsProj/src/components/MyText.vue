<template>
<div style="position: relative">
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
  action="http://localhost:9090/download/upload"
  :on-exceed="exceed"
  :limit="1"
  multiple>
  <i class="el-icon-upload"></i>
  <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em>
  <br>只能上传txt文件
  </div>
  <div class="el-upload__tip" slot="tip"></div>
</el-upload>


 </div>

<div style="clear: both"></div>

 <div class="emitButton">
    <el-button type="primary" :loading="uploadStatus" @click="analyze">分析上传的文件</el-button>
  </div>
  <div class="analyze">
          <el-button type="primary" :loading="analysisStatus" @click="load">分析输入的文书</el-button>
    </div>
   <!--    清除浮动-->


<div style="clear: both"></div>
</div>

</template>

<script>
const url="http://localhost:9090"
export default {
  name: "MyText",
  data(){
    return{
      Case:"",
      uploadStatus:false,
      analysisStatus:false,
    }
  },
  computed:{
    textToFillTheCase(){
      return this.$store.state.result.textFromUpload
    }
  },
  methods:{
    exceed(){
      console.log("超出数量限制")
      this.$alert('超出文件数量限制', '提示', {
          confirmButtonText: '确定',
        });
    },
    // todo "sendText"
    load(){
      this.$store.commit("sendText",this.Case)
      this.$store.dispatch('getDivision')
      this.analysisStatus=true
      setTimeout(()=>{
                      this.analysisStatus=false
                      // console.log(that.analysisStatus)
                    },3000)

    },

    analyze(){
      this.uploadStatus=true
      this.$store.dispatch("getResultFromUpload")
      this.Case=this.textToFillTheCase

      setTimeout(()=>{
                      this.uploadStatus=false
                      // console.log(that.analysisStatus)
                    },3000)
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
.emitButton{

   margin-top: 10px;
   float: right;
    margin-right:500px ;
   display: inline-block;
}
 .analyze{
   margin-left: 250px;
   margin-top: 10px;
   float: left;
   display: inline-block;
 }
</style>
