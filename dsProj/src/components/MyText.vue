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
  action="https://jsonplaceholder.typicode.com/posts/"
  multiple>
  <i class="el-icon-upload"></i>
  <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em>
  <br>只能上传xxx文件，且不超过xxxkb
  </div>
  <div class="el-upload__tip" slot="tip"></div>
</el-upload>


 </div>
   <!--    清除浮动-->
    <div style="clear: both">

    </div>
  </div>

</template>

<script>
export default {
  name: "MyText",
  data(){
    return{
      Case:""
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
