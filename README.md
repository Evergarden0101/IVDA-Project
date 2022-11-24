# IVDA-Course

## Commit rules

- different folders for different modules
  - Frontend, backend...
- develop on own branch use **checkout**
  -  **yifan, yizhi, yunlong, alex**
- keep commits clean (once commit one function) and describe briefly what is updated
  - in case we need to look back to find bugs, so we can search commits
- Use merge request to merge your branch to **main**, and send the request  in group chat to let others know the update and check bugs
  - merge should be done after checking
- use meaningful variable names, regardless of the length.
- update .gitignore file to ignore changes

## Front back API

先忽略headers，

#### tempGeoJson

- 地图温度数据-map

- 反csv
  - 澳大利亚为例
  - name	code	tempRate
    - Australia	AUS	1.5%

- ```vue
  method: 'post',
  url: '/tempGeoJson',
  headers: {'token': this.$store.state.userInfo.token},
  data: {
  	time: [1980,2020] //初始默认40年
  }
  ```
  
- ```vue
  if (res.data.code == 1001) {
    this.tempRate = res.data.data
  }
  ```

#### co2GeoJson

- 地图co2数据

- 反csv
  - 澳大利亚为例
  - name	code	CO2Rate
    - Australia	AUS	2.5%

- ```vue
  method: 'post',
  url: '/co2GeoJson',
  headers: {'token': this.$store.state.userInfo.token},
  data: {
  	time: [1980,2020] //初始默认40年
  }
  ```

- ```vue
  if (res.data.code == 1001) {
    this.co2Rate = res.data.data
  }
  ```

#### monthTemp

- 40年月平均气温-heatmap
- 反**csv**
  - Mon	Year	Temp
  - Jul	1988	20.0

- ```vue
  method: 'post',
  url: '/monthTemp',
  headers: {'token': this.$store.state.userInfo.token},
  data: {
  	place: ["global", 0] // (["CHN", 1],["上海的id"，2])
  	// 第一个参数表示国家或者城市名称，名称按后端给的数据来
  	// 第二个参数0表示全球，1表示国家，2表示城市
  }
  ```
  
- ```vue
  if (res.data.code == 1001) {
    this.glbMonthTemp = res.data.data
  }
  ```
#### selectcountry

- 选择国家显示城市

- 反字典组

  - {long: 2.349, lat: 48.864, popu: 150000000, tempRate:5.1%, co2Rate: 2.5%}, // *Paris*

- ```vue
  method: 'post',
  url: '/selectcountry',
  headers: {'token': this.$store.state.userInfo.token},
  data: {
  	time: [1980, 2020]
  	country: countryid // 根据后端唯一的名称来给
  }
  ```

- ```vue
  if (res.data.code == 1001) {
    this.citylist = res.data.data
  }
  ```
