<template>
  <el-button text @click="centerDialogVisible = true" style="margin-top: 20px;">
      Dataset Preview
    </el-button>

    <el-dialog v-model="centerDialogVisible" title="Preview" width="70%" center>
      <img alt="image load failed" src="../img/preview_pc.jpg" style="width:100%"/>
    </el-dialog>

    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Distribution of Polarity Score</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/bai1.png" style="width:80%"/>

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
        <h2>Polarity Score Distribution by Ratings</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/bai2.png" style="width:80%"/>

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
        <h2>Top 20 most frequent unigrams in reviews</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/bai3.png" style="width:80%"/>

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
        <h2>Top 20 most frequent bigrams in reviews</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/bai4.png" style="width:80%"/>

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
        <h2>Top 20 most frequent trigrams in reviews</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/bai5.png" style="width:80%"/>

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
  name: 'PCadv',
  data() {
    return {
      centerDialogVisible: false,

    };
  },
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
