<template>
  <div class="biggest">
         <div class="item">
                <div class="title">
                  {{eachtitle}}
                </div>

              <div style="margin-left: 5px">
               <el-checkbox-group @change="sendBack"
                v-model="checkedArray">
                <el-checkbox-button v-for="item in items" :label="item" :key="item.id">{{item}}</el-checkbox-button>
              </el-checkbox-group>
              </div>

          </div>

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
  props:["items","eachtitle","status"],
  methods:{
    sendBack() {
      let param={
        eachtitle:this.eachtitle,
        checkedArray:this.checkedArray
      }
      this.$store.commit('UPDATE',param)
    },


  },

  updated() {
    var that=this
    this.$nextTick(
      ()=>{
          if(that.status===true){
            that.checkedArray=[]
          }
      }
    )
  },

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

</style>
