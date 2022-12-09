<template>
  <div class="affix-container">
    <el-affix target=".affix-container">
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        @select="handleSelect"
      >
        <el-menu-item index="1">
          <router-link to='/home'>Housing Analysis</router-link>
        </el-menu-item>
        <el-menu-item index="2">
          <router-link to='/review_analysis'>Reviews Analysis</router-link>
        </el-menu-item>
        <el-menu-item index="3">Advanced Features</el-menu-item>
      </el-menu>
    </el-affix>
    <router-view></router-view>
  <!-- <Home msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// import theHome from './views/Home.vue'
import { ref } from 'vue'

export default {
  name: 'App',
  data() {
    return {
      activeIndex : ref('1'),

    };
  },
  components: {
    // theHome
  },
  methods: {
    handleSelect(key, keyPath) {
      if(key==1){
        this.$router.push('/home')
      }
      if(key==2){
        this.$router.push('/review_analysis')
      }
      console.log(key, keyPath);
    },
  },
}
</script>

<style>
.affix-container{
 margin:0; 
 padding:0
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body { margin: 0; padding:0}
</style>
