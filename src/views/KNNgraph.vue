<template>

    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>KNN Graph</h2>
      </div>
    </template>

    <img alt="image load failed" src="../img/yixian1.png" style="width:80%"/>

      <div>
      <el-popover
        placement="bottom"
        :width="600"
        trigger="click"
        content="The graph is about categorizing product titles on knn-Clustering. The product titles is vectorized by GloVe model and transferred to 2D dimension using PCA, and it represent of the position of one point on the graph. The knn-means clustering categorizing the points into different parts. (For the sample graph it  categorizing the points into 6 parts)."
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
  name: 'KNNgraph',
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
