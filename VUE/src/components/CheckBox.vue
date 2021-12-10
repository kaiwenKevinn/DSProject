<template>

  <div style="margin: 5px 0;">{{title}}</div>
  <el-checkbox-group   >
    <el-checkbox v-for="people in Array"  :key="people.id"  :label="people" >{{people.name}}</el-checkbox>
  </el-checkbox-group>


</template>

<script>
export default {
  name: "CheckBox",
  props:['title','checkedArray','Array'],
  data(){
    return{

    }
  },
  mounted(){
    console.log(this.checkedArray)
    console.log(this.Array)
  },

  created(){

  },

  methods:{

  },
}
</script>

<style scoped>

</style>