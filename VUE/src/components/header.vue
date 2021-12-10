<template>
  <div style="position: relative">
    <div style="height: 360px; line-height: 50px;display: flex; border-bottom: gray solid 1px; background: #eee8d8" >
  <div style="margin-left:20px ;height:100% ;font-size:20px ">
    2021年12月8日
  </div>
      <div style="flex: 20  ;height:100% ;font-size:20px " >
      </div>

      <div style="margin-right: 20px ;">
        <el-dropdown>
    <span class="el-dropdown-link" style="font-size:20px">
      {{username}}
      <el-icon class="el-icon--right">
        <arrow-down />
      </el-icon>
    </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item>设置</el-dropdown-item>
              <el-dropdown-item>退出</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>

    <div style=" background: #eee8d8 ;position:absolute ;top: 10px">
      
      <img src="https://s4.ax1x.com/2021/12/08/oRWkp4.png" alt="oRWkp4.png" border="0" style="margin-left:240px;" />
      <!-- java代码注释快捷键：ctrl+/       -->
    </div >
  </div>
<div style="">

</div>
</template>

<script>
import { ArrowDown } from '@element-plus/icons'
export default {
  name: "header",
  data() {
     return{
         username: "张三"
     }
  }

}

</script>

<style scoped>

</style>