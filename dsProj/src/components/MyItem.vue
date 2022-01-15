<template>
  <div class="biggest">
         <div class="item">
                <div class="title">
                  {{eachtitle}}
                </div>

              <div style="margin-left: 5px">
               <el-checkbox-group
                v-model="checkedArray">
                <el-checkbox-button v-for="item in items" :label="item" :key="item.id">{{item}}</el-checkbox-button>
              </el-checkbox-group>
              </div>

          </div>
      <div class="sendBack" >
          <el-button type="success" icon="el-icon-check" circle @click="sendBack"></el-button>
      </div>
    </div>

</template>

<script>
export default {
  name: "MyItem",
  data(){
    return{
      checkedArray:[],
      thelast:false
    }
  },
  props:["items","eachtitle"],
  methods:{
    sendBack() {
      this.$nextTick(function (){
        this.$bus.$emit('please','this.checkedArray')
      })

    },
    touch(){
    this.$nextTick(function (){
        this.$bus.$emit('please','this.checkedArray')
      })
    }

  },
   // updated:function () {
   //    // console.log('updated'+this.eachtitle)
   //   // console.log(this.checkedArray)
   //
   //   // console.log(this.$bus)
   // },

}
</script>

<style scoped>
.item{

  margin-left: 250px;
  margin-top: 8px;
  width: 800px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
}
.title{
  margin-bottom: 3px;
  margin-left: 5px;
}
.biggest{
  position: relative;
}
 .sendBack{
   position: absolute;
   right: 400px;
   bottom: 8px;
 }
</style>
