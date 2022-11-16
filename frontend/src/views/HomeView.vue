<template>
  <div class="home">
  <el-backtop target=".page-component__scroll .el-scrollbar__wrap"></el-backtop>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <el-container>
      <el-header>
        <el-row>
          <h1>Temperature changes in 1000 cities during the past 40 years</h1>
        </el-row>
      </el-header>
      <el-main>
        <el-row style="height: 4rem;">
          <template>
            <!-- <h4 class="demonstration">Time Selection</h4> -->
            <el-col :span="16" :offset="4">
              <el-slider
                v-model="value"
                :step="2.5"
                range
                :show-tooltip="true"
                :marks="marks">
              </el-slider>
            </el-col>
          </template>
          <template>
            <el-button type="text" @click="dialogFormVisible = true">
              <el-link type="primary">+ Filters</el-link>
            </el-button>
            <el-dialog title="Filters" :visible.sync="dialogFormVisible">
              <el-form :model="form">
                <el-form-item label="Selection1" :label-width="formLabelWidth">
                  <el-select v-model="form.region" placeholder="Please Select">
                    <el-option label="shanghai" value="shanghai"></el-option>
                    <el-option label="beijing" value="beijing"></el-option>
                  </el-select>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">Cancel</el-button>
                <el-button type="primary" @click="dialogFormVisible = false">Confirm</el-button>
              </div>
            </el-dialog>
          </template>
        </el-row>
          <!-- <Earth/> -->
        <el-row>
          <el-col span="6" offset="2">
            <template>
              <el-radio-group v-model="tabPosition" style="transform:scale(0.75)">
                <el-radio-button label="tempture">Tempture</el-radio-button>
                <el-radio-button label="co2">CO2 Emission</el-radio-button>
              </el-radio-group>
            </template>
          </el-col>
        </el-row>
        <el-row style="height: 550px;">
          <el-col span="20" offset ="2">
            <iframe src="interactive_earth.html" frameborder="0"
            onload="this.height=550" width="100%" height="100%"></iframe>
          </el-col>
        </el-row>

        <el-row style="height: 740px;">

          <el-col span="12" offset="0">
            <el-row style="height:380px;">
              <ScatterPlot/>
            </el-row>
            <el-row style="height:300px">
              <Linegraph/>
            </el-row>
          </el-col>

          <el-col span="12">
            <iframe src="heatmap.html" frameborder="0"
            onload="this.height=740" width="500px" height="100%"></iframe>
          </el-col>

        </el-row>
      </el-main>
      <!-- <el-footer>Footer</el-footer> -->
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Linegraph from '@/components/linegraph.vue'
import ScatterPlot from "@/components/ScatterPlot";
import LinePlot from "@/components/LinePlot";

export default {
  name: 'HomeView',
  components: {
    Linegraph,
    ScatterPlot, 
    LinePlot,
  },
  data() {
      return {
        value: [0, 100],
        marks: {
          0: '1980',
          25: '1990',
          50: {
            style: {
              color: '#1989FA'
            },
            label: this.$createElement('strong', '2000')
          },
          75: '2010',
          100: '2020'
        },
        dialogTableVisible: false,
        dialogFormVisible: false,
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        formLabelWidth: '120px',
        earthUrl: "../components/earth.html",
        tabPosition: 'tempture',
      }
    }
}
</script>
