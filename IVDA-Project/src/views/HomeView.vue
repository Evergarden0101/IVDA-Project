<template>
    <div class="home">
    <!-- <el-backtop target=".page-component__scroll .el-scrollbar__wrap"></el-backtop> -->
      <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
      <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
      <el-container>
        <el-header>
          <el-row style="margin-top: -1rem;height:1rem">
            <h1>Temperature changes in 1000 cities during the past 40 years</h1>
          </el-row>
        </el-header>
        <el-main>
          <el-row style="height: 4rem; margin-top: -2rem;">
  
            <!-- timeline -->
              <!-- <h4 class="demonstration">Time Selection</h4> -->
            <el-col :span="16" :offset="4">
              <template>
                <!-- <div class="block">
                  <el-slider
                    v-model="value"
                    :step="2.5"
                    range
                    :marks="marks">
                  </el-slider> 
                </div>-->
                <a-slider 
                  range 
                  :min=1980
                  :max=2020
                  :marks="marks" 
                  @afterChange="changeYear"
                  :default-value="[1980, 2020]"
                />
              </template>
            </el-col>
            <!-- filter -->
            <!--
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
            -->
          </el-row>
          <el-row style="height: 2rem;"></el-row>
  
          <el-row style="height: 80vh;">
            <!-- <Earth/> -->
            <el-col :span="16" :offset ="0">
              <!-- layer tab 
              <el-row>
                <el-col :span="8" :offset="0">
                  <template>
                    <el-radio-group v-model="tabPosition" style="transform:scale(0.85)">
                      <el-radio-button label="tempture">Tempture</el-radio-button>
                      <el-radio-button label="co2">CO2 Emission</el-radio-button>
                    </el-radio-group>
                  </template>
                </el-col>
              </el-row>
              -->
              <el-row style="margin-left:25px; ">
                <!-- <earth></earth> -->
                <template>
                  <div id='map'></div>
                </template>
              </el-row>
            </el-col>
            <!-- heatmap -->
            <el-col :span="7" :offset="0" id="globalhtmp" style="display:none">
              <iframe src="/static/heatmap.html" frameborder="0" ref="heatmpfrm" @load=""
              onload="this.height=630" width="420px" height="100%" ></iframe>
              <!-- <div id="my_dataviz" style="overflow-x:hidden"></div> -->
            </el-col>
            <el-col :span="7" :offset="0" id="italyhtmp" style="display:none">
              <iframe src="/static/heatmap1.html" frameborder="0" ref="heatmpfrm" @load=""
              onload="this.height=630" width="420px" height="100%" ></iframe>
            </el-col>
            <el-col :span="7" :offset="0" id="milanhtmp" style="display:none">
              <iframe src="/static/heatmap2.html" frameborder="0" ref="heatmpfrm" @load=""
              onload="this.height=630" width="420px" height="100%" ></iframe>
            </el-col>
          </el-row>
          <template>
          </template>
  
          <el-row>
            <iframe src="/static/interactive_earth.html" frameborder="0"
                onload="this.height=550" width="100%" height="100%"></iframe>
          </el-row>

        <el-row style="margin-left:25px">
            <iframe src="/static/earth.html" frameborder="0" ref="earthfrm" @load=""
            onload="this.height=580" width="100%" height="100%"></iframe>
        </el-row>
  
          <!-- hidden
          <el-row style="height: 740px;">
            <el-col span="12" offset="0">
              <el-row style="height:380px;">
                <ScatterPlot/>
              </el-row>
              <el-row style="height:300px">
                <Linegraph/>
              </el-row>
            </el-col>
          </el-row>
          -->
        </el-main>
        <!-- <el-footer>Footer</el-footer> -->
      </el-container>
    </div>
  </template>
  
<script>
  // @ is an alias to /src
  import Earth from '../components/earth.vue';
  import * as d3 from 'd3';
  export default {
    name: 'HomeView',
    components: {
      Earth,
    },
    data() {
        return {
          value: [1980, 2020],
          marks: {
            1980: {
              style: {
                color: '#1989FA'
              },
              label: this.$createElement('strong', '1980')
            },
            1990: {
              style: {
                color: '#1989FA'
              },
              label: this.$createElement('strong', '1990')
            },
            2000: {
              style: {
                color: '#1989FA'
              },
              label: this.$createElement('strong', '2000')
            },
            2010: {
              style: {
                color: '#1989FA'
              },
              label: this.$createElement('strong', '2010')
            },
            2020: {
              style: {
                color: '#1989FA'
              },
              label: this.$createElement('strong', '2020')
            },
          },
          iearth:"",
          iheatmp:"",
          temp:null,
          placeSelection: null,
          scaleSelection: null,
          startY:1980,
          endY: 2020,
          heatMapMons: [],
          heatMapYears: [],
          htmpcsv: 0,

          // Earth

          corner1: 0,
          corner2: 0,
          bounds: null,
          maxZoom: 4.5,
          minZoom: 1.49,
          map: null,
          scaleControl: null,
          temperature: null,
          CO2: null,
          allOptions: {},
          Tooltip: null,
          info: null,
          legend: null,
          markers: [],
          geojson: null,
          worldData: null,
          worldJson: null,
          cityMarkers : null,
          placeSelection: null,
          scaleSelection: null,
          heatMapList: [{"Mon": 1, "Year": 1980, "Temp": 9.9647822581}, {"Mon": 2, "Year": 1980, "Temp": 11.2115727586}, {"Mon": 3, "Year": 1980, "Temp": 14.1692183871}, {"Mon": 4, "Year": 1980, "Temp": 17.9420146667}, {"Mon": 5, "Year": 1980, "Temp": 21.0720832258}, {"Mon": 6, "Year": 1980, "Temp": 22.9402726667}, {"Mon": 7, "Year": 1980, "Temp": 23.7624854839}, {"Mon": 8, "Year": 1980, "Temp": 23.3751280645}, {"Mon": 9, "Year": 1980, "Temp": 21.5082726667}, {"Mon": 10, "Year": 1980, "Temp": 18.3934580645}, {"Mon": 11, "Year": 1980, "Temp": 15.069785}, {"Mon": 12, "Year": 1980, "Temp": 11.2873580645}, {"Mon": 1, "Year": 1981, "Temp": 9.8572325806}, {"Mon": 2, "Year": 1981, "Temp": 11.8167889286}, {"Mon": 3, "Year": 1981, "Temp": 15.15311}, {"Mon": 4, "Year": 1981, "Temp": 18.3570696667}, {"Mon": 5, "Year": 1981, "Temp": 20.8189164516}, {"Mon": 6, "Year": 1981, "Temp": 23.143208}, {"Mon": 7, "Year": 1981, "Temp": 23.9586558065}, {"Mon": 8, "Year": 1981, "Temp": 23.6607235484}, {"Mon": 9, "Year": 1981, "Temp": 21.544615}, {"Mon": 10, "Year": 1981, "Temp": 18.09098}, {"Mon": 11, "Year": 1981, "Temp": 14.139458}, {"Mon": 12, "Year": 1981, "Temp": 11.3514890323}, {"Mon": 1, "Year": 1982, "Temp": 10.1765658065}, {"Mon": 2, "Year": 1982, "Temp": 11.245865}, {"Mon": 3, "Year": 1982, "Temp": 14.3675393548}, {"Mon": 4, "Year": 1982, "Temp": 17.7952686667}, {"Mon": 5, "Year": 1982, "Temp": 21.1193335484}, {"Mon": 6, "Year": 1982, "Temp": 22.799479}, {"Mon": 7, "Year": 1982, "Temp": 23.9126012903}, {"Mon": 8, "Year": 1982, "Temp": 23.5710187097}, {"Mon": 9, "Year": 1982, "Temp": 21.6935323333}, {"Mon": 10, "Year": 1982, "Temp": 18.7437519355}, {"Mon": 11, "Year": 1982, "Temp": 14.7826733333}, {"Mon": 12, "Year": 1982, "Temp": 11.5622832258}, {"Mon": 1, "Year": 1983, "Temp": 10.6846551613}, {"Mon": 2, "Year": 1983, "Temp": 11.3279260714}, {"Mon": 3, "Year": 1983, "Temp": 14.53924}, {"Mon": 4, "Year": 1983, "Temp": 18.1523233333}, {"Mon": 5, "Year": 1983, "Temp": 21.136913871}, {"Mon": 6, "Year": 1983, "Temp": 22.9693353333}, {"Mon": 7, "Year": 1983, "Temp": 24.242383871}, {"Mon": 8, "Year": 1983, "Temp": 23.834473871}, {"Mon": 9, "Year": 1983, "Temp": 22.013058}, {"Mon": 10, "Year": 1983, "Temp": 18.49528}, {"Mon": 11, "Year": 1983, "Temp": 14.790403}, {"Mon": 12, "Year": 1983, "Temp": 11.1635816129}, {"Mon": 1, "Year": 1984, "Temp": 9.8339632258}, {"Mon": 2, "Year": 1984, "Temp": 10.8271596552}, {"Mon": 3, "Year": 1984, "Temp": 14.1496658065}, {"Mon": 4, "Year": 1984, "Temp": 17.8317096667}, {"Mon": 5, "Year": 1984, "Temp": 20.86898}, {"Mon": 6, "Year": 1984, "Temp": 22.797693}, {"Mon": 7, "Year": 1984, "Temp": 23.7014316129}, {"Mon": 8, "Year": 1984, "Temp": 23.5397609677}, {"Mon": 9, "Year": 1984, "Temp": 21.2122993333}, {"Mon": 10, "Year": 1984, "Temp": 18.5380974194}, {"Mon": 11, "Year": 1984, "Temp": 14.6793116667}, {"Mon": 12, "Year": 1984, "Temp": 10.7872093548}, {"Mon": 1, "Year": 1985, "Temp": 9.4105951613}, {"Mon": 2, "Year": 1985, "Temp": 10.8957078571}, {"Mon": 3, "Year": 1985, "Temp": 14.0232535484}, {"Mon": 4, "Year": 1985, "Temp": 18.2791316667}, {"Mon": 5, "Year": 1985, "Temp": 21.248786129}, {"Mon": 6, "Year": 1985, "Temp": 22.6217416667}, {"Mon": 7, "Year": 1985, "Temp": 23.6929316129}, {"Mon": 8, "Year": 1985, "Temp": 23.744066129}, {"Mon": 9, "Year": 1985, "Temp": 21.462257}, {"Mon": 10, "Year": 1985, "Temp": 18.4696151613}, {"Mon": 11, "Year": 1985, "Temp": 14.4152323333}, {"Mon": 12, "Year": 1985, "Temp": 10.9817077419}, {"Mon": 1, "Year": 1986, "Temp": 10.4428522581}, {"Mon": 2, "Year": 1986, "Temp": 10.6799189286}, {"Mon": 3, "Year": 1986, "Temp": 14.5053851613}, {"Mon": 4, "Year": 1986, "Temp": 18.1961923333}, {"Mon": 5, "Year": 1986, "Temp": 21.1874051613}, {"Mon": 6, "Year": 1986, "Temp": 22.9980346667}, {"Mon": 7, "Year": 1986, "Temp": 23.6708916129}, {"Mon": 8, "Year": 1986, "Temp": 23.5400619355}, {"Mon": 9, "Year": 1986, "Temp": 21.4555476667}, {"Mon": 10, "Year": 1986, "Temp": 18.2580793548}, {"Mon": 11, "Year": 1986, "Temp": 14.3622006667}, {"Mon": 12, "Year": 1986, "Temp": 11.3685267742}, {"Mon": 1, "Year": 1987, "Temp": 10.109213871}, {"Mon": 2, "Year": 1987, "Temp": 12.2247285714}, {"Mon": 3, "Year": 1987, "Temp": 13.9605683871}, {"Mon": 4, "Year": 1987, "Temp": 18.156508}, {"Mon": 5, "Year": 1987, "Temp": 20.9596448387}, {"Mon": 6, "Year": 1987, "Temp": 22.9330946667}, {"Mon": 7, "Year": 1987, "Temp": 24.2374951613}, {"Mon": 8, "Year": 1987, "Temp": 23.8095929032}, {"Mon": 9, "Year": 1987, "Temp": 22.0382156667}, {"Mon": 10, "Year": 1987, "Temp": 18.6207777419}, {"Mon": 11, "Year": 1987, "Temp": 14.782326}, {"Mon": 12, "Year": 1987, "Temp": 11.9600122581}, {"Mon": 1, "Year": 1988, "Temp": 11.0407512903}, {"Mon": 2, "Year": 1988, "Temp": 11.6117041379}, {"Mon": 3, "Year": 1988, "Temp": 14.3045645161}, {"Mon": 4, "Year": 1988, "Temp": 18.2320396667}, {"Mon": 5, "Year": 1988, "Temp": 21.4196467742}, {"Mon": 6, "Year": 1988, "Temp": 23.160912}, {"Mon": 7, "Year": 1988, "Temp": 24.1821477419}, {"Mon": 8, "Year": 1988, "Temp": 23.7775709677}, {"Mon": 9, "Year": 1988, "Temp": 21.730907}, {"Mon": 10, "Year": 1988, "Temp": 18.4732851613}, {"Mon": 11, "Year": 1988, "Temp": 14.3994216667}, {"Mon": 12, "Year": 1988, "Temp": 11.7615258065}, {"Mon": 1, "Year": 1989, "Temp": 10.7351167742}, {"Mon": 2, "Year": 1989, "Temp": 11.7004714286}, {"Mon": 3, "Year": 1989, "Temp": 14.9332783871}, {"Mon": 4, "Year": 1989, "Temp": 18.2980136667}, {"Mon": 5, "Year": 1989, "Temp": 21.1673809677}, {"Mon": 6, "Year": 1989, "Temp": 22.8288453333}, {"Mon": 7, "Year": 1989, "Temp": 23.9290480645}, {"Mon": 8, "Year": 1989, "Temp": 23.6633035484}, {"Mon": 9, "Year": 1989, "Temp": 21.673963}, {"Mon": 10, "Year": 1989, "Temp": 18.7069270968}, {"Mon": 11, "Year": 1989, "Temp": 14.6576756667}, {"Mon": 12, "Year": 1989, "Temp": 11.4573516129}, {"Mon": 1, "Year": 1990, "Temp": 10.8951474194}, {"Mon": 2, "Year": 1990, "Temp": 12.6135778571}, {"Mon": 3, "Year": 1990, "Temp": 15.4857825806}, {"Mon": 4, "Year": 1990, "Temp": 18.17279}, {"Mon": 5, "Year": 1990, "Temp": 20.9897}, {"Mon": 6, "Year": 1990, "Temp": 23.1112503333}, {"Mon": 7, "Year": 1990, "Temp": 23.9830493548}, {"Mon": 8, "Year": 1990, "Temp": 23.9938570968}, {"Mon": 9, "Year": 1990, "Temp": 21.704937}, {"Mon": 10, "Year": 1990, "Temp": 18.9551048387}, {"Mon": 11, "Year": 1990, "Temp": 15.6278126667}, {"Mon": 12, "Year": 1990, "Temp": 11.8725290323}, {"Mon": 1, "Year": 1991, "Temp": 10.6790241935}, {"Mon": 2, "Year": 1991, "Temp": 11.7913946429}, {"Mon": 3, "Year": 1991, "Temp": 14.8771916129}, {"Mon": 4, "Year": 1991, "Temp": 18.2125756667}, {"Mon": 5, "Year": 1991, "Temp": 20.8802283871}, {"Mon": 6, "Year": 1991, "Temp": 23.067719}, {"Mon": 7, "Year": 1991, "Temp": 24.1990632258}, {"Mon": 8, "Year": 1991, "Temp": 23.7843583871}, {"Mon": 9, "Year": 1991, "Temp": 21.8988576667}, {"Mon": 10, "Year": 1991, "Temp": 18.4982670968}, {"Mon": 11, "Year": 1991, "Temp": 14.539526}, {"Mon": 12, "Year": 1991, "Temp": 11.4089712903}, {"Mon": 1, "Year": 1992, "Temp": 10.5442367742}, {"Mon": 2, "Year": 1992, "Temp": 11.9049082759}, {"Mon": 3, "Year": 1992, "Temp": 14.5340858065}, {"Mon": 4, "Year": 1992, "Temp": 18.249889}, {"Mon": 5, "Year": 1992, "Temp": 20.915673871}, {"Mon": 6, "Year": 1992, "Temp": 22.816403}, {"Mon": 7, "Year": 1992, "Temp": 23.7607487097}, {"Mon": 8, "Year": 1992, "Temp": 23.5885451613}, {"Mon": 9, "Year": 1992, "Temp": 21.47183}, {"Mon": 10, "Year": 1992, "Temp": 18.0046058065}, {"Mon": 11, "Year": 1992, "Temp": 14.4777023333}, {"Mon": 12, "Year": 1992, "Temp": 11.6958341935}, {"Mon": 1, "Year": 1993, "Temp": 10.4639783871}, {"Mon": 2, "Year": 1993, "Temp": 11.8005625}, {"Mon": 3, "Year": 1993, "Temp": 14.4191516129}, {"Mon": 4, "Year": 1993, "Temp": 18.1623986667}, {"Mon": 5, "Year": 1993, "Temp": 21.1221309677}, {"Mon": 6, "Year": 1993, "Temp": 23.06616}, {"Mon": 7, "Year": 1993, "Temp": 23.7000451613}, {"Mon": 8, "Year": 1993, "Temp": 23.4817722581}, {"Mon": 9, "Year": 1993, "Temp": 21.4090866667}, {"Mon": 10, "Year": 1993, "Temp": 18.4212067742}, {"Mon": 11, "Year": 1993, "Temp": 14.0770186667}, {"Mon": 12, "Year": 1993, "Temp": 11.7970193548}, {"Mon": 1, "Year": 1994, "Temp": 11.0291929032}, {"Mon": 2, "Year": 1994, "Temp": 11.4836164286}, {"Mon": 3, "Year": 1994, "Temp": 14.8652635484}, {"Mon": 4, "Year": 1994, "Temp": 18.68459}, {"Mon": 5, "Year": 1994, "Temp": 21.4930064516}, {"Mon": 6, "Year": 1994, "Temp": 23.26213}, {"Mon": 7, "Year": 1994, "Temp": 24.4978022581}, {"Mon": 8, "Year": 1994, "Temp": 24.0232619355}, {"Mon": 9, "Year": 1994, "Temp": 21.828856}, {"Mon": 10, "Year": 1994, "Temp": 18.61732}, {"Mon": 11, "Year": 1994, "Temp": 15.647303}, {"Mon": 12, "Year": 1994, "Temp": 12.0005067742}, {"Mon": 1, "Year": 1995, "Temp": 10.881523871}, {"Mon": 2, "Year": 1995, "Temp": 12.6144492857}, {"Mon": 3, "Year": 1995, "Temp": 14.9723616129}, {"Mon": 4, "Year": 1995, "Temp": 18.181933}, {"Mon": 5, "Year": 1995, "Temp": 21.2281319355}, {"Mon": 6, "Year": 1995, "Temp": 23.2526073333}, {"Mon": 7, "Year": 1995, "Temp": 24.3979751613}, {"Mon": 8, "Year": 1995, "Temp": 24.1949658065}, {"Mon": 9, "Year": 1995, "Temp": 21.751506}, {"Mon": 10, "Year": 1995, "Temp": 19.1476941935}, {"Mon": 11, "Year": 1995, "Temp": 14.6726056667}, {"Mon": 12, "Year": 1995, "Temp": 11.1805887097}, {"Mon": 1, "Year": 1996, "Temp": 10.2675709677}, {"Mon": 2, "Year": 1996, "Temp": 11.3940582759}, {"Mon": 3, "Year": 1996, "Temp": 14.0500722581}, {"Mon": 4, "Year": 1996, "Temp": 17.6871583333}, {"Mon": 5, "Year": 1996, "Temp": 21.2007732258}, {"Mon": 6, "Year": 1996, "Temp": 23.1181013333}, {"Mon": 7, "Year": 1996, "Temp": 23.886183871}, {"Mon": 8, "Year": 1996, "Temp": 23.6474364516}, {"Mon": 9, "Year": 1996, "Temp": 21.5113596667}, {"Mon": 10, "Year": 1996, "Temp": 18.5248945161}, {"Mon": 11, "Year": 1996, "Temp": 14.5990806667}, {"Mon": 12, "Year": 1996, "Temp": 11.7395122581}, {"Mon": 1, "Year": 1997, "Temp": 10.3136590323}, {"Mon": 2, "Year": 1997, "Temp": 12.2100657143}, {"Mon": 3, "Year": 1997, "Temp": 15.1988380645}, {"Mon": 4, "Year": 1997, "Temp": 17.686838}, {"Mon": 5, "Year": 1997, "Temp": 21.1667587097}, {"Mon": 6, "Year": 1997, "Temp": 23.2218116667}, {"Mon": 7, "Year": 1997, "Temp": 24.2102612903}, {"Mon": 8, "Year": 1997, "Temp": 24.1767529032}, {"Mon": 9, "Year": 1997, "Temp": 21.6811913333}, {"Mon": 10, "Year": 1997, "Temp": 18.6771845161}, {"Mon": 11, "Year": 1997, "Temp": 15.0121683333}, {"Mon": 12, "Year": 1997, "Temp": 11.9202767742}, {"Mon": 1, "Year": 1998, "Temp": 11.0496345161}, {"Mon": 2, "Year": 1998, "Temp": 13.0710092857}, {"Mon": 3, "Year": 1998, "Temp": 15.0945822581}, {"Mon": 4, "Year": 1998, "Temp": 19.30204}, {"Mon": 5, "Year": 1998, "Temp": 21.8282806452}, {"Mon": 6, "Year": 1998, "Temp": 23.5824346667}, {"Mon": 7, "Year": 1998, "Temp": 24.5455206452}, {"Mon": 8, "Year": 1998, "Temp": 24.3402883871}, {"Mon": 9, "Year": 1998, "Temp": 22.4326393333}, {"Mon": 10, "Year": 1998, "Temp": 19.3529351613}, {"Mon": 11, "Year": 1998, "Temp": 15.1573256667}, {"Mon": 12, "Year": 1998, "Temp": 12.2880964516}, {"Mon": 1, "Year": 1999, "Temp": 11.3521077419}, {"Mon": 2, "Year": 1999, "Temp": 12.878655}, {"Mon": 3, "Year": 1999, "Temp": 14.9611470968}, {"Mon": 4, "Year": 1999, "Temp": 18.805242}, {"Mon": 5, "Year": 1999, "Temp": 21.2879993548}, {"Mon": 6, "Year": 1999, "Temp": 23.2416263333}, {"Mon": 7, "Year": 1999, "Temp": 24.3453270968}, {"Mon": 8, "Year": 1999, "Temp": 23.9421409677}, {"Mon": 9, "Year": 1999, "Temp": 22.41203}, {"Mon": 10, "Year": 1999, "Temp": 18.8460896774}, {"Mon": 11, "Year": 1999, "Temp": 14.911163}, {"Mon": 12, "Year": 1999, "Temp": 11.9833316129}, {"Mon": 1, "Year": 2000, "Temp": 10.3743335484}, {"Mon": 2, "Year": 2000, "Temp": 11.9338672414}, {"Mon": 3, "Year": 2000, "Temp": 15.2318493548}, {"Mon": 4, "Year": 2000, "Temp": 18.9372356667}, {"Mon": 5, "Year": 2000, "Temp": 21.7117022581}, {"Mon": 6, "Year": 2000, "Temp": 23.3344516667}, {"Mon": 7, "Year": 2000, "Temp": 24.1613154839}, {"Mon": 8, "Year": 2000, "Temp": 24.0766480645}, {"Mon": 9, "Year": 2000, "Temp": 21.907414}, {"Mon": 10, "Year": 2000, "Temp": 18.6197112903}, {"Mon": 11, "Year": 2000, "Temp": 14.5958333333}, {"Mon": 12, "Year": 2000, "Temp": 11.8526532258}, {"Mon": 1, "Year": 2001, "Temp": 10.6590248387}, {"Mon": 2, "Year": 2001, "Temp": 12.2229039286}, {"Mon": 3, "Year": 2001, "Temp": 15.4303209677}, {"Mon": 4, "Year": 2001, "Temp": 18.6212246667}, {"Mon": 5, "Year": 2001, "Temp": 21.8147080645}, {"Mon": 6, "Year": 2001, "Temp": 23.1523736667}, {"Mon": 7, "Year": 2001, "Temp": 24.4790722581}, {"Mon": 8, "Year": 2001, "Temp": 24.2122648387}, {"Mon": 9, "Year": 2001, "Temp": 21.8881643333}, {"Mon": 10, "Year": 2001, "Temp": 19.4418754839}, {"Mon": 11, "Year": 2001, "Temp": 15.2352083333}, {"Mon": 12, "Year": 2001, "Temp": 11.4607935484}, {"Mon": 1, "Year": 2002, "Temp": 11.5441132258}, {"Mon": 2, "Year": 2002, "Temp": 13.4368578571}, {"Mon": 3, "Year": 2002, "Temp": 16.1294283871}, {"Mon": 4, "Year": 2002, "Temp": 18.8479266667}, {"Mon": 5, "Year": 2002, "Temp": 21.4671216129}, {"Mon": 6, "Year": 2002, "Temp": 23.5279873333}, {"Mon": 7, "Year": 2002, "Temp": 24.6992948387}, {"Mon": 8, "Year": 2002, "Temp": 24.0439187097}, {"Mon": 9, "Year": 2002, "Temp": 22.0262886667}, {"Mon": 10, "Year": 2002, "Temp": 18.7852283871}, {"Mon": 11, "Year": 2002, "Temp": 14.9934783333}, {"Mon": 12, "Year": 2002, "Temp": 11.1655677419}, {"Mon": 1, "Year": 2003, "Temp": 10.7341835484}, {"Mon": 2, "Year": 2003, "Temp": 12.0623564286}, {"Mon": 3, "Year": 2003, "Temp": 14.9693393548}, {"Mon": 4, "Year": 2003, "Temp": 18.5815246667}, {"Mon": 5, "Year": 2003, "Temp": 21.7764806452}, {"Mon": 6, "Year": 2003, "Temp": 23.55036}, {"Mon": 7, "Year": 2003, "Temp": 24.3237516129}, {"Mon": 8, "Year": 2003, "Temp": 24.3157351613}, {"Mon": 9, "Year": 2003, "Temp": 22.0773616667}, {"Mon": 10, "Year": 2003, "Temp": 18.7540180645}, {"Mon": 11, "Year": 2003, "Temp": 15.3549136667}, {"Mon": 12, "Year": 2003, "Temp": 11.98461}, {"Mon": 1, "Year": 2004, "Temp": 10.7190583871}, {"Mon": 2, "Year": 2004, "Temp": 12.7258486207}, {"Mon": 3, "Year": 2004, "Temp": 15.6864296774}, {"Mon": 4, "Year": 2004, "Temp": 18.952218}, {"Mon": 5, "Year": 2004, "Temp": 21.3127735484}, {"Mon": 6, "Year": 2004, "Temp": 23.1902686667}, {"Mon": 7, "Year": 2004, "Temp": 24.1475393548}, {"Mon": 8, "Year": 2004, "Temp": 23.9558719355}, {"Mon": 9, "Year": 2004, "Temp": 22.2432996667}, {"Mon": 10, "Year": 2004, "Temp": 19.0215696774}, {"Mon": 11, "Year": 2004, "Temp": 15.510617}, {"Mon": 12, "Year": 2004, "Temp": 11.9872474194}, {"Mon": 1, "Year": 2005, "Temp": 10.8034048387}, {"Mon": 2, "Year": 2005, "Temp": 11.42017}, {"Mon": 3, "Year": 2005, "Temp": 14.8229506452}, {"Mon": 4, "Year": 2005, "Temp": 19.0273636667}, {"Mon": 5, "Year": 2005, "Temp": 21.43902}, {"Mon": 6, "Year": 2005, "Temp": 23.9889253333}, {"Mon": 7, "Year": 2005, "Temp": 24.5689983871}, {"Mon": 8, "Year": 2005, "Temp": 24.0946187097}, {"Mon": 9, "Year": 2005, "Temp": 22.5970996667}, {"Mon": 10, "Year": 2005, "Temp": 19.19676}, {"Mon": 11, "Year": 2005, "Temp": 15.473134}, {"Mon": 12, "Year": 2005, "Temp": 11.3595658065}, {"Mon": 1, "Year": 2006, "Temp": 10.7928448387}, {"Mon": 2, "Year": 2006, "Temp": 12.2603132143}, {"Mon": 3, "Year": 2006, "Temp": 15.1057877419}, {"Mon": 4, "Year": 2006, "Temp": 18.7959986667}, {"Mon": 5, "Year": 2006, "Temp": 21.5198858065}, {"Mon": 6, "Year": 2006, "Temp": 23.702347}, {"Mon": 7, "Year": 2006, "Temp": 24.8445741935}, {"Mon": 8, "Year": 2006, "Temp": 24.3166641935}, {"Mon": 9, "Year": 2006, "Temp": 22.1553243333}, {"Mon": 10, "Year": 2006, "Temp": 19.8772758065}, {"Mon": 11, "Year": 2006, "Temp": 15.6806393333}, {"Mon": 12, "Year": 2006, "Temp": 12.4011874194}, {"Mon": 1, "Year": 2007, "Temp": 11.6360651613}, {"Mon": 2, "Year": 2007, "Temp": 13.1287485714}, {"Mon": 3, "Year": 2007, "Temp": 15.6567483871}, {"Mon": 4, "Year": 2007, "Temp": 18.7849173333}, {"Mon": 5, "Year": 2007, "Temp": 22.0604754839}, {"Mon": 6, "Year": 2007, "Temp": 23.656992}, {"Mon": 7, "Year": 2007, "Temp": 24.2722254839}, {"Mon": 8, "Year": 2007, "Temp": 24.348643871}, {"Mon": 9, "Year": 2007, "Temp": 22.270792}, {"Mon": 10, "Year": 2007, "Temp": 19.1497580645}, {"Mon": 11, "Year": 2007, "Temp": 14.8629853333}, {"Mon": 12, "Year": 2007, "Temp": 12.0640870968}, {"Mon": 1, "Year": 2008, "Temp": 10.3125145161}, {"Mon": 2, "Year": 2008, "Temp": 11.7690668966}, {"Mon": 3, "Year": 2008, "Temp": 15.9205364516}, {"Mon": 4, "Year": 2008, "Temp": 18.877875}, {"Mon": 5, "Year": 2008, "Temp": 21.4885358065}, {"Mon": 6, "Year": 2008, "Temp": 23.2510273333}, {"Mon": 7, "Year": 2008, "Temp": 24.457566129}, {"Mon": 8, "Year": 2008, "Temp": 24.1112348387}, {"Mon": 9, "Year": 2008, "Temp": 22.0824203333}, {"Mon": 10, "Year": 2008, "Temp": 19.3174374194}, {"Mon": 11, "Year": 2008, "Temp": 15.3233373333}, {"Mon": 12, "Year": 2008, "Temp": 12.0255951613}, {"Mon": 1, "Year": 2009, "Temp": 10.6930793548}, {"Mon": 2, "Year": 2009, "Temp": 13.0199778571}, {"Mon": 3, "Year": 2009, "Temp": 15.3585419355}, {"Mon": 4, "Year": 2009, "Temp": 18.8938723333}, {"Mon": 5, "Year": 2009, "Temp": 21.7336848387}, {"Mon": 6, "Year": 2009, "Temp": 23.6693783333}, {"Mon": 7, "Year": 2009, "Temp": 24.3869777419}, {"Mon": 8, "Year": 2009, "Temp": 24.3189829032}, {"Mon": 9, "Year": 2009, "Temp": 22.452364}, {"Mon": 10, "Year": 2009, "Temp": 19.2946025806}, {"Mon": 11, "Year": 2009, "Temp": 15.1140133333}, {"Mon": 12, "Year": 2009, "Temp": 11.74245}, {"Mon": 1, "Year": 2010, "Temp": 10.6206622581}, {"Mon": 2, "Year": 2010, "Temp": 12.3872282143}, {"Mon": 3, "Year": 2010, "Temp": 15.5906058065}, {"Mon": 4, "Year": 2010, "Temp": 18.676471}, {"Mon": 5, "Year": 2010, "Temp": 21.747303871}, {"Mon": 6, "Year": 2010, "Temp": 23.8433173333}, {"Mon": 7, "Year": 2010, "Temp": 24.9957083871}, {"Mon": 8, "Year": 2010, "Temp": 24.6293709677}, {"Mon": 9, "Year": 2010, "Temp": 22.387267}, {"Mon": 10, "Year": 2010, "Temp": 18.9640480645}, {"Mon": 11, "Year": 2010, "Temp": 15.5958333333}, {"Mon": 12, "Year": 2010, "Temp": 11.396443871}, {"Mon": 1, "Year": 2011, "Temp": 9.8020029032}, {"Mon": 2, "Year": 2011, "Temp": 12.0449335714}, {"Mon": 3, "Year": 2011, "Temp": 14.8329354839}, {"Mon": 4, "Year": 2011, "Temp": 18.8713283333}, {"Mon": 5, "Year": 2011, "Temp": 21.6097845161}, {"Mon": 6, "Year": 2011, "Temp": 23.622833}, {"Mon": 7, "Year": 2011, "Temp": 24.5206658065}, {"Mon": 8, "Year": 2011, "Temp": 24.2670670968}, {"Mon": 9, "Year": 2011, "Temp": 22.2468436667}, {"Mon": 10, "Year": 2011, "Temp": 18.9915141935}, {"Mon": 11, "Year": 2011, "Temp": 15.5006023333}, {"Mon": 12, "Year": 2011, "Temp": 11.9194332258}, {"Mon": 1, "Year": 2012, "Temp": 10.6162409677}, {"Mon": 2, "Year": 2012, "Temp": 11.1620513793}, {"Mon": 3, "Year": 2012, "Temp": 15.3335254839}, {"Mon": 4, "Year": 2012, "Temp": 19.0775193333}, {"Mon": 5, "Year": 2012, "Temp": 22.1456180645}, {"Mon": 6, "Year": 2012, "Temp": 23.8615343333}, {"Mon": 7, "Year": 2012, "Temp": 24.7876119355}, {"Mon": 8, "Year": 2012, "Temp": 24.5016329032}, {"Mon": 9, "Year": 2012, "Temp": 22.175309}, {"Mon": 10, "Year": 2012, "Temp": 19.2656451613}, {"Mon": 11, "Year": 2012, "Temp": 15.1798573333}, {"Mon": 12, "Year": 2012, "Temp": 11.5166070968}, {"Mon": 1, "Year": 2013, "Temp": 10.8174280645}, {"Mon": 2, "Year": 2013, "Temp": 12.1923210714}, {"Mon": 3, "Year": 2013, "Temp": 15.194576129}, {"Mon": 4, "Year": 2013, "Temp": 18.4400403333}, {"Mon": 5, "Year": 2013, "Temp": 21.7664803226}, {"Mon": 6, "Year": 2013, "Temp": 23.5630926667}, {"Mon": 7, "Year": 2013, "Temp": 24.6933409677}, {"Mon": 8, "Year": 2013, "Temp": 24.490916129}, {"Mon": 9, "Year": 2013, "Temp": 22.173797}, {"Mon": 10, "Year": 2013, "Temp": 19.2272380645}, {"Mon": 11, "Year": 2013, "Temp": 15.3424486667}, {"Mon": 12, "Year": 2013, "Temp": 11.7994548387}, {"Mon": 1, "Year": 2014, "Temp": 11.3348667742}, {"Mon": 2, "Year": 2014, "Temp": 12.0677546429}, {"Mon": 3, "Year": 2014, "Temp": 15.6825829032}, {"Mon": 4, "Year": 2014, "Temp": 19.134305}, {"Mon": 5, "Year": 2014, "Temp": 21.7684741935}, {"Mon": 6, "Year": 2014, "Temp": 23.7953956667}, {"Mon": 7, "Year": 2014, "Temp": 24.5854990323}, {"Mon": 8, "Year": 2014, "Temp": 24.073466129}, {"Mon": 9, "Year": 2014, "Temp": 22.3698183333}, {"Mon": 10, "Year": 2014, "Temp": 19.5527374194}, {"Mon": 11, "Year": 2014, "Temp": 15.3695296667}, {"Mon": 12, "Year": 2014, "Temp": 12.0165287097}, {"Mon": 1, "Year": 2015, "Temp": 11.3910045161}, {"Mon": 2, "Year": 2015, "Temp": 12.4825789286}, {"Mon": 3, "Year": 2015, "Temp": 15.591523871}, {"Mon": 4, "Year": 2015, "Temp": 18.810135}, {"Mon": 5, "Year": 2015, "Temp": 22.0407225806}, {"Mon": 6, "Year": 2015, "Temp": 23.711906}, {"Mon": 7, "Year": 2015, "Temp": 24.7027409677}, {"Mon": 8, "Year": 2015, "Temp": 24.6574287097}, {"Mon": 9, "Year": 2015, "Temp": 22.7013913333}, {"Mon": 10, "Year": 2015, "Temp": 19.5560919355}, {"Mon": 11, "Year": 2015, "Temp": 15.9633223333}, {"Mon": 12, "Year": 2015, "Temp": 13.2291948387}, {"Mon": 1, "Year": 2016, "Temp": 11.0796806452}, {"Mon": 2, "Year": 2016, "Temp": 13.433}, {"Mon": 3, "Year": 2016, "Temp": 16.3043422581}, {"Mon": 4, "Year": 2016, "Temp": 19.6147923333}, {"Mon": 5, "Year": 2016, "Temp": 21.8446129032}, {"Mon": 6, "Year": 2016, "Temp": 23.882143}, {"Mon": 7, "Year": 2016, "Temp": 24.9340306452}, {"Mon": 8, "Year": 2016, "Temp": 24.8342706452}, {"Mon": 9, "Year": 2016, "Temp": 22.8717926667}, {"Mon": 10, "Year": 2016, "Temp": 19.3708529032}, {"Mon": 11, "Year": 2016, "Temp": 15.2029776667}, {"Mon": 12, "Year": 2016, "Temp": 12.5757929032}, {"Mon": 1, "Year": 2017, "Temp": 11.3643835484}, {"Mon": 2, "Year": 2017, "Temp": 13.1277282143}, {"Mon": 3, "Year": 2017, "Temp": 15.761646129}, {"Mon": 4, "Year": 2017, "Temp": 19.3168133333}, {"Mon": 5, "Year": 2017, "Temp": 22.1352509677}, {"Mon": 6, "Year": 2017, "Temp": 23.8620903333}, {"Mon": 7, "Year": 2017, "Temp": 25.0272854839}, {"Mon": 8, "Year": 2017, "Temp": 24.6267596774}, {"Mon": 9, "Year": 2017, "Temp": 22.6618156667}, {"Mon": 10, "Year": 2017, "Temp": 19.4506367742}, {"Mon": 11, "Year": 2017, "Temp": 15.385216}, {"Mon": 12, "Year": 2017, "Temp": 12.2017893548}, {"Mon": 1, "Year": 2018, "Temp": 10.9896006452}, {"Mon": 2, "Year": 2018, "Temp": 12.3247253571}, {"Mon": 3, "Year": 2018, "Temp": 15.8414358065}, {"Mon": 4, "Year": 2018, "Temp": 19.3177016667}, {"Mon": 5, "Year": 2018, "Temp": 22.3325035484}, {"Mon": 6, "Year": 2018, "Temp": 23.924559}, {"Mon": 7, "Year": 2018, "Temp": 25.1350035484}, {"Mon": 8, "Year": 2018, "Temp": 24.8241912903}, {"Mon": 9, "Year": 2018, "Temp": 22.6958576667}, {"Mon": 10, "Year": 2018, "Temp": 19.236256129}, {"Mon": 11, "Year": 2018, "Temp": 15.383815}, {"Mon": 12, "Year": 2018, "Temp": 12.2427712903}, {"Mon": 1, "Year": 2019, "Temp": 11.3000751613}, {"Mon": 2, "Year": 2019, "Temp": 12.7719353571}, {"Mon": 3, "Year": 2019, "Temp": 15.8589203226}, {"Mon": 4, "Year": 2019, "Temp": 19.1834206667}, {"Mon": 5, "Year": 2019, "Temp": 21.845926129}, {"Mon": 6, "Year": 2019, "Temp": 24.242051}, {"Mon": 7, "Year": 2019, "Temp": 24.8549306452}, {"Mon": 8, "Year": 2019, "Temp": 24.677376129}, {"Mon": 9, "Year": 2019, "Temp": 22.8459726667}, {"Mon": 10, "Year": 2019, "Temp": 19.6581906452}, {"Mon": 11, "Year": 2019, "Temp": 15.641688}, {"Mon": 12, "Year": 2019, "Temp": 12.7898206452}, {"Mon": 1, "Year": 2020, "Temp": 12.0862712903}, {"Mon": 2, "Year": 2020, "Temp": 13.6008275862}, {"Mon": 3, "Year": 2020, "Temp": 16.2831045161}, {"Mon": 4, "Year": 2020, "Temp": 18.7358753333}, {"Mon": 5, "Year": 2020, "Temp": 21.961583871}, {"Mon": 6, "Year": 2020, "Temp": 23.888501}, {"Mon": 7, "Year": 2020, "Temp": 24.660786129}, {"Mon": 8, "Year": 2020, "Temp": 24.8090329032}, {"Mon": 9, "Year": 2020, "Temp": 22.733206}],
          cityInfo:[{"long": "121.4365", "lat": "31.2165", "popu": "14987000.0", "tempRate": "-20.3%", "co2Rate": null}, {"long": "116.3883", "lat": "39.9289", "popu": "11106000.0", "tempRate": "-27.7%", "co2Rate": null}, {"long": "113.325", "lat": "23.145", "popu": "8829000.0", "tempRate": "-7.3%", "co2Rate": null}, {"long": "114.1221", "lat": "22.5524", "popu": "7581000.0", "tempRate": "-7.6%", "co2Rate": null}, {"long": "114.27", "lat": "30.58", "popu": "7243000.0", "tempRate": "-16.3%", "co2Rate": null}, {"long": "117.2", "lat": "39.13", "popu": "7180000.0", "tempRate": "-26.1%", "co2Rate": null}, {"long": "106.595", "lat": "29.565", "popu": "6461000.0", "tempRate": "-10.7%", "co2Rate": null}, {"long": "123.45", "lat": "41.805", "popu": "4787000.0", "tempRate": "-41.3%", "co2Rate": null}, {"long": "113.7447", "lat": "23.0489", "popu": "4528000.0", "tempRate": "-7.4%", "co2Rate": null}, {"long": "104.07", "lat": "30.67", "popu": "4123000.0", "tempRate": "-15.5%", "co2Rate": null}, {"long": "108.895", "lat": "34.275", "popu": "4009000.0", "tempRate": "-16.6%", "co2Rate": null}, {"long": "109.6091", "lat": "23.0965", "popu": "3830000.0", "tempRate": "-6.7%", "co2Rate": null}, {"long": "118.78", "lat": "32.05", "popu": "3679000.0", "tempRate": "-21.4%", "co2Rate": null}, {"long": "106.72", "lat": "26.58", "popu": "3662000.0", "tempRate": "-13.0%", "co2Rate": null}, {"long": "126.65", "lat": "45.75", "popu": "3621000.0", "tempRate": "-63.2%", "co2Rate": null}, {"long": "117.67", "lat": "24.5204", "popu": "3531147.0", "tempRate": "-10.6%", "co2Rate": null}, {"long": "125.34", "lat": "43.865", "popu": "3183000.0", "tempRate": "-53.8%", "co2Rate": null}, {"long": "121.6298", "lat": "38.9228", "popu": "3167000.0", "tempRate": "-24.3%", "co2Rate": null}, {"long": "118.05", "lat": "36.8", "popu": "3061000.0", "tempRate": "-26.2%", "co2Rate": null}, {"long": "120.17", "lat": "30.25", "popu": "3007000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "102.68", "lat": "25.07", "popu": "2931000.0", "tempRate": "-10.1%", "co2Rate": null}, {"long": "112.5451", "lat": "37.875", "popu": "2913000.0", "tempRate": "-34.2%", "co2Rate": null}, {"long": "120.33", "lat": "36.09", "popu": "2866000.0", "tempRate": "-21.0%", "co2Rate": null}, {"long": "116.995", "lat": "36.675", "popu": "2798000.0", "tempRate": "-25.0%", "co2Rate": null}, {"long": "113.6651", "lat": "34.755", "popu": "2636000.0", "tempRate": "-21.2%", "co2Rate": null}, {"long": "119.3", "lat": "26.08", "popu": "2606000.0", "tempRate": "-12.5%", "co2Rate": null}, {"long": "112.97", "lat": "28.2", "popu": "2604000.0", "tempRate": "-14.2%", "co2Rate": null}, {"long": "112.9", "lat": "27.8504", "popu": "2586948.0", "tempRate": "-14.3%", "co2Rate": null}, {"long": "103.792", "lat": "36.056", "popu": "2561000.0", "tempRate": "-26.6%", "co2Rate": null}, {"long": "118.08", "lat": "24.45", "popu": "2519000.0", "tempRate": "-9.1%", "co2Rate": null}, {"long": "120.83", "lat": "40.7503", "popu": "2426000.0", "tempRate": "-31.1%", "co2Rate": null}, {"long": "114.48", "lat": "38.05", "popu": "2417000.0", "tempRate": "-19.2%", "co2Rate": null}, {"long": "126.55", "lat": "43.85", "popu": "2396000.0", "tempRate": "-60.5%", "co2Rate": null}, {"long": "115.88", "lat": "28.68", "popu": "2350000.0", "tempRate": "-16.1%", "co2Rate": null}, {"long": "120.6501", "lat": "28.02", "popu": "2350000.0", "tempRate": "-15.7%", "co2Rate": null}, {"long": "106.13", "lat": "30.7804", "popu": "2174000.0", "tempRate": "-11.8%", "co2Rate": null}, {"long": "108.32", "lat": "22.82", "popu": "2167000.0", "tempRate": "-7.0%", "co2Rate": null}, {"long": "87.575", "lat": "43.805", "popu": "2151000.0", "tempRate": "-52.5%", "co2Rate": null}, {"long": "117.57", "lat": "34.88", "popu": "2145000.0", "tempRate": "-26.0%", "co2Rate": null}, {"long": "121.4", "lat": "37.5304", "popu": "2116000.0", "tempRate": "-24.7%", "co2Rate": null}, {"long": "117.18", "lat": "34.28", "popu": "2091000.0", "tempRate": "-23.3%", "co2Rate": null}, {"long": "118.33", "lat": "35.08", "popu": "2082000.0", "tempRate": "-25.5%", "co2Rate": null}, {"long": "110.32", "lat": "20.05", "popu": "2046189.0", "tempRate": "-6.5%", "co2Rate": null}, {"long": "109.822", "lat": "40.6522", "popu": "2036000.0", "tempRate": "-45.4%", "co2Rate": null}, {"long": "117.28", "lat": "31.85", "popu": "2035000.0", "tempRate": "-20.2%", "co2Rate": null}, {"long": "116.9789", "lat": "33.6361", "popu": "1964000.0", "tempRate": "-22.4%", "co2Rate": null}, {"long": "112.53", "lat": "33.0004", "popu": "1944000.0", "tempRate": "-20.1%", "co2Rate": null}, {"long": "121.55", "lat": "29.88", "popu": "1923000.0", "tempRate": "-17.2%", "co2Rate": null}, {"long": "118.1944", "lat": "39.6243", "popu": "1879000.0", "tempRate": "-29.2%", "co2Rate": null}, {"long": "113.3", "lat": "40.08", "popu": "1873000.0", "tempRate": "-45.1%", "co2Rate": null}, {"long": "118.7734", "lat": "34.1299", "popu": "1770000.0", "tempRate": "-22.9%", "co2Rate": null}, {"long": "115.65", "lat": "34.4504", "popu": "1753000.0", "tempRate": "-23.7%", "co2Rate": null}, {"long": "120.3", "lat": "31.58", "popu": "1749000.0", "tempRate": "-21.5%", "co2Rate": null}, {"long": "111.66", "lat": "40.82", "popu": "1726000.0", "tempRate": "-60.4%", "co2Rate": null}, {"long": "112.4701", "lat": "34.68", "popu": "1715000.0", "tempRate": "-20.5%", "co2Rate": null}, {"long": "113.16", "lat": "30.6501", "popu": "1708000.0", "tempRate": "-15.4%", "co2Rate": null}, {"long": "125.0", "lat": "46.58", "popu": "1693000.0", "tempRate": "-62.9%", "co2Rate": null}, {"long": "116.48", "lat": "31.7503", "popu": "1690000.0", "tempRate": "-21.0%", "co2Rate": null}, {"long": "108.4", "lat": "30.82", "popu": "1680000.0", "tempRate": "-11.8%", "co2Rate": null}, {"long": "120.62", "lat": "31.3005", "popu": "1650000.0", "tempRate": "-21.2%", "co2Rate": null}, {"long": "123.99", "lat": "47.345", "popu": "1641000.0", "tempRate": "-65.9%", "co2Rate": null}, {"long": "122.94", "lat": "41.115", "popu": "1639000.0", "tempRate": "-37.2%", "co2Rate": null}, {"long": "114.48", "lat": "36.58", "popu": "1631000.0", "tempRate": "-21.8%", "co2Rate": null}, {"long": "117.1201", "lat": "36.2", "popu": "1629000.0", "tempRate": "-28.5%", "co2Rate": null}, {"long": "116.67", "lat": "23.37", "popu": "1601000.0", "tempRate": "-8.7%", "co2Rate": null}, {"long": "110.38", "lat": "21.2", "popu": "1590000.0", "tempRate": "-6.7%", "co2Rate": null}, {"long": "113.44", "lat": "30.3704", "popu": "1556000.0", "tempRate": "-15.3%", "co2Rate": null}, {"long": "119.1001", "lat": "36.7204", "popu": "1553000.0", "tempRate": "-26.5%", "co2Rate": null}, {"long": "114.07", "lat": "32.1304", "popu": "1541000.0", "tempRate": "-19.3%", "co2Rate": null}, {"long": "105.38", "lat": "28.88", "popu": "1537000.0", "tempRate": "-11.4%", "co2Rate": null}, {"long": "114.95", "lat": "25.92", "popu": "1500000.0", "tempRate": "-13.2%", "co2Rate": null}, {"long": "109.25", "lat": "24.28", "popu": "1497000.0", "tempRate": "-9.3%", "co2Rate": null}, {"long": "123.87", "lat": "41.8654", "popu": "1470000.0", "tempRate": "-43.7%", "co2Rate": null}, {"long": "111.68", "lat": "29.03", "popu": "1469000.0", "tempRate": "-13.3%", "co2Rate": null}, {"long": "105.05", "lat": "29.5804", "popu": "1466000.0", "tempRate": "-13.7%", "co2Rate": null}, {"long": "118.58", "lat": "24.9", "popu": "1463000.0", "tempRate": "-10.2%", "co2Rate": null}, {"long": "116.98", "lat": "32.63", "popu": "1451000.0", "tempRate": "-21.8%", "co2Rate": null}, {"long": "105.5333", "lat": "30.5333", "popu": "1425000.0", "tempRate": "-12.8%", "co2Rate": null}, {"long": "104.77", "lat": "31.47", "popu": "1396000.0", "tempRate": "-15.1%", "co2Rate": null}, {"long": "118.48", "lat": "31.7304", "popu": "1366302.0", "tempRate": "-20.8%", "co2Rate": null}, {"long": "112.33", "lat": "28.6004", "popu": "1352000.0", "tempRate": "-13.9%", "co2Rate": null}, {"long": "115.45", "lat": "35.23", "popu": "1338000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "119.97", "lat": "31.78", "popu": "1327000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "118.95", "lat": "42.27", "popu": "1277000.0", "tempRate": "-41.6%", "co2Rate": null}, {"long": "119.03", "lat": "33.58", "popu": "1264000.0", "tempRate": "-22.6%", "co2Rate": null}, {"long": "129.59", "lat": "44.575", "popu": "1244000.0", "tempRate": "-67.5%", "co2Rate": null}, {"long": "120.1", "lat": "30.8704", "popu": "1231000.0", "tempRate": "-20.7%", "co2Rate": null}, {"long": "105.92", "lat": "34.6", "popu": "1225000.0", "tempRate": "-23.4%", "co2Rate": null}, {"long": "104.8333", "lat": "26.5944", "popu": "1221000.0", "tempRate": "-14.4%", "co2Rate": null}, {"long": "110.87", "lat": "21.9204", "popu": "1217715.0", "tempRate": "-5.6%", "co2Rate": null}, {"long": "116.55", "lat": "35.4004", "popu": "1186000.0", "tempRate": "-24.5%", "co2Rate": null}, {"long": "103.7333", "lat": "29.5671", "popu": "1157000.0", "tempRate": "-14.4%", "co2Rate": null}, {"long": "117.97", "lat": "28.4704", "popu": "1144577.0", "tempRate": "-16.7%", "co2Rate": null}, {"long": "110.15", "lat": "22.63", "popu": "1127000.0", "tempRate": "-5.8%", "co2Rate": null}, {"long": "108.7147", "lat": "34.3456", "popu": "1126000.0", "tempRate": "-16.7%", "co2Rate": null}, {"long": "115.48", "lat": "38.8704", "popu": "1107000.0", "tempRate": "-21.1%", "co2Rate": null}, {"long": "104.78", "lat": "29.4", "popu": "1105000.0", "tempRate": "-13.9%", "co2Rate": null}, {"long": "109.02", "lat": "32.68", "popu": "1100000.0", "tempRate": "-16.3%", "co2Rate": null}, {"long": "119.65", "lat": "29.12", "popu": "1092852.0", "tempRate": "-19.2%", "co2Rate": null}, {"long": "113.15", "lat": "27.83", "popu": "1080000.0", "tempRate": "-14.1%", "co2Rate": null}, {"long": "112.13", "lat": "32.02", "popu": "1069000.0", "tempRate": "-18.0%", "co2Rate": null}, {"long": "119.3801", "lat": "35.99", "popu": "1060000.0", "tempRate": "-26.6%", "co2Rate": null}, {"long": "101.77", "lat": "36.62", "popu": "1048000.0", "tempRate": "-44.6%", "co2Rate": null}, {"long": "114.93", "lat": "40.83", "popu": "1046000.0", "tempRate": "-49.6%", "co2Rate": null}, {"long": "113.5678", "lat": "22.2769", "popu": "1023000.0", "tempRate": "-6.9%", "co2Rate": null}, {"long": "130.35", "lat": "46.83", "popu": "1020000.0", "tempRate": "-70.9%", "co2Rate": null}, {"long": "112.59", "lat": "26.88", "popu": "1016000.0", "tempRate": "-14.5%", "co2Rate": null}, {"long": "123.75", "lat": "41.3304", "popu": "1012000.0", "tempRate": "-47.4%", "co2Rate": null}, {"long": "119.62", "lat": "39.9304", "popu": "1003000.0", "tempRate": "-29.8%", "co2Rate": null}, {"long": "111.62", "lat": "26.2304", "popu": "1000000.0", "tempRate": "-14.1%", "co2Rate": null}, {"long": "99.15", "lat": "25.12", "popu": "1000000.0", "tempRate": "-10.2%", "co2Rate": null}, {"long": "106.273", "lat": "38.468", "popu": "991000.0", "tempRate": "-28.9%", "co2Rate": null}, {"long": "120.75", "lat": "30.7704", "popu": "988000.0", "tempRate": "-20.5%", "co2Rate": null}, {"long": "110.28", "lat": "25.28", "popu": "987000.0", "tempRate": "-10.1%", "co2Rate": null}, {"long": "114.4", "lat": "27.8333", "popu": "982000.0", "tempRate": "-15.4%", "co2Rate": null}, {"long": "113.57", "lat": "37.87", "popu": "981448.0", "tempRate": "-28.8%", "co2Rate": null}, {"long": "130.97", "lat": "45.3", "popu": "965000.0", "tempRate": "-65.4%", "co2Rate": null}, {"long": "118.35", "lat": "34.38", "popu": "962656.0", "tempRate": "-23.3%", "co2Rate": null}, {"long": "113.85", "lat": "27.62", "popu": "961000.0", "tempRate": "-14.9%", "co2Rate": null}, {"long": "121.1", "lat": "41.1204", "popu": "956000.0", "tempRate": "-34.7%", "co2Rate": null}, {"long": "120.825", "lat": "32.0304", "popu": "947000.0", "tempRate": "-22.6%", "co2Rate": null}, {"long": "113.12", "lat": "23.0301", "popu": "943000.0", "tempRate": "-7.2%", "co2Rate": null}, {"long": "116.75", "lat": "33.9504", "popu": "913000.0", "tempRate": "-22.8%", "co2Rate": null}, {"long": "114.93", "lat": "27.8", "popu": "913000.0", "tempRate": "-15.9%", "co2Rate": null}, {"long": "113.87", "lat": "35.3204", "popu": "903000.0", "tempRate": "-21.2%", "co2Rate": null}, {"long": "104.57", "lat": "28.77", "popu": "902000.0", "tempRate": "-12.9%", "co2Rate": null}, {"long": "117.33", "lat": "32.95", "popu": "894000.0", "tempRate": "-21.9%", "co2Rate": null}, {"long": "114.35", "lat": "36.08", "popu": "887000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "122.27", "lat": "43.62", "popu": "884000.0", "tempRate": "-42.6%", "co2Rate": null}, {"long": "111.28", "lat": "30.7", "popu": "875000.0", "tempRate": "-13.6%", "co2Rate": null}, {"long": "111.97", "lat": "21.8504", "popu": "872363.0", "tempRate": "-6.2%", "co2Rate": null}, {"long": "114.35", "lat": "34.85", "popu": "872000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "124.3936", "lat": "40.1436", "popu": "870000.0", "tempRate": "-35.2%", "co2Rate": null}, {"long": "118.7553", "lat": "30.9525", "popu": "866000.0", "tempRate": "-21.7%", "co2Rate": null}, {"long": "119.45", "lat": "35.4304", "popu": "865000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "113.22", "lat": "35.25", "popu": "857000.0", "tempRate": "-23.5%", "co2Rate": null}, {"long": "119.43", "lat": "32.22", "popu": "854000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "113.3", "lat": "33.7304", "popu": "849000.0", "tempRate": "-20.6%", "co2Rate": null}, {"long": "106.92", "lat": "27.7", "popu": "849000.0", "tempRate": "-14.3%", "co2Rate": null}, {"long": "105.93", "lat": "26.2504", "popu": "849000.0", "tempRate": "-12.7%", "co2Rate": null}, {"long": "112.73", "lat": "37.6804", "popu": "840000.0", "tempRate": "-31.1%", "co2Rate": null}, {"long": "120.1253", "lat": "33.3856", "popu": "839000.0", "tempRate": "-23.4%", "co2Rate": null}, {"long": "111.52", "lat": "36.0803", "popu": "834000.0", "tempRate": "-25.0%", "co2Rate": null}, {"long": "113.1", "lat": "29.3801", "popu": "826000.0", "tempRate": "-14.3%", "co2Rate": null}, {"long": "104.89", "lat": "25.0904", "popu": "816000.0", "tempRate": "-12.2%", "co2Rate": null}, {"long": "118.37", "lat": "31.3504", "popu": "810000.0", "tempRate": "-20.4%", "co2Rate": null}, {"long": "116.68", "lat": "39.5204", "popu": "810000.0", "tempRate": "-25.4%", "co2Rate": null}, {"long": "103.72", "lat": "27.3204", "popu": "809000.0", "tempRate": "-17.3%", "co2Rate": null}, {"long": "119.4011", "lat": "41.24", "popu": "806000.0", "tempRate": "-39.6%", "co2Rate": null}, {"long": "107.15", "lat": "34.38", "popu": "800000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "122.28", "lat": "40.6703", "popu": "795000.0", "tempRate": "-34.8%", "co2Rate": null}, {"long": "123.18", "lat": "41.28", "popu": "794000.0", "tempRate": "-38.3%", "co2Rate": null}, {"long": "120.57", "lat": "30.0004", "popu": "777000.0", "tempRate": "-20.7%", "co2Rate": null}, {"long": "128.9", "lat": "47.6999", "popu": "777000.0", "tempRate": "-105.0%", "co2Rate": null}, {"long": "119.9519", "lat": "30.0533", "popu": "771000.0", "tempRate": "-21.5%", "co2Rate": null}, {"long": "121.66", "lat": "42.0105", "popu": "770000.0", "tempRate": "-42.5%", "co2Rate": null}, {"long": "110.78", "lat": "32.57", "popu": "770000.0", "tempRate": "-17.8%", "co2Rate": null}, {"long": "112.83", "lat": "35.5004", "popu": "760000.0", "tempRate": "-28.3%", "co2Rate": null}, {"long": "130.37", "lat": "47.4", "popu": "743307.0", "tempRate": "-78.7%", "co2Rate": null}, {"long": "109.1", "lat": "21.4804", "popu": "728978.0", "tempRate": "-7.1%", "co2Rate": null}, {"long": "113.58", "lat": "24.8", "popu": "720266.0", "tempRate": "-8.9%", "co2Rate": null}, {"long": "119.17", "lat": "34.6004", "popu": "715600.0", "tempRate": "-22.2%", "co2Rate": null}, {"long": "113.0301", "lat": "23.7004", "popu": "706717.0", "tempRate": "-7.6%", "co2Rate": null}, {"long": "113.1053", "lat": "36.1839", "popu": "706000.0", "tempRate": "-30.2%", "co2Rate": null}, {"long": "115.1", "lat": "30.22", "popu": "688090.0", "tempRate": "-15.7%", "co2Rate": null}, {"long": "114.98", "lat": "35.7004", "popu": "666322.0", "tempRate": "-20.7%", "co2Rate": null}, {"long": "103.8166", "lat": "25.6005", "popu": "652604.0", "tempRate": "-10.9%", "co2Rate": null}, {"long": "115.79", "lat": "39.5401", "popu": "628000.0", "tempRate": "-25.9%", "co2Rate": null}, {"long": "116.1944", "lat": "40.2248", "popu": "614821.0", "tempRate": "-32.5%", "co2Rate": null}, {"long": "119.9", "lat": "32.4904", "popu": "612356.0", "tempRate": "-22.6%", "co2Rate": null}, {"long": "114.5", "lat": "37.05", "popu": "611739.0", "tempRate": "-21.7%", "co2Rate": null}, {"long": "117.05", "lat": "30.5", "popu": "580497.0", "tempRate": "-18.3%", "co2Rate": null}, {"long": "86.0299", "lat": "44.3", "popu": "573182.0", "tempRate": "-48.7%", "co2Rate": null}, {"long": "112.42", "lat": "39.3004", "popu": "570000.0", "tempRate": "-47.8%", "co2Rate": null}, {"long": "117.78", "lat": "30.9504", "popu": "562832.0", "tempRate": "-19.5%", "co2Rate": null}, {"long": "122.1", "lat": "37.5", "popu": "560255.0", "tempRate": "-21.4%", "co2Rate": null}, {"long": "124.33", "lat": "43.17", "popu": "555609.0", "tempRate": "-48.8%", "co2Rate": null}, {"long": "115.98", "lat": "29.73", "popu": "545616.0", "tempRate": "-16.8%", "co2Rate": null}, {"long": "75.9699", "lat": "39.4763", "popu": "543914.0", "tempRate": "-22.7%", "co2Rate": null}, {"long": "119.43", "lat": "32.4", "popu": "539715.0", "tempRate": "-22.1%", "co2Rate": null}],
          tempGeoJson: [{"name": "Afghanistan", "code": "AFG", "tempRate": "-13.3%"}, {"name": "Albania", "code": "ALB", "tempRate": "-17.1%"}, {"name": "Algeria", "code": "DZA", "tempRate": "-14.7%"}, {"name": "American Samoa", "code": "ASM", "tempRate": "-2.0%"}, {"name": "Andorra", "code": "AND", "tempRate": "-45.0%"}, {"name": "Angola", "code": "AGO", "tempRate": "-3.0%"}, {"name": "Antigua And Barbuda", "code": "ATG", "tempRate": "-1.3%"}, {"name": "Argentina", "code": "ARG", "tempRate": "4.6%"}, {"name": "Armenia", "code": "ARM", "tempRate": "-23.9%"}, {"name": "Aruba", "code": "ABW", "tempRate": "-1.1%"}, {"name": "Australia", "code": "AUS", "tempRate": "4.3%"}, {"name": "Austria", "code": "AUT", "tempRate": "-34.5%"}, {"name": "Azerbaijan", "code": "AZE", "tempRate": "-14.7%"}, {"name": "Bahamas, The", "code": "BHS", "tempRate": "-4.1%"}, {"name": "Bahrain", "code": "BHR", "tempRate": "-4.2%"}, {"name": "Bangladesh", "code": "BGD", "tempRate": "-2.5%"}, {"name": "Barbados", "code": "BRB", "tempRate": "-1.4%"}, {"name": "Belarus", "code": "BLR", "tempRate": "-57.3%"}, {"name": "Belgium", "code": "BEL", "tempRate": "-29.6%"}, {"name": "Belize", "code": "BLZ", "tempRate": "-9.0%"}, {"name": "Benin", "code": "BEN", "tempRate": "-2.5%"}, {"name": "Bhutan", "code": "BTN", "tempRate": "-13.7%"}, {"name": "Bolivia", "code": "BOL", "tempRate": "-5.6%"}, {"name": "Bosnia And Herzegovina", "code": "BIH", "tempRate": "-34.1%"}, {"name": "Botswana", "code": "BWA", "tempRate": "0.7%"}, {"name": "Brazil", "code": "BRA", "tempRate": "-0.5%"}, {"name": "Brunei", "code": "BRN", "tempRate": "-4.4%"}, {"name": "Bulgaria", "code": "BGR", "tempRate": "-25.8%"}, {"name": "Burkina Faso", "code": "BFA", "tempRate": "-2.9%"}, {"name": "Burma", "code": "MMR", "tempRate": "-4.1%"}, {"name": "Burundi", "code": "BDI", "tempRate": "-5.8%"}, {"name": "Cabo Verde", "code": "CPV", "tempRate": "-0.8%"}, {"name": "Cambodia", "code": "KHM", "tempRate": "-4.1%"}, {"name": "Cameroon", "code": "CMR", "tempRate": "-5.8%"}, {"name": "Canada", "code": "CAN", "tempRate": "-38.2%"}, {"name": "Central African Republic", "code": "CAF", "tempRate": "-6.2%"}, {"name": "Chad", "code": "TCD", "tempRate": "-3.3%"}, {"name": "Chile", "code": "CHL", "tempRate": "3.5%"}, {"name": "China", "code": "CHN", "tempRate": "-24.1%"}, {"name": "Colombia", "code": "COL", "tempRate": "-3.6%"}, {"name": "Comoros", "code": "COM", "tempRate": "-2.1%"}, {"name": "Congo (Brazzaville)", "code": "COG", "tempRate": "-5.4%"}, {"name": "Congo (Kinshasa)", "code": "COD", "tempRate": "-4.5%"}, {"name": "Costa Rica", "code": "CRI", "tempRate": "-3.2%"}, {"name": "Croatia", "code": "HRV", "tempRate": "-29.7%"}, {"name": "Cuba", "code": "CUB", "tempRate": "-5.0%"}, {"name": "Cura\u00e7ao", "code": "CUW", "tempRate": "-1.1%"}, {"name": "Cyprus", "code": "CYP", "tempRate": "-12.0%"}, {"name": "Czechia", "code": "CZE", "tempRate": "-37.5%"}, {"name": "C\u00f4te D\u2019Ivoire", "code": "CIV", "tempRate": "-3.9%"}, {"name": "Denmark", "code": "DNK", "tempRate": "-35.5%"}, {"name": "Djibouti", "code": "DJI", "tempRate": "-3.3%"}, {"name": "Dominica", "code": "DMA", "tempRate": "-1.4%"}, {"name": "Dominican Republic", "code": "DOM", "tempRate": "-3.9%"}, {"name": "Ecuador", "code": "ECU", "tempRate": "-4.1%"}, {"name": "Egypt", "code": "EGY", "tempRate": "-8.1%"}, {"name": "El Salvador", "code": "SLV", "tempRate": "-4.1%"}, {"name": "Equatorial Guinea", "code": "GNQ", "tempRate": "-3.3%"}, {"name": "Eritrea", "code": "ERI", "tempRate": "-4.4%"}, {"name": "Estonia", "code": "EST", "tempRate": "-51.2%"}, {"name": "Ethiopia", "code": "ETH", "tempRate": "-9.1%"}, {"name": "Fiji", "code": "FJI", "tempRate": "-3.7%"}, {"name": "Finland", "code": "FIN", "tempRate": "-55.0%"}, {"name": "France", "code": "FRA", "tempRate": "-25.6%"}, {"name": "Gabon", "code": "GAB", "tempRate": "-4.9%"}, {"name": "Gambia, The", "code": "GMB", "tempRate": "-3.8%"}, {"name": "Georgia", "code": "GEO", "tempRate": "-25.9%"}, {"name": "Germany", "code": "DEU", "tempRate": "-32.9%"}, {"name": "Ghana", "code": "GHA", "tempRate": "-4.7%"}, {"name": "Greece", "code": "GRC", "tempRate": "-12.8%"}, {"name": "Grenada", "code": "GRD", "tempRate": "-2.0%"}, {"name": "Guam", "code": "GUM", "tempRate": "-1.9%"}, {"name": "Guatemala", "code": "GTM", "tempRate": "-8.3%"}, {"name": "Guinea", "code": "GIN", "tempRate": "-3.1%"}, {"name": "Guinea-Bissau", "code": "GNB", "tempRate": "-2.9%"}, {"name": "Guyana", "code": "GUY", "tempRate": "-2.7%"}, {"name": "Haiti", "code": "HTI", "tempRate": "-5.0%"}, {"name": "Honduras", "code": "HND", "tempRate": "-7.4%"}, {"name": "Hong Kong", "code": "HKG", "tempRate": "-6.9%"}, {"name": "Hungary", "code": "HUN", "tempRate": "-33.2%"}, {"name": "Iceland", "code": "ISL", "tempRate": "-21.5%"}, {"name": "India", "code": "IND", "tempRate": "-3.4%"}, {"name": "Indonesia", "code": "IDN", "tempRate": "-3.3%"}, {"name": "Iran", "code": "IRN", "tempRate": "-16.2%"}, {"name": "Iraq", "code": "IRQ", "tempRate": "-13.9%"}, {"name": "Ireland", "code": "IRL", "tempRate": "-12.6%"}, {"name": "Israel", "code": "ISR", "tempRate": "-8.0%"}, {"name": "Italy", "code": "ITA", "tempRate": "-19.8%"}, {"name": "Jamaica", "code": "JAM", "tempRate": "-4.9%"}, {"name": "Japan", "code": "JPN", "tempRate": "-18.7%"}, {"name": "Jordan", "code": "JOR", "tempRate": "-12.8%"}, {"name": "Kazakhstan", "code": "KAZ", "tempRate": "-48.1%"}, {"name": "Kenya", "code": "KEN", "tempRate": "-2.4%"}, {"name": "Kiribati", "code": "KIR", "tempRate": "-3.0%"}, {"name": "Korea, North", "code": "PRK", "tempRate": "-28.5%"}, {"name": "Korea, South", "code": "KOR", "tempRate": "-25.4%"}, {"name": "Kosovo", "code": "XKS", "tempRate": "-24.9%"}, {"name": "Kuwait", "code": "KWT", "tempRate": "-10.1%"}, {"name": "Kyrgyzstan", "code": "KGZ", "tempRate": "-23.2%"}, {"name": "Laos", "code": "LAO", "tempRate": "-6.3%"}, {"name": "Latvia", "code": "LVA", "tempRate": "-48.1%"}, {"name": "Lebanon", "code": "LBN", "tempRate": "-11.0%"}, {"name": "Lesotho", "code": "LSO", "tempRate": "9.9%"}, {"name": "Liberia", "code": "LBR", "tempRate": "-3.2%"}, {"name": "Libya", "code": "LBY", "tempRate": "-8.5%"}, {"name": "Liechtenstein", "code": "LIE", "tempRate": "-54.6%"}, {"name": "Lithuania", "code": "LTU", "tempRate": "-54.6%"}, {"name": "Luxembourg", "code": "LUX", "tempRate": "-34.7%"}, {"name": "Macau", "code": "MAC", "tempRate": "-6.8%"}, {"name": "Macedonia", "code": "MKD", "tempRate": "-24.9%"}, {"name": "Madagascar", "code": "MDG", "tempRate": "0.4%"}, {"name": "Malawi", "code": "MWI", "tempRate": "0.9%"}, {"name": "Malaysia", "code": "MYS", "tempRate": "-4.0%"}, {"name": "Maldives", "code": "MDV", "tempRate": "-3.4%"}, {"name": "Mali", "code": "MLI", "tempRate": "-2.7%"}, {"name": "Malta", "code": "MLT", "tempRate": "-9.2%"}, {"name": "Marshall Islands", "code": "MHL", "tempRate": "-2.1%"}, {"name": "Mauritania", "code": "MRT", "tempRate": "-5.0%"}, {"name": "Mauritius", "code": "MUS", "tempRate": "0.7%"}, {"name": "Mexico", "code": "MEX", "tempRate": "-8.6%"}, {"name": "Micronesia, Federated States Of", "code": "FSM", "tempRate": "-2.7%"}, {"name": "Moldova", "code": "MDA", "tempRate": "-41.9%"}, {"name": "Monaco", "code": "MCO", "tempRate": "-19.8%"}, {"name": "Mongolia", "code": "MNG", "tempRate": "-192.5%"}, {"name": "Montenegro", "code": "MNE", "tempRate": "-24.2%"}, {"name": "Morocco", "code": "MAR", "tempRate": "-10.1%"}, {"name": "Mozambique", "code": "MOZ", "tempRate": "0.3%"}, {"name": "Namibia", "code": "NAM", "tempRate": "-2.2%"}, {"name": "Nepal", "code": "NPL", "tempRate": "-3.8%"}, {"name": "Netherlands", "code": "NLD", "tempRate": "-25.6%"}, {"name": "New Zealand", "code": "NZL", "tempRate": "-4.8%"}, {"name": "Nicaragua", "code": "NIC", "tempRate": "-3.6%"}, {"name": "Niger", "code": "NER", "tempRate": "-2.9%"}, {"name": "Nigeria", "code": "NGA", "tempRate": "-3.3%"}, {"name": "Northern Mariana Islands", "code": "MNP", "tempRate": "-1.7%"}, {"name": "Norway", "code": "NOR", "tempRate": "-55.7%"}, {"name": "Oman", "code": "OMN", "tempRate": "-2.3%"}, {"name": "Pakistan", "code": "PAK", "tempRate": "-7.7%"}, {"name": "Palau", "code": "PLW", "tempRate": "-2.5%"}, {"name": "Panama", "code": "PAN", "tempRate": "-2.2%"}, {"name": "Papua New Guinea", "code": "PNG", "tempRate": "-2.5%"}, {"name": "Paraguay", "code": "PRY", "tempRate": "-2.1%"}, {"name": "Peru", "code": "PER", "tempRate": "-1.1%"}, {"name": "Philippines", "code": "PHL", "tempRate": "-4.0%"}, {"name": "Poland", "code": "POL", "tempRate": "-40.7%"}, {"name": "Portugal", "code": "PRT", "tempRate": "-13.1%"}, {"name": "Qatar", "code": "QAT", "tempRate": "-6.0%"}, {"name": "Romania", "code": "ROU", "tempRate": "-35.4%"}, {"name": "Russia", "code": "RUS", "tempRate": "-67.0%"}, {"name": "Rwanda", "code": "RWA", "tempRate": "-7.8%"}, {"name": "Saint Kitts And Nevis", "code": "KNA", "tempRate": "-1.3%"}, {"name": "Saint Lucia", "code": "LCA", "tempRate": "-2.4%"}, {"name": "Saint Vincent And The Grenadines", "code": "VCT", "tempRate": "-1.8%"}, {"name": "Samoa", "code": "WSM", "tempRate": "-1.9%"}, {"name": "San Marino", "code": "SMR", "tempRate": "-22.1%"}, {"name": "Sao Tome And Principe", "code": "STP", "tempRate": "-4.4%"}, {"name": "Saudi Arabia", "code": "SAU", "tempRate": "-7.8%"}, {"name": "Senegal", "code": "SEN", "tempRate": "-1.4%"}, {"name": "Serbia", "code": "SRB", "tempRate": "-28.1%"}, {"name": "Seychelles", "code": "SYC", "tempRate": "-2.9%"}, {"name": "Sierra Leone", "code": "SLE", "tempRate": "-3.3%"}, {"name": "Singapore", "code": "SGP", "tempRate": "-2.2%"}, {"name": "Sint Maarten", "code": "SXM", "tempRate": "-1.3%"}, {"name": "Slovakia", "code": "SVK", "tempRate": "-33.0%"}, {"name": "Slovenia", "code": "SVN", "tempRate": "-37.0%"}, {"name": "Solomon Islands", "code": "SLB", "tempRate": "-3.6%"}, {"name": "Somalia", "code": "SOM", "tempRate": "-2.7%"}, {"name": "South Africa", "code": "ZAF", "tempRate": "1.5%"}, {"name": "South Sudan", "code": "SSD", "tempRate": "-4.2%"}, {"name": "Spain", "code": "ESP", "tempRate": "-15.6%"}, {"name": "Sri Lanka", "code": "LKA", "tempRate": "-3.7%"}, {"name": "Sudan", "code": "SDN", "tempRate": "-1.7%"}, {"name": "Suriname", "code": "SUR", "tempRate": "-3.2%"}, {"name": "Swaziland", "code": "SWZ", "tempRate": "0.7%"}, {"name": "Sweden", "code": "SWE", "tempRate": "-40.6%"}, {"name": "Switzerland", "code": "CHE", "tempRate": "-36.4%"}, {"name": "Syria", "code": "SYR", "tempRate": "-15.5%"}, {"name": "Taiwan", "code": "TWN", "tempRate": "-7.2%"}, {"name": "Tajikistan", "code": "TJK", "tempRate": "-18.2%"}, {"name": "Tanzania", "code": "TZA", "tempRate": "-0.8%"}, {"name": "Thailand", "code": "THA", "tempRate": "-4.1%"}, {"name": "Timor-Leste", "code": "TLS", "tempRate": "-2.2%"}, {"name": "Togo", "code": "TGO", "tempRate": "-2.6%"}, {"name": "Tonga", "code": "TON", "tempRate": "-3.7%"}, {"name": "Trinidad And Tobago", "code": "TTO", "tempRate": "-2.6%"}, {"name": "Tunisia", "code": "TUN", "tempRate": "-13.3%"}, {"name": "Turkey", "code": "TUR", "tempRate": "-17.6%"}, {"name": "Turkmenistan", "code": "TKM", "tempRate": "-19.8%"}, {"name": "Tuvalu", "code": "TUV", "tempRate": "-1.4%"}, {"name": "Uganda", "code": "UGA", "tempRate": "-3.9%"}, {"name": "Ukraine", "code": "UKR", "tempRate": "-43.4%"}, {"name": "United Arab Emirates", "code": "ARE", "tempRate": "-6.3%"}, {"name": "United Kingdom", "code": "GBR", "tempRate": "-20.4%"}, {"name": "United States", "code": "USA", "tempRate": "-18.9%"}, {"name": "Uruguay", "code": "URY", "tempRate": "3.3%"}, {"name": "Uzbekistan", "code": "UZB", "tempRate": "-18.1%"}, {"name": "Vanuatu", "code": "VUT", "tempRate": "-2.7%"}, {"name": "Venezuela", "code": "VEN", "tempRate": "-3.9%"}, {"name": "Vietnam", "code": "VNM", "tempRate": "-5.6%"}, {"name": "West Bank", "code": "XWB", "tempRate": "-10.5%"}, {"name": "Yemen", "code": "YEM", "tempRate": "-3.0%"}, {"name": "Zambia", "code": "ZMB", "tempRate": "-0.2%"}, {"name": "Zimbabwe", "code": "ZWE", "tempRate": "-1.1%"}],
  
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
        }
    },
    beforeMount() {
        window.localStorage.setItem('placeSelection', "global");
        window.localStorage.setItem('scaleSelection', 0);

        this.placeSelection = window.localStorage.getItem('placeSelection');
        this.scaleSelection = window.localStorage.getItem('scaleSelection');
        console.log(this.placeSelection);
        console.log(this.scaleSelection);
        this.temp = this.tempGeoJson;
        this.readGeoJson().then(this.initMap);
        // this.getTemp().then(this.readGeoJson).then(this.initMap);
    },
    mounted() {
      this.refreshHtmp();
      /*
        this.$nextTick(function() {
            this.iearth = this.$refs["earthfrm"].contentWindow;
            window.addEventListener("message", this.sendEarth);
            this.iheatmp = this.$refs["heatmpfrm"].contentWindow;
            window.addEventListener("message", this.sendHeatmp);
        });
      */

    },
    beforeDestroy(){
        this.removeMap();
    },
    destroyed() {
        // window.removeEventListener("message", this.sendEarth);
        // window.removeEventListener("message", this.sendHeatmp);
    },
    methods: {
      refreshHtmp(){
        if (this.htmpcsv == 0) {
              console.log(this.htmpcsv);
              document.getElementById("globalhtmp").removeAttribute("style")
              document.getElementById("italyhtmp").setAttribute("style", "display:none")
              document.getElementById("milanhtmp").setAttribute("style", "display:none")
        } else if (this.htmpcsv == 1){
            document.getElementById("globalhtmp").setAttribute("style", "display:none")
            document.getElementById("italyhtmp").removeAttribute("style")
            document.getElementById("milanhtmp").setAttribute("style", "display:none")
        } else if (this.htmpcsv == 2) {
            document.getElementById("milanhtmp").removeAttribute("style")
            document.getElementById("globalhtmp").setAttribute("style", "display:none")
            document.getElementById("italyhtmp").setAttribute("style", "display:none")
        } else {
            this.getHeatMapList().then(this.initHeatMap);
            // this.initHeatMap();
        }
      },
      async getTemp() {
            console.log("getTemp");
            return this.axios({
                method: 'post',
                headers: {
                  'Content-Type':'application/json',
                  // 'X-CSRFToken': csrf_token,
                },
                url: '/tempGeoJson/',
                // headers: {'token': this.$store.state.userInfo.token},
                data: {
                    data: {time: [this.startY, this.endY]}
                },
            }).then(res => {
                this.temp = res.data;
                console.log("res");
                console.log(res.data);
                // if (res.data.code == 1001) {
                // } 
                // else {
                //   this.$message({
                //     showClose: true,
                //     type: 'error',
                //     message: "Error on getting Temperature Data"
                //   })
                // }
            })
        },
        /*
        sendEarth(){
            this.iearth.postMessage({
                data: this.temp
            },'*');
        },
        sendHeatmp(){
            this.iheatmp.postMessage({
            data: "1"
            },'*');
        },
        */
        async readGeoJson(){
            return this.worldData = await d3.json("static/world-110.geojson");
        },
        // TODO: heatmap
        async getHeatMapList(){
            console.log("getHeatMap");
            return this.axios({
                method: 'post',
                url: '/monthTemp/',
                data: {
                  data: {place: [this.placeSelection, this.scaleSelection]}
                },
            }).then(res => {
                this.heatMapList = res.data;
                console.log("res monthTemp");
                // console.log(this.heatMapList);
            });
        },
        mouseover(){
            this.Tooltip.style("opacity", 1)
        },
        mousemove (d) {
            this.Tooltip
                .html(d.name + "<br>" + "long: " + d.long + "<br>" + "lat: " + d.lat)
                .style("left", (d3.pointer(this)[0]+10) + "px")
                .style("top", (d3.pointer(this)[1]) + "px");
        },
        mouseleave(d) {
            this.Tooltip.style("opacity", 0);
        },
        getColor(d) {
            return d == undefined ? 'white' :   // #e3ecc2
                d > 0.25 ? '#b10026' :
                d > 0.125  ? '#e31a1c' :
                d > 0.10  ? '#fc4e2a' :
                d > 0.075  ? '#fd8d3c' :
                d > 0.05   ? '#feb24c' :
                d > 0.025   ? '#fed976' :
                d > 0   ? '#ffeda0' : '#ffffcc';
        },
        style(feature) {
            return {
                weight: 1,
                opacity: 1,
                color: 'white',
                dashArray: '3',
                fillOpacity: 1,
                fillColor: this.getColor(feature.properties.tempRate)
            };
        },
        highlightFeature(e) {
            const layer = e.target;

            layer.setStyle({
                weight: 4,
                color: 'white',
                dashArray: '',
                fillOpacity: 1
            });

            // layer.bringToFront();

            this.info.update(layer.feature.properties);
        },
        resetHighlight(e) {
            this.geojson.resetStyle(e.target);
            this.info.update();
        },
        // TODO: axios
        getCity(countryCode){
            this.placeSelection = countryCode;
            this.scaleSelection = 1;
            window.localStorage.setItem('placeSelection', this.placeSelection);
            window.localStorage.setItem('scaleSelection', this.scaleSelection);

            console.log("getCity");
            console.log(countryCode);
            return this.axios({
                method: 'post',
                url: '/selectcountry/',
                // headers: {'token': this.$store.state.userInfo.token},
                data: {
                    data:{
                        time: [this.startY, this.endY], 
                        country: countryCode
                    }
                },
            }).then(res => {
                this.cityInfo = res.data;
                console.log("res");
                console.log(this.cityInfo[0].name);
            })
        },
        floatEqual(num1, num2) {
            return Math.abs(num1 - num2) < Number.EPSILON;
        },
        citySelection(e){
            console.log(e);
            var latlng = e.latlng;
            let tempRate = null;
            let popu = null;
            console.log(latlng.lat);
            console.log(latlng.lng);
            for (let i of this.cityInfo) {
                // console.log(Number(i.lat), Number(i.long));
                // console.log(this.floatEqual(Number(i.lat),latlng.lat), this.floatEqual(Number(i.long),latlng.lng));
                if (this.floatEqual(Number(i.lat),latlng.lat) && this.floatEqual(Number(i.long),latlng.lng)) {
                    // tempRate = (-1 * i.tempRate.replace("%","")).toFixed(3);
                    // popu = i.popu;
                    this.placeSelection = i.id;
                    this.scaleSelection = 2;
                    console.log(i.id);
                    break;
                }
            }
            this.htmpcsv = 2;
            this.refreshHtmp();
            // this.getHeatMapList().then(this.initHeatMap);
            // this.initHeatMap();

            // return `Population: ${1}<br>Temperature increase rate: ${tempRate}`
        },
        showCity(){
            if(this.cityMarkers!=null){
                console.log('clearLayers');
                this.cityMarkers.clearLayers();
            }
            // this.info.update();
            /*
            if(countryCode != 'CHN'){
                console.log('111');
                return;
            }*/
            var layers = [];
            for (let i of this.cityInfo) {
                var city = {};
                city.lat = i.lat;
                city.lng = i.long;
                city.popu = i.popu;
                city.tempRate = (-1 * i.tempRate.replace("%","")).toFixed(3);
                layers.push(L.circleMarker(city, {
                    color: 'green',
                    fillColor: 'green',
                    fillOpacity: 0.5,
                    radius: 5,
                    zIndexOffset: 9999
                }).bringToFront().addTo(this.map).on('click', this.citySelection)
                  .bindPopup(`<h3>${i.name}</h3>Population: ${i.popu}<br>Temperature increase rate: ${city.tempRate}%`));
                // TODO: bindPopup function select city
            }
            this.cityMarkers = L.layerGroup(layers);
            this.map.addLayer(this.cityMarkers);
        },
        zoomToFeature(e) {
            console.log(e);
            const layer = e.target;
            this.map.fitBounds(layer.getBounds());
            var countryCode = layer.feature.properties.code;
            console.log(countryCode);
            this.htmpcsv = 1;
            this.refreshHtmp();
            // this.getHeatMapList().then(this.initHeatMap);
            // this.initHeatMap()
            this.getCity(countryCode).then(this.showCity);
            // this.showCity(countryCode);
        },
        onEachFeature(feature, layer) {
            layer.on({
                mouseover: this.highlightFeature,
                mouseout: this.resetHighlight,
                click: this.zoomToFeature
            });
        },
        addLegend(){
            console.log('legend');
            const div = L.DomUtil.create('div', 'info legend');
            const grades = ["<0%", '0.0%', '2.5%', "5.0%", "7.5%", "10.0%", "12.5%", "25.0%"];
            const labels = [];
            let from, to;
            labels.push(`<i style="background:${this.getColor(undefined)}"></i> Unknown`);
            for (let i = 0; i < grades.length; i++) {
                from = grades[i];
                to = grades[i + 1];
                if (i == grades.length-1){
                    i = 30;
                }
                labels.push(`<i style="background:${this.getColor(i*0.025 - 0.01)}"></i> ${from}${to ? `&ndash;${to}` : '+'}`);
            }
            div.innerHTML = labels.join('<br>');
            return div;
        },
        setMapBg(){
            console.log('initMap');
            this.corner1 = L.latLng(-90, -180), //设置左上角经纬度 
            this.corner2 = L.latLng(90, 180), //设置右下点经纬度 
            this.bounds = L.latLngBounds(this.corner1, this.corner2), //构建视图限制范围
            this.map = L.map('map', {
                minZoom: this.minZoom,
                maxZoom: this.maxZoom,
                dragging: true,
                maxBounds: this.bounds,
                maxBoundsViscosity: 1
            }).setView([40, 0], 1);
            this.scaleControl = L.control.scale({maxWidth: 150, imperial: false}).addTo(this.map);
        },
        setToolTips(){
            console.log('tooltip');
            this.Tooltip = d3.select("#map")
                            .append("div")
                            .attr("class", "tooltip")
                            .style("opacity", 1)
                            .style("background-color", "white")
                            .style("border", "solid")
                            .style("border-width", "2px")
                            .style("border-radius", "5px")
                            .style("padding", "5px");
        },
        setInfo(){
            console.log('info')
            // TODO: fix info function (ok?
            // control that shows country info on hover
            this.info = L.control();

            this.info.update = function (props) {
                const contents = props ? `<b>${props.name}</b>: ${(props.tempRate * 100).toFixed(1)}% increase` : 'Hover over a region';
                this._div.innerHTML = `<h3>Temperature Increase Rate</h3>${contents}`;
            };

            this.info.onAdd = function (map) {
                this._div = L.DomUtil.create('div', 'info');
                this.update();
                return this._div;
            };
            this.info.addTo(this.map);
        },
        setLayers(){
            console.log('layers');
            const mbAttr = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
            const mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';
            // const streets = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});

            // https://tile.openstreetmap.org/{z}/{x}/{y}.png '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            // temperature
            this.temperature = L.tileLayer(
                mbUrl, {
                id: 'mapbox/streets-v11',tileSize: 512, zoomOffset: -1,
                maxZoom: this.maxZoom,
                attribution: mbAttr
            }).addTo(this.map);

            // CO2
            this.CO2 = L.tileLayer(
                mbUrl, {
                id: 'mapbox/streets-v11',tileSize: 512, zoomOffset: -1,
                maxZoom: this.maxZoom,
                attribution: mbAttr
            });

            this.allOptions = {
                "Temperature": this.temperature,
                "Carbon Emission": this.CO2,
                // "test": streets
            };

            console.log('add layers');
            // Add baseLayers to map as control layers
            // L.control.layers(this.allOptions, null, {collapsed: false}).addTo(this.map);

        },
        addTempData(){
            console.log('add tempdata');
            // console.log(this.worldData);
		        console.log(this.temp);
            if (Array.isArray(this.temp)){
                var dataJson = JSON.parse(JSON.stringify(this.temp));
                this.worldJson = JSON.parse(JSON.stringify(this.worldData)); // For Deep Cloning so that gj does not get changed
                for (let i of this.worldJson.features) {
                    var tempRate = dataJson.find((item) => item.name == i.properties.name);
                    if (tempRate != undefined) {
                        i.properties.tempRate = (-1 * tempRate.tempRate.replace("%","") / 100).toFixed(5);
                        i.properties.code = tempRate.code
                    } else {
                        i.properties.tempRate = undefined;
                        // console.log(i.properties.name);
                    }
                    // console.log(i.properties)
                }
		        }
			// console.log(this.worldJson);
            this.geojson = L.geoJson(this.worldJson, {
                style: this.style,
                onEachFeature: this.onEachFeature,
            }).addTo(this.map);
            
        },
        async initMap() {
            this.setMapBg();
            // this.setToolTips();
            this.setLayers();
            this.setInfo();
            this.addTempData();
        
            this.legend = L.control({position: 'bottomright'});
            this.legend.onAdd = this.addLegend;
            this.legend.addTo(this.map);

        },
        async removeMap(){
            console.log("remove Map");
            this.map.off();
            this.map.remove();
            return this.map = null;
        },
        // TODO: 年份变化没有？
        changeYear(value) {
          this.startY = value[0];
          this.endY = value[1];
          console.log('start: ', this.startY);
          console.log('end: ', this.endY);
          this.getTemp().then(this.removeMap).then(this.initMap);
        },
        getMon(d){
          console.log(d.Mon);
          return d.Mon;
        },
        getYear(d){
          console.log(d.Year);
          return d.Year;
        },
        getMonJson(key,jsonObj){  
            for(var index in jsonObj){  
              this.getMonJson1(key,jsonObj[index]);
            }  
        },
        getMonJson1(key,jsonObj){
          for (var p1 in jsonObj) {
                if((p1 === key) && (this.heatMapMons.indexOf(jsonObj[key].toString()) == -1)){ 
                    // console.log(jsonObj[key]); 
                    this.heatMapMons.push(jsonObj[key].toString())
                }else if(jsonObj[p1] instanceof Array) {
                    this.getMonJson(key, jsonObj[p1]);
              }
          }
        },
        getYearJson(key,jsonObj){  
            for(var index in jsonObj){  
              this.getYearJson1(key,jsonObj[index]);
            }  
        },
        getYearJson1(key,jsonObj){
          for (var p1 in jsonObj) {
                if((p1 === key) && (this.heatMapYears.indexOf(jsonObj[key].toString()) == -1)){ 
                    // console.log(jsonObj[key]); 
                    this.heatMapYears.push(jsonObj[key].toString())
                }else if(jsonObj[p1] instanceof Array) {
                    this.getYearJson(key, jsonObj[p1]);
              }
          }
        },
        json2Csv(objArray){
            var array = typeof objArray != 'object' ? JSON.parse(objArray) : objArray;
            var str = 'Mon,Year,Temp\n';
            for (var i = 0; i < array.length; i++) {
                var line = '';
                // for (var index in array[i]) {
                //     line += array[i][index] + ',';
                // }
                // 添加双引号
                for (var index in array[i]) {
                   line += '"' + array[i][index] + '",';
                }

                line.slice(0, line.Length-1); 
                str += line + '\n';
            }
            // window.open("data:text/csv;charset=utf-8," + str)
            return str;
        },
        parseCsv (csv) {
          let lines = csv.split(/\r?\n/);
          const header = lines.shift().split(",")
          return  lines.map(line => {
            const bits = line.split(",")
            let obj = {};
            header.forEach((h, i) => obj[h] = bits[i]); // or use reduce here
            // optional:
            // obj["includeInAuto"] = obj["includeInAuto"] === "true";
            return obj;
          });
        },

        // TODO: 
        async initHeatMap() {
          console.log("init heat map");
          // set the dimensions and margins of the graph
          var margin = {top: 70, right: 25, bottom: 30, left: 40},
            width = 420 - margin.left - margin.right,
            height = 490 - margin.top - margin.bottom;

          // append the svg object to the body of the page
          var svg = d3.select("#my_dataviz")
                      .append("svg")
                        .attr("width", width + margin.left + margin.right)
                        .attr("height", height + margin.top + margin.bottom)
                      .append("g")
                        .attr("transform",
                              "translate(" + margin.left + "," + margin.top + ")");
          console.log("svg");
          console.log(this.heatMapList);
          // Labels of row and columns -> unique identifier of the column called 'group' and 'variable'
          this.heatMapMons = [];
          this.heatMapYears = []; 
          // this.heatMapList = JSON.parse(JSON.stringify(this.heatMapList));
          // var data = this.parseCsv(this.json2Csv(this.heatMapList));
          // var data = d3.csv("http://127.0.0.1:8000/monthTemp/?data={'place':['global',0]}");
          // console.log(data);
          this.getMonJson('Mon', this.heatMapList);
          this.getYearJson('Year', this.heatMapList);
          // this.heatMapMons = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"];
          console.log(this.heatMapMons);
          console.log(this.heatMapYears);

          var myMons = d3.map(this.heatMapList, this.getMon).keys()
          var myYear = d3.map(this.heatMapList, this.getYear).keys()
          console.log(myMons);
          console.log(myYear);
          // Build X scales and axis:
          var x = d3.scaleBand()
            .range([ 0, width ])
            .domain(this.heatMapMons)
            .padding(0.05);
          svg.append("g")
            .style("font-size", 15)
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x).tickSize(0))
            .select(".domain").remove()

          // Build Y scales and axis:
          var y = d3.scaleBand()
            .range([ height, 0 ])
            .domain(this.heatMapYears)
            .padding(0.05);
          svg.append("g")
            .style("font-size", 15)
            .call(d3.axisLeft(y).tickSize(0))
            .select(".domain").remove()

          // Build color scale
          var myColor = d3.scaleSequential()
            .interpolator(d3.interpolateInferno)
            .domain([-100,100])

          // create a tooltip
          var tooltip = d3.select("#my_dataviz")
            .append("div")
            .style("opacity", 0)
            .attr("class", "tooltip")
            .style("background-color", "white")
            .style("border", "solid")
            .style("border-width", "2px")
            .style("border-radius", "5px")
            .style("padding", "5px")
            .style("width", "inherit")

          // Three function that change the tooltip when user hover / move / leave a cell
          var mouseover = function(d) {
            tooltip
              .style("opacity", 1)
            d3.select(this)
              .style("stroke", "black")
              .style("opacity", 1)
          }
          var mousemove = function(d) {
            tooltip
              .html("The exact value of<br>this cell is: " + d.value)
              .style("left", (d3.pointer(this)[0]+70) + "px")
              .style("top", (d3.pointer(this)[1]) + "px")
          }
          var mouseleave = function(d) {
            tooltip
              .style("opacity", 0)
            d3.select(this)
              .style("stroke", "none")
              .style("opacity", 0.8)
          }

          // add the squares
          svg.selectAll()
            .data(this.heatMapList, function(d) {return d.Mon+':'+d.Year;})
            .enter()
            .append("rect")
              .attr("x", function(d) { return x(d.Mon) })
              .attr("y", function(d) { return y(d.Year) })
              .attr("rx", 4)
              .attr("ry", 4)
              .attr("width", x.bandwidth() )
              .attr("height", y.bandwidth() )
              .style("fill", function(d) { return myColor(d.Temp)} )
              .style("stroke-width", 4)
              .style("stroke", "none")
              .style("opacity", 0.8)
            .on("mouseover", mouseover)
            .on("mousemove", mousemove)
            .on("mouseleave", mouseleave)
          
          // Add title to graph
          svg.append("text")
                  .attr("x", 0)
                  .attr("y", -50)
                  .attr("text-anchor", "left")
                  .style("font-size", "22px")
                  .text("Avg monthly temperature in Shanghai");

          // Add subtitle to graph
          svg.append("text")
                  .attr("x", 0)
                  .attr("y", -20)
                  .attr("text-anchor", "left")
                  .style("font-size", "14px")
                  .style("fill", "grey")
                  .style("max-width", 400)
                  .text("A short description on findings...");
                  },
    },
  }
</script>

<style>
html, body {
    height: 100%;
    margin: 0;
}
.leaflet-container {
    /* height: 450px; */
    /* width: 600px; */
    max-width: 100%;
    max-height: 100%;
}
#map { width: 850px; height: 530px; }
.info { padding: 6px 8px; font: 14px/16px Arial, Helvetica, sans-serif; background: white; background: rgba(255,255,255,0.8); box-shadow: 0 0 15px rgba(0,0,0,0.2); border-radius: 5px; } .info h4 { margin: 0 0 5px; color: #777; }
.legend { text-align: left; line-height: 18px; color: #555; } .legend i { width: 18px; height: 18px; float: left; margin-right: 8px; opacity: 0.7; }
</style>
  