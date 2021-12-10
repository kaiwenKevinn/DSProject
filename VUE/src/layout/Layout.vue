<template>
  <div>

    <!--  头部-->
    <Header></Header>

    <div style="display:flex;">
      <!--  导航栏 -->
      <LeftSide > </LeftSide>
      <!--主体部分-->
      <router-view style="flex: 1" @userInfo="refreshUser"/>

    </div>




  </div>

</template>

<script>
import Header from "@/components/header";
import LeftSide from "@/components/LeftSide";

export default{
  name:"Layout",
  components:{
    Header,LeftSide
  }
}
</script>

<style>

</style>
