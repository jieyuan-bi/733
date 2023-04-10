<template>

    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Number of reviews evolved over years</h2>
      </div>
      <img alt="image load failed" src="../img/kelvin1.png" style="width:100%"/>

      <div>
      <el-popover
        placement="bottom"
        :width="600"
        trigger="click"
        content="The number of reviews have evolved over years jump exponentially"
      >
        <template #reference>
          <el-button class="m-2">Graph description</el-button>
        </template>
      </el-popover>
      </div>

      </template>
    </el-card>

    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Star Rating Distribution</h2>
      </div>
      <img alt="image load failed" src="../img/kelvin2.png" style="width:100%"/>

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

      </template>
    </el-card>

    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Vote Ratio Distribution by Star Rating</h2>
      </div>
      <img alt="image load failed" src="../img/kelvin3.png" style="width:100%"/>

      <div>
      <el-popover
        placement="bottom"
        :width="600"
        trigger="click"
        content="vote_ratio distribution by star rating. More than half of reviews with 5 star rating or 4 star rating have 90% helpfulness vote ratio."
      >
        <template #reference>
          <el-button class="m-2">Graph description</el-button>
        </template>
      </el-popover>
      </div>

      </template>
    </el-card>

    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Vote Ratio Distribution by Sentence_count</h2>
      </div>
      <img alt="image load failed" src="../img/kelvin4.png" style="width:100%"/>

      <div>
      <el-popover
        placement="bottom"
        :width="600"
        trigger="click"
        content="vote_ratio distribution by sentence_count. Most of the reviews which has more than 20 sentences have 80% helpfulness vote ratio"
      >
        <template #reference>
          <el-button class="m-2">Graph description</el-button>
        </template>
      </el-popover>
      </div>

      </template>
    </el-card>


</template>

<script>
// import corela_rooms_beds_accommodates from '../components/chart/corela_rooms_beds_accommodates';
// import price_numberOfBedRoom from '../components/chart/price_numberOfBedRoom';
// import avg_price_license from '../components/chart/avg_price_license';
// import priceWithMonth from '../components/chart/priceWithMonth';
// import priceWithWeek from '../components/chart/priceWithWeek';
// import priceWithSpace from '../components/chart/priceWithSpace';
// import priceWithType from '../components/chart/priceWithType';




export default {
  name: 'theHome',
  props: {
    msg: String
  },
  components: {
    // corela_rooms_beds_accommodates,
    // price_numberOfBedRoom,
    // avg_price_license,
    // priceWithMonth,
    // priceWithWeek,
    // priceWithSpace,
    // priceWithType,

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
