<template>
<div>
   <el-checkbox-group
    v-model="checkedArray"
    :min="1"
    :max="3">
    <el-checkbox v-for="item in items" :label="item" :key="item.id">{{item.name}}</el-checkbox>
  </el-checkbox-group>
</div>
</template>

<script>
export default {
  name: "MyItem",
  data(){
    return{
      checkedArray:[],
    }
  },
  props:["items"]
}
</script>

<style scoped>

</style>
