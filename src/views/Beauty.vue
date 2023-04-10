<template>

  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Title</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/tony1.png" style="width:80%"/>

      <div>
      <el-popover
        placement="bottom"
        :width="600"
        trigger="click"
        content="Star rating distribution, more than 40% is 5 star rating, and 25% is 1 star rating."
      >
        <template #reference>
          <el-button class="m-2">Graph description</el-button>
        </template>
      </el-popover>
      </div>
    </el-card>


    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Title</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/tony2.png" style="width:80%"/>

      <div>
      <el-popover
        placement="bottom"
        :width="600"
        trigger="click"
        content="Star rating distribution, more than 40% is 5 star rating, and 25% is 1 star rating."
      >
        <template #reference>
          <el-button class="m-2">Graph description</el-button>
        </template>
      </el-popover>
      </div>
    </el-card>

</template>

<script>



export default {
  name: 'theBeauty',
  props: {
    msg: String
  },
  components: {
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box-card{
  margin:5% 10%
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
