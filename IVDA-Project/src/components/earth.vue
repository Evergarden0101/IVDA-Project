<template>
    <div id='map'></div>
</template>

<script>
import * as d3 from 'd3';
export default {
    name: 'Earth',
    data() {
        return {
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
            tempGeoJson: [{"name": "Afghanistan", "code": "AFG", "tempRate": "-13.3%"}, {"name": "Albania", "code": "ALB", "tempRate": "-17.1%"}, {"name": "Algeria", "code": "DZA", "tempRate": "-14.7%"}, {"name": "American Samoa", "code": "ASM", "tempRate": "-2.0%"}, {"name": "Andorra", "code": "AND", "tempRate": "-45.0%"}, {"name": "Angola", "code": "AGO", "tempRate": "-3.0%"}, {"name": "Antigua And Barbuda", "code": "ATG", "tempRate": "-1.3%"}, {"name": "Argentina", "code": "ARG", "tempRate": "4.6%"}, {"name": "Armenia", "code": "ARM", "tempRate": "-23.9%"}, {"name": "Aruba", "code": "ABW", "tempRate": "-1.1%"}, {"name": "Australia", "code": "AUS", "tempRate": "4.3%"}, {"name": "Austria", "code": "AUT", "tempRate": "-34.5%"}, {"name": "Azerbaijan", "code": "AZE", "tempRate": "-14.7%"}, {"name": "Bahamas, The", "code": "BHS", "tempRate": "-4.1%"}, {"name": "Bahrain", "code": "BHR", "tempRate": "-4.2%"}, {"name": "Bangladesh", "code": "BGD", "tempRate": "-2.5%"}, {"name": "Barbados", "code": "BRB", "tempRate": "-1.4%"}, {"name": "Belarus", "code": "BLR", "tempRate": "-57.3%"}, {"name": "Belgium", "code": "BEL", "tempRate": "-29.6%"}, {"name": "Belize", "code": "BLZ", "tempRate": "-9.0%"}, {"name": "Benin", "code": "BEN", "tempRate": "-2.5%"}, {"name": "Bhutan", "code": "BTN", "tempRate": "-13.7%"}, {"name": "Bolivia", "code": "BOL", "tempRate": "-5.6%"}, {"name": "Bosnia And Herzegovina", "code": "BIH", "tempRate": "-34.1%"}, {"name": "Botswana", "code": "BWA", "tempRate": "0.7%"}, {"name": "Brazil", "code": "BRA", "tempRate": "-0.5%"}, {"name": "Brunei", "code": "BRN", "tempRate": "-4.4%"}, {"name": "Bulgaria", "code": "BGR", "tempRate": "-25.8%"}, {"name": "Burkina Faso", "code": "BFA", "tempRate": "-2.9%"}, {"name": "Burma", "code": "MMR", "tempRate": "-4.1%"}, {"name": "Burundi", "code": "BDI", "tempRate": "-5.8%"}, {"name": "Cabo Verde", "code": "CPV", "tempRate": "-0.8%"}, {"name": "Cambodia", "code": "KHM", "tempRate": "-4.1%"}, {"name": "Cameroon", "code": "CMR", "tempRate": "-5.8%"}, {"name": "Canada", "code": "CAN", "tempRate": "-38.2%"}, {"name": "Central African Republic", "code": "CAF", "tempRate": "-6.2%"}, {"name": "Chad", "code": "TCD", "tempRate": "-3.3%"}, {"name": "Chile", "code": "CHL", "tempRate": "3.5%"}, {"name": "China", "code": "CHN", "tempRate": "-24.1%"}, {"name": "Colombia", "code": "COL", "tempRate": "-3.6%"}, {"name": "Comoros", "code": "COM", "tempRate": "-2.1%"}, {"name": "Congo (Brazzaville)", "code": "COG", "tempRate": "-5.4%"}, {"name": "Congo (Kinshasa)", "code": "COD", "tempRate": "-4.5%"}, {"name": "Costa Rica", "code": "CRI", "tempRate": "-3.2%"}, {"name": "Croatia", "code": "HRV", "tempRate": "-29.7%"}, {"name": "Cuba", "code": "CUB", "tempRate": "-5.0%"}, {"name": "Cura\u00e7ao", "code": "CUW", "tempRate": "-1.1%"}, {"name": "Cyprus", "code": "CYP", "tempRate": "-12.0%"}, {"name": "Czechia", "code": "CZE", "tempRate": "-37.5%"}, {"name": "C\u00f4te D\u2019Ivoire", "code": "CIV", "tempRate": "-3.9%"}, {"name": "Denmark", "code": "DNK", "tempRate": "-35.5%"}, {"name": "Djibouti", "code": "DJI", "tempRate": "-3.3%"}, {"name": "Dominica", "code": "DMA", "tempRate": "-1.4%"}, {"name": "Dominican Republic", "code": "DOM", "tempRate": "-3.9%"}, {"name": "Ecuador", "code": "ECU", "tempRate": "-4.1%"}, {"name": "Egypt", "code": "EGY", "tempRate": "-8.1%"}, {"name": "El Salvador", "code": "SLV", "tempRate": "-4.1%"}, {"name": "Equatorial Guinea", "code": "GNQ", "tempRate": "-3.3%"}, {"name": "Eritrea", "code": "ERI", "tempRate": "-4.4%"}, {"name": "Estonia", "code": "EST", "tempRate": "-51.2%"}, {"name": "Ethiopia", "code": "ETH", "tempRate": "-9.1%"}, {"name": "Fiji", "code": "FJI", "tempRate": "-3.7%"}, {"name": "Finland", "code": "FIN", "tempRate": "-55.0%"}, {"name": "France", "code": "FRA", "tempRate": "-25.6%"}, {"name": "Gabon", "code": "GAB", "tempRate": "-4.9%"}, {"name": "Gambia, The", "code": "GMB", "tempRate": "-3.8%"}, {"name": "Georgia", "code": "GEO", "tempRate": "-25.9%"}, {"name": "Germany", "code": "DEU", "tempRate": "-32.9%"}, {"name": "Ghana", "code": "GHA", "tempRate": "-4.7%"}, {"name": "Greece", "code": "GRC", "tempRate": "-12.8%"}, {"name": "Grenada", "code": "GRD", "tempRate": "-2.0%"}, {"name": "Guam", "code": "GUM", "tempRate": "-1.9%"}, {"name": "Guatemala", "code": "GTM", "tempRate": "-8.3%"}, {"name": "Guinea", "code": "GIN", "tempRate": "-3.1%"}, {"name": "Guinea-Bissau", "code": "GNB", "tempRate": "-2.9%"}, {"name": "Guyana", "code": "GUY", "tempRate": "-2.7%"}, {"name": "Haiti", "code": "HTI", "tempRate": "-5.0%"}, {"name": "Honduras", "code": "HND", "tempRate": "-7.4%"}, {"name": "Hong Kong", "code": "HKG", "tempRate": "-6.9%"}, {"name": "Hungary", "code": "HUN", "tempRate": "-33.2%"}, {"name": "Iceland", "code": "ISL", "tempRate": "-21.5%"}, {"name": "India", "code": "IND", "tempRate": "-3.4%"}, {"name": "Indonesia", "code": "IDN", "tempRate": "-3.3%"}, {"name": "Iran", "code": "IRN", "tempRate": "-16.2%"}, {"name": "Iraq", "code": "IRQ", "tempRate": "-13.9%"}, {"name": "Ireland", "code": "IRL", "tempRate": "-12.6%"}, {"name": "Israel", "code": "ISR", "tempRate": "-8.0%"}, {"name": "Italy", "code": "ITA", "tempRate": "-19.8%"}, {"name": "Jamaica", "code": "JAM", "tempRate": "-4.9%"}, {"name": "Japan", "code": "JPN", "tempRate": "-18.7%"}, {"name": "Jordan", "code": "JOR", "tempRate": "-12.8%"}, {"name": "Kazakhstan", "code": "KAZ", "tempRate": "-48.1%"}, {"name": "Kenya", "code": "KEN", "tempRate": "-2.4%"}, {"name": "Kiribati", "code": "KIR", "tempRate": "-3.0%"}, {"name": "Korea, North", "code": "PRK", "tempRate": "-28.5%"}, {"name": "Korea, South", "code": "KOR", "tempRate": "-25.4%"}, {"name": "Kosovo", "code": "XKS", "tempRate": "-24.9%"}, {"name": "Kuwait", "code": "KWT", "tempRate": "-10.1%"}, {"name": "Kyrgyzstan", "code": "KGZ", "tempRate": "-23.2%"}, {"name": "Laos", "code": "LAO", "tempRate": "-6.3%"}, {"name": "Latvia", "code": "LVA", "tempRate": "-48.1%"}, {"name": "Lebanon", "code": "LBN", "tempRate": "-11.0%"}, {"name": "Lesotho", "code": "LSO", "tempRate": "9.9%"}, {"name": "Liberia", "code": "LBR", "tempRate": "-3.2%"}, {"name": "Libya", "code": "LBY", "tempRate": "-8.5%"}, {"name": "Liechtenstein", "code": "LIE", "tempRate": "-54.6%"}, {"name": "Lithuania", "code": "LTU", "tempRate": "-54.6%"}, {"name": "Luxembourg", "code": "LUX", "tempRate": "-34.7%"}, {"name": "Macau", "code": "MAC", "tempRate": "-6.8%"}, {"name": "Macedonia", "code": "MKD", "tempRate": "-24.9%"}, {"name": "Madagascar", "code": "MDG", "tempRate": "0.4%"}, {"name": "Malawi", "code": "MWI", "tempRate": "0.9%"}, {"name": "Malaysia", "code": "MYS", "tempRate": "-4.0%"}, {"name": "Maldives", "code": "MDV", "tempRate": "-3.4%"}, {"name": "Mali", "code": "MLI", "tempRate": "-2.7%"}, {"name": "Malta", "code": "MLT", "tempRate": "-9.2%"}, {"name": "Marshall Islands", "code": "MHL", "tempRate": "-2.1%"}, {"name": "Mauritania", "code": "MRT", "tempRate": "-5.0%"}, {"name": "Mauritius", "code": "MUS", "tempRate": "0.7%"}, {"name": "Mexico", "code": "MEX", "tempRate": "-8.6%"}, {"name": "Micronesia, Federated States Of", "code": "FSM", "tempRate": "-2.7%"}, {"name": "Moldova", "code": "MDA", "tempRate": "-41.9%"}, {"name": "Monaco", "code": "MCO", "tempRate": "-19.8%"}, {"name": "Mongolia", "code": "MNG", "tempRate": "-192.5%"}, {"name": "Montenegro", "code": "MNE", "tempRate": "-24.2%"}, {"name": "Morocco", "code": "MAR", "tempRate": "-10.1%"}, {"name": "Mozambique", "code": "MOZ", "tempRate": "0.3%"}, {"name": "Namibia", "code": "NAM", "tempRate": "-2.2%"}, {"name": "Nepal", "code": "NPL", "tempRate": "-3.8%"}, {"name": "Netherlands", "code": "NLD", "tempRate": "-25.6%"}, {"name": "New Zealand", "code": "NZL", "tempRate": "-4.8%"}, {"name": "Nicaragua", "code": "NIC", "tempRate": "-3.6%"}, {"name": "Niger", "code": "NER", "tempRate": "-2.9%"}, {"name": "Nigeria", "code": "NGA", "tempRate": "-3.3%"}, {"name": "Northern Mariana Islands", "code": "MNP", "tempRate": "-1.7%"}, {"name": "Norway", "code": "NOR", "tempRate": "-55.7%"}, {"name": "Oman", "code": "OMN", "tempRate": "-2.3%"}, {"name": "Pakistan", "code": "PAK", "tempRate": "-7.7%"}, {"name": "Palau", "code": "PLW", "tempRate": "-2.5%"}, {"name": "Panama", "code": "PAN", "tempRate": "-2.2%"}, {"name": "Papua New Guinea", "code": "PNG", "tempRate": "-2.5%"}, {"name": "Paraguay", "code": "PRY", "tempRate": "-2.1%"}, {"name": "Peru", "code": "PER", "tempRate": "-1.1%"}, {"name": "Philippines", "code": "PHL", "tempRate": "-4.0%"}, {"name": "Poland", "code": "POL", "tempRate": "-40.7%"}, {"name": "Portugal", "code": "PRT", "tempRate": "-13.1%"}, {"name": "Qatar", "code": "QAT", "tempRate": "-6.0%"}, {"name": "Romania", "code": "ROU", "tempRate": "-35.4%"}, {"name": "Russia", "code": "RUS", "tempRate": "-67.0%"}, {"name": "Rwanda", "code": "RWA", "tempRate": "-7.8%"}, {"name": "Saint Kitts And Nevis", "code": "KNA", "tempRate": "-1.3%"}, {"name": "Saint Lucia", "code": "LCA", "tempRate": "-2.4%"}, {"name": "Saint Vincent And The Grenadines", "code": "VCT", "tempRate": "-1.8%"}, {"name": "Samoa", "code": "WSM", "tempRate": "-1.9%"}, {"name": "San Marino", "code": "SMR", "tempRate": "-22.1%"}, {"name": "Sao Tome And Principe", "code": "STP", "tempRate": "-4.4%"}, {"name": "Saudi Arabia", "code": "SAU", "tempRate": "-7.8%"}, {"name": "Senegal", "code": "SEN", "tempRate": "-1.4%"}, {"name": "Serbia", "code": "SRB", "tempRate": "-28.1%"}, {"name": "Seychelles", "code": "SYC", "tempRate": "-2.9%"}, {"name": "Sierra Leone", "code": "SLE", "tempRate": "-3.3%"}, {"name": "Singapore", "code": "SGP", "tempRate": "-2.2%"}, {"name": "Sint Maarten", "code": "SXM", "tempRate": "-1.3%"}, {"name": "Slovakia", "code": "SVK", "tempRate": "-33.0%"}, {"name": "Slovenia", "code": "SVN", "tempRate": "-37.0%"}, {"name": "Solomon Islands", "code": "SLB", "tempRate": "-3.6%"}, {"name": "Somalia", "code": "SOM", "tempRate": "-2.7%"}, {"name": "South Africa", "code": "ZAF", "tempRate": "1.5%"}, {"name": "South Sudan", "code": "SSD", "tempRate": "-4.2%"}, {"name": "Spain", "code": "ESP", "tempRate": "-15.6%"}, {"name": "Sri Lanka", "code": "LKA", "tempRate": "-3.7%"}, {"name": "Sudan", "code": "SDN", "tempRate": "-1.7%"}, {"name": "Suriname", "code": "SUR", "tempRate": "-3.2%"}, {"name": "Swaziland", "code": "SWZ", "tempRate": "0.7%"}, {"name": "Sweden", "code": "SWE", "tempRate": "-40.6%"}, {"name": "Switzerland", "code": "CHE", "tempRate": "-36.4%"}, {"name": "Syria", "code": "SYR", "tempRate": "-15.5%"}, {"name": "Taiwan", "code": "TWN", "tempRate": "-7.2%"}, {"name": "Tajikistan", "code": "TJK", "tempRate": "-18.2%"}, {"name": "Tanzania", "code": "TZA", "tempRate": "-0.8%"}, {"name": "Thailand", "code": "THA", "tempRate": "-4.1%"}, {"name": "Timor-Leste", "code": "TLS", "tempRate": "-2.2%"}, {"name": "Togo", "code": "TGO", "tempRate": "-2.6%"}, {"name": "Tonga", "code": "TON", "tempRate": "-3.7%"}, {"name": "Trinidad And Tobago", "code": "TTO", "tempRate": "-2.6%"}, {"name": "Tunisia", "code": "TUN", "tempRate": "-13.3%"}, {"name": "Turkey", "code": "TUR", "tempRate": "-17.6%"}, {"name": "Turkmenistan", "code": "TKM", "tempRate": "-19.8%"}, {"name": "Tuvalu", "code": "TUV", "tempRate": "-1.4%"}, {"name": "Uganda", "code": "UGA", "tempRate": "-3.9%"}, {"name": "Ukraine", "code": "UKR", "tempRate": "-43.4%"}, {"name": "United Arab Emirates", "code": "ARE", "tempRate": "-6.3%"}, {"name": "United Kingdom", "code": "GBR", "tempRate": "-20.4%"}, {"name": "United States", "code": "USA", "tempRate": "-18.9%"}, {"name": "Uruguay", "code": "URY", "tempRate": "3.3%"}, {"name": "Uzbekistan", "code": "UZB", "tempRate": "-18.1%"}, {"name": "Vanuatu", "code": "VUT", "tempRate": "-2.7%"}, {"name": "Venezuela", "code": "VEN", "tempRate": "-3.9%"}, {"name": "Vietnam", "code": "VNM", "tempRate": "-5.6%"}, {"name": "West Bank", "code": "XWB", "tempRate": "-10.5%"}, {"name": "Yemen", "code": "YEM", "tempRate": "-3.0%"}, {"name": "Zambia", "code": "ZMB", "tempRate": "-0.2%"}, {"name": "Zimbabwe", "code": "ZWE", "tempRate": "-1.1%"}]
        }
    },
    mounted() {
        this.readGeoJson().then(this.initMap);
    },
    beforeDestroy(){
        this.map.off();
        this.map.remove();
        this.map = null;
    },
    methods: {
        async readGeoJson(){
            this.worldData = await d3.json("static/world-110.geojson");
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
            return d == undefined ? "white" :
                d > 0.30 ? '#800026' :
                d > 0.25  ? '#BD0026' :
                d > 0.20  ? '#E31A1C' :
                d > 0.15  ? '#FC4E2A' :
                d > 0.10   ? '#FD8D3C' :
                d > 0.05   ? '#FEB24C' :
                d > 0   ? '#FED976' : '#FFEDA0';
        },
        style(feature) {
            return {
                weight: 1,
                opacity: 1,
                color: 'white',
                dashArray: '2',
                fillOpacity: 1,
                // TODO: add to geoJson
                // fillColor : 0
                fillColor: this.getColor(feature.properties.tempRate)
            };
        },
        highlightFeature(e) {
            const layer = e.target;

            layer.setStyle({
                weight: 3,
                color: 'black',
                dashArray: '1',
                fillOpacity: 1
            });

            layer.bringToFront();

            this.info.update(layer.feature.properties);
        },
        resetHighlight(e) {
            this.geojson.resetStyle(e.target);
            this.info.update();
        },
        zoomToFeature(e) {
            this.map.fitBounds(e.target.getBounds());
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
            const grades = ["<0%", '0%', '5%', "10%", "15%", "20%", "25%", "30%"];
            const labels = [];
            let from, to;
            for (let i = 0; i < grades.length; i++) {
                from = grades[i];
                to = grades[i + 1];

                labels.push(`<i style="background:${this.getColor(i*0.05 - 0.01)}"></i> ${from}${to ? `&ndash;${to}` : '+'}`);
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
                const contents = props ? `<b>${props.name}</b><br />${(props.tempRate * 100).toFixed(1)}% Change` : 'Hover over a region';
                this._div.innerHTML = `<h4>Temperature Changing Rate</h4>${contents}`;
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
            // temperature
            this.temperature = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: this.maxZoom,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }).addTo(this.map);

            // CO2
            this.CO2 = L.tileLayer(
                'http://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
                maxZoom: this.maxZoom,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            });

            this.allOptions = {
                "Temperature Changing Rate": this.temperature,
                "Carbon Emission increasing Rate": this.CO2,
            };

            console.log('add layers');
            // Add baseLayers to map as control layers
            L.control.layers(this.allOptions).addTo(this.map);

        },
        addTempData(){
            console.log('add tempdata');
            // console.log(this.worldData);
		    console.log(Array.isArray(this.tempGeoJson));
            if (Array.isArray(this.tempGeoJson)){
                var dataJson = JSON.parse(JSON.stringify(this.tempGeoJson));
                this.worldJson = JSON.parse(JSON.stringify(this.worldData)); // For Deep Cloning so that gj does not get changed
                for (let i of this.worldJson.features) {
                    var tempRate = dataJson.find((item) => item.name == i.properties.name);
                    if (tempRate != undefined) {
                        i.properties.tempRate = (-1 * tempRate.tempRate.replace("%","") / 100).toFixed(5);
                       
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
            this.setToolTips();
            this.setInfo();
            this.setLayers();
            this.addTempData();
        
            this.legend = L.control({position: 'bottomright'});
            this.legend.onAdd = this.addLegend;
            this.legend.addTo(this.map);

        },
        showCities(country){
            // TODO: post city

            // Add a svg layer to the map
            L.svg().addTo(map);
            var markers = [
                {lng: 7.26, lat: 43.71, popu: 1231}, // nice
                {lng: 2.349, lat: 48.864, popu: 12312}, // Paris
            ];
            for (let i in markers) {
                city = {}
                city.lat = markers[i].lat
                city.lng = markers[i].lng
                L.circleMarker(city, {
                    color: 'red',
                    fillColor: 'red',
                    fillOpacity: 0.5,
                    radius: 12,
                    zIndexOffset: 9999
                }).bringToFront().addTo(this.map).bindPopup(markers[i].name);
            }
        }
    }
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
</style>

<style>
    #map { width: 850px; height: 530px; }
    .info { padding: 6px 8px; font: 14px/16px Arial, Helvetica, sans-serif; background: white; background: rgba(255,255,255,0.8); box-shadow: 0 0 15px rgba(0,0,0,0.2); border-radius: 5px; } .info h4 { margin: 0 0 5px; color: #777; }
    .legend { text-align: left; line-height: 18px; color: #555; } .legend i { width: 18px; height: 18px; float: left; margin-right: 8px; opacity: 0.7; }
</style>
