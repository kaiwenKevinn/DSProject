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
  props:["items","eachtitle"],
  methods:{
    sendBack() {
      let param={
        eachtitle:this.eachtitle,
        checkedArray:this.checkedArray
      }
      this.$store.commit('UPDATE',param)
    }
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

  watch:{
    items:{
      handler(news, olds)
      {
        if (this.items){
          if (this.eachtitle === "相关法院:" || this.eachtitle === "案由:"){
            // console.log("if case")
            for (var item in this.items){
              this.checkedArray.push(this.items[item])
            }
            this.sendBack()
          }
          else{
            // console.log("else case")
            this.checkedArray.push(this.items[0])
            this.sendBack()
          }
          // console.log(this.checkedArray)
        }
      }
    }
  }

}
</script>

<style scoped>
.item{
  background: antiquewhite;
  height: 70px;
  margin-left: 250px;
  margin-top: 8px;
  width: 800px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
}
.title{
  margin-top: 10px;
  margin-bottom: 3px;
  margin-left: 10px;
}
.biggest{
  position: relative;
}

</style>
