<template>
<div class="father">
  <Header></Header>
  <Crawler></Crawler>
  <MyText></MyText>
  <MyBox></MyBox>
</div>
</template>

<script >
import Header from "./components/Header"
import Crawler from "./components/Crawler";
import MyText from "./components/MyText";
import MyBox from "./components/MyBox";
const url="http://localhost:9090"
export default{
  name: 'App',
  components:{Header,Crawler,MyText,MyBox}
}
</script>
<style scoped>
 .father{
   background: #eee8d8;
   position: relative;
   height: 100%;
 }
</style>
