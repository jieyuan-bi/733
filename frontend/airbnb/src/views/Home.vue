<template>
    <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Correlation between bedrooms_num, beds_num and accommodates</h2>
      </div>
    </template>
    <corela_rooms_beds_accommodates/>
  </el-card>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Price Distribution by BedRooms_number</h2>
      </div>
    </template>
    <price_numberOfBedRoom/>
  </el-card>
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <h2>Average Price by having License(1) or not(0)</h2>
      </div>
    </template>
    <avg_price_license/>
  </el-card>
</template>

<script>
import corela_rooms_beds_accommodates from '../components/chart/corela_rooms_beds_accommodates';
import price_numberOfBedRoom from '../components/chart/price_numberOfBedRoom';
import avg_price_license from '../components/chart/avg_price_license';



export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components: {
    corela_rooms_beds_accommodates,
    price_numberOfBedRoom,
    avg_price_license,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.box-card{
  margin:5%
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
