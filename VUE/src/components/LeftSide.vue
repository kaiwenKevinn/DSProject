<template>
<!-- min-height  最小高度  100vh是整个视图的框架 -->
  <div style="background: #eee8d8;border-radius:4px; border: 3px solid #e9453b">
    <el-row class="tac">
      <el-col style="width:230px">
        <div style="border-bottom:3px solid #e9453b">
        <h5 style="text-align: center;font-size:30px;font-family: 'Microsoft YaHei'; color: #606266">导航栏</h5>
        </div>
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            background-color="##eee8d8"
            text-color="#fff"
            active-text-color="#000000"
        >
          <div class="menuItem">
          <el-menu-item  index="2">

            <span slot="title">自动标注</span>
          </el-menu-item>
          </div>

          <div class="menuItem">
          <el-menu-item index="3" >
<!--            <i class="el-icon-document"></i>-->
            <span slot="title">相似案例推荐</span>
          </el-menu-item>
          </div>
            <div class="menuItem">
          <el-menu-item index="4">
<!--            <i class="el-icon-setting"></i>-->
            <span slot="title">罪名推测</span>
          </el-menu-item>
            </div>
        </el-menu>
      </el-col>
    </el-row>
  </div>

</template>

<script>
export default {
  name: "LeftSide",
  data(){
    return{

    }
  },
  methods:{
    handleOpen(){

    },
    handleClose(){

    }
  }
}
</script>

<style scoped>
  span{
    text-align: center ;
    font-size:20px;
    font-family: 'Microsoft YaHei';
  }
  .menuItem{
    border-bottom:#e9453b 3px solid;
  }
</style>