<template>
  <GChart
    type="BarChart"
    :data="chartData"
    :options="chartOptions"
  />
</template>


<script>
import axios from "axios";
import { GChart } from 'vue-google-charts'

export default {
  name: "corela_rooms_beds_accommodates",
  data() {
    return {
      chartData:[],
      chartOptions: {
        
          // title: 'Correlation between bedrooms_num, beds_num and accommodates',
          hAxis: {
            title: 'Correlation',
            minValue: 0,
          },
          height: 400,
          colors: ['#43D7FF']
        
      }
    };
  },
  components: {
    GChart,
  },
  methods: {
      init_data(){
        axios
        .get("/api/corela_rooms_beds_accommodates")
        .then((response) => {
          var response_data = response.data;
          var graph_data = [['','correlation'],
            ['bedrooms and beds',response_data[0].beds],
            ['bedrooms and accommodates',response_data[0].accommodates],
            ['beds and accommodates',response_data[1].accommodates],
          ]
          this.chartData = graph_data
        })
        .catch((error) => {
          console.log(error);
        });
        // console.log('complete_init')
      }
  },
  mounted() {
    this.init_data();
  },
};
</script>

<style rel="stylesheet/scss" lang="scss">
</style>