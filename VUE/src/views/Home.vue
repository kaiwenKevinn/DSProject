<template>
  <div style="padding: 20px; background: #eee8d8" >

<!--    输入框 输入爬虫参数-->
    <el-form  :inline="true" :model="formInline" class="demo-form-inline">
      <el-form-item label="开始日期">
        <el-date-picker
            v-model="formInline.date"
            type="datetimerange"
            range-separator="To"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
        >
        </el-date-picker>
      </el-form-item>
      <el-form-item>
        <el-input type="number" v-model.number="formInline.num" placeholder="份数">

        </el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="beginPaqu">开始下载</el-button>
      </el-form-item>
    </el-form>

    <el-button type="primary">上传案例文件</el-button>
    <el-form  style="padding: 10px"  :model="formFiles" >
      <el-input
          v-model="formFiles.text"
          :rows="2"
          :autosize="{ minRows: 10}"
          type="textarea"
          placeholder="请输入或上传文件"
          style="width: 80%"
      />
    </el-form>

  <div class="boxBorder" >

    <div style="margin: 5px 0;">人名</div>
    <el-checkbox-group  v-model="checkedPeople" @change="handleCheckedPeopleChange">
      <el-checkbox v-for="people in People" :label="people"   value="people.name" >{{people.name}}</el-checkbox>
    </el-checkbox-group>

    <div style="margin: 5px 0;">性别</div>
    <el-checkbox-group v-model="checkedSex" @change="handleCheckedSexChange">
      <el-checkbox v-for="sex in Sex" :label="sex" >{{sex.name}}</el-checkbox>
    </el-checkbox-group>



    <div style="margin: 5px 0;">案由</div>
    <el-checkbox-group v-model="checkedReason" @change="handleCheckedReasonChange">
      <el-checkbox v-for="reason in Reason" :label="reason" >{{reason.text}}</el-checkbox>
    </el-checkbox-group>

    <CheckBox title="实验" :checkedArray="checkedPeople" :Array="People">
    </CheckBox>


  </div>
    <el-button type="primary">下载案例与标注</el-button>
  </div>




</template>

<script>
// @ is an alias to /src
import request from "@/utils/request";
import CheckBox from "@/components/CheckBox";


export default {
  name: 'Home',

  data(){
    return{
      dialogFormVisible:false,
      tableData:[],
      formInline: {
          num:'',
        date:'',
    },
      formFiles:{
        text:'',
      },
      People:[{
        name:'张三',
        id:'1',

      },
        {
          name:'王五',
          id:'2'
        },
        {
          name:'hh',
          id:'3'
        },
        {
          name:'李四',
          id:'4'
        }],
      Sex:[{
        name:'男',
        id:'1'
      },{
        name:'女',
        id:'2'
    }],
      Reason:[{
        text:'抢劫',
        id:'1'
      },
      {
          text:'偷盗',
          id:'2'
              },
      {
         text:'绑架',
          id:'3'
              },
        ],
      checkedPeople: [],
      checkedSex:[],
      checkedReason:[],

  }
    },
  created() {
    // this.load()
  },
  methods:{
    handleCheckedPeopleChange(){
      console.log(this.checkedPeople)
    }
  },

  components: {
    CheckBox
  }
}
</script>
<style>

   .boxBorder{
       border:3px solid #e9453b; width:80% ;margin: 10px 0;border-radius: 10px ;padding: 5px
   }
</style>
