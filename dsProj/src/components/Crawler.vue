<template>

  <div class="whole">
    <!--    输入框 输入爬虫参数-->
    <div class="block">
     <span class="demonstration">请输入想要查询的判决文书的时间</span>
     <el-date-picker
      v-model="value2"
      type="datetimerange"
      :picker-options="pickerOptions"
      range-separator="至"
      start-placeholder="开始日期"
      end-placeholder="结束日期"
      align="right">
    </el-date-picker>

    </div >

       <!--    开始爬取案钮-->
    <div class="MyButton">
    <el-row>
      <el-button icon="el-icon-search" type="primary" circle @click="Crawling"></el-button>
    </el-row>
   </div>

      <!--    清除浮动-->
    <div style="clear: both">

    </div>
    </div>

</template>

<script>
export default {
  name: "crawler",
  data(){
    return{
      pickerOptions: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
      },
      value2:''
    }
    },
  methods:{
    Crawling(){
      console.log(this.value2)
      if(true) {
        this.$notify({
          title: '成功',
          message: '正在爬取',
          type: 'success'
        });
        this.value2=''
      }
      if(false){
         this.$notify.error({
          title: '成功',
          message: '这是一条成功的提示消息',
        });
      }
    }
  }
}
</script>

<style scoped>
.block{
  float: left;
  margin-left: 250px;
}
.MyButton{
  float: right;
  margin-right: 580px ;
}
.whole{
  background-color: #eee8d8;
}
</style>
