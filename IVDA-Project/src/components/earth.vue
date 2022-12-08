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
            cityMarkers : null,
            placeSelection: null,
            scaleSelection: null,
            cityInfo:[{"long": "121.4365", "lat": "31.2165", "popu": "14987000.0", "tempRate": "-20.3%", "co2Rate": null}, {"long": "116.3883", "lat": "39.9289", "popu": "11106000.0", "tempRate": "-27.7%", "co2Rate": null}, {"long": "113.325", "lat": "23.145", "popu": "8829000.0", "tempRate": "-7.3%", "co2Rate": null}, {"long": "114.1221", "lat": "22.5524", "popu": "7581000.0", "tempRate": "-7.6%", "co2Rate": null}, {"long": "114.27", "lat": "30.58", "popu": "7243000.0", "tempRate": "-16.3%", "co2Rate": null}, {"long": "117.2", "lat": "39.13", "popu": "7180000.0", "tempRate": "-26.1%", "co2Rate": null}, {"long": "106.595", "lat": "29.565", "popu": "6461000.0", "tempRate": "-10.7%", "co2Rate": null}, {"long": "123.45", "lat": "41.805", "popu": "4787000.0", "tempRate": "-41.3%", "co2Rate": null}, {"long": "113.7447", "lat": "23.0489", "popu": "4528000.0", "tempRate": "-7.4%", "co2Rate": null}, {"long": "104.07", "lat": "30.67", "popu": "4123000.0", "tempRate": "-15.5%", "co2Rate": null}, {"long": "108.895", "lat": "34.275", "popu": "4009000.0", "tempRate": "-16.6%", "co2Rate": null}, {"long": "109.6091", "lat": "23.0965", "popu": "3830000.0", "tempRate": "-6.7%", "co2Rate": null}, {"long": "118.78", "lat": "32.05", "popu": "3679000.0", "tempRate": "-21.4%", "co2Rate": null}, {"long": "106.72", "lat": "26.58", "popu": "3662000.0", "tempRate": "-13.0%", "co2Rate": null}, {"long": "126.65", "lat": "45.75", "popu": "3621000.0", "tempRate": "-63.2%", "co2Rate": null}, {"long": "117.67", "lat": "24.5204", "popu": "3531147.0", "tempRate": "-10.6%", "co2Rate": null}, {"long": "125.34", "lat": "43.865", "popu": "3183000.0", "tempRate": "-53.8%", "co2Rate": null}, {"long": "121.6298", "lat": "38.9228", "popu": "3167000.0", "tempRate": "-24.3%", "co2Rate": null}, {"long": "118.05", "lat": "36.8", "popu": "3061000.0", "tempRate": "-26.2%", "co2Rate": null}, {"long": "120.17", "lat": "30.25", "popu": "3007000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "102.68", "lat": "25.07", "popu": "2931000.0", "tempRate": "-10.1%", "co2Rate": null}, {"long": "112.5451", "lat": "37.875", "popu": "2913000.0", "tempRate": "-34.2%", "co2Rate": null}, {"long": "120.33", "lat": "36.09", "popu": "2866000.0", "tempRate": "-21.0%", "co2Rate": null}, {"long": "116.995", "lat": "36.675", "popu": "2798000.0", "tempRate": "-25.0%", "co2Rate": null}, {"long": "113.6651", "lat": "34.755", "popu": "2636000.0", "tempRate": "-21.2%", "co2Rate": null}, {"long": "119.3", "lat": "26.08", "popu": "2606000.0", "tempRate": "-12.5%", "co2Rate": null}, {"long": "112.97", "lat": "28.2", "popu": "2604000.0", "tempRate": "-14.2%", "co2Rate": null}, {"long": "112.9", "lat": "27.8504", "popu": "2586948.0", "tempRate": "-14.3%", "co2Rate": null}, {"long": "103.792", "lat": "36.056", "popu": "2561000.0", "tempRate": "-26.6%", "co2Rate": null}, {"long": "118.08", "lat": "24.45", "popu": "2519000.0", "tempRate": "-9.1%", "co2Rate": null}, {"long": "120.83", "lat": "40.7503", "popu": "2426000.0", "tempRate": "-31.1%", "co2Rate": null}, {"long": "114.48", "lat": "38.05", "popu": "2417000.0", "tempRate": "-19.2%", "co2Rate": null}, {"long": "126.55", "lat": "43.85", "popu": "2396000.0", "tempRate": "-60.5%", "co2Rate": null}, {"long": "115.88", "lat": "28.68", "popu": "2350000.0", "tempRate": "-16.1%", "co2Rate": null}, {"long": "120.6501", "lat": "28.02", "popu": "2350000.0", "tempRate": "-15.7%", "co2Rate": null}, {"long": "106.13", "lat": "30.7804", "popu": "2174000.0", "tempRate": "-11.8%", "co2Rate": null}, {"long": "108.32", "lat": "22.82", "popu": "2167000.0", "tempRate": "-7.0%", "co2Rate": null}, {"long": "87.575", "lat": "43.805", "popu": "2151000.0", "tempRate": "-52.5%", "co2Rate": null}, {"long": "117.57", "lat": "34.88", "popu": "2145000.0", "tempRate": "-26.0%", "co2Rate": null}, {"long": "121.4", "lat": "37.5304", "popu": "2116000.0", "tempRate": "-24.7%", "co2Rate": null}, {"long": "117.18", "lat": "34.28", "popu": "2091000.0", "tempRate": "-23.3%", "co2Rate": null}, {"long": "118.33", "lat": "35.08", "popu": "2082000.0", "tempRate": "-25.5%", "co2Rate": null}, {"long": "110.32", "lat": "20.05", "popu": "2046189.0", "tempRate": "-6.5%", "co2Rate": null}, {"long": "109.822", "lat": "40.6522", "popu": "2036000.0", "tempRate": "-45.4%", "co2Rate": null}, {"long": "117.28", "lat": "31.85", "popu": "2035000.0", "tempRate": "-20.2%", "co2Rate": null}, {"long": "116.9789", "lat": "33.6361", "popu": "1964000.0", "tempRate": "-22.4%", "co2Rate": null}, {"long": "112.53", "lat": "33.0004", "popu": "1944000.0", "tempRate": "-20.1%", "co2Rate": null}, {"long": "121.55", "lat": "29.88", "popu": "1923000.0", "tempRate": "-17.2%", "co2Rate": null}, {"long": "118.1944", "lat": "39.6243", "popu": "1879000.0", "tempRate": "-29.2%", "co2Rate": null}, {"long": "113.3", "lat": "40.08", "popu": "1873000.0", "tempRate": "-45.1%", "co2Rate": null}, {"long": "118.7734", "lat": "34.1299", "popu": "1770000.0", "tempRate": "-22.9%", "co2Rate": null}, {"long": "115.65", "lat": "34.4504", "popu": "1753000.0", "tempRate": "-23.7%", "co2Rate": null}, {"long": "120.3", "lat": "31.58", "popu": "1749000.0", "tempRate": "-21.5%", "co2Rate": null}, {"long": "111.66", "lat": "40.82", "popu": "1726000.0", "tempRate": "-60.4%", "co2Rate": null}, {"long": "112.4701", "lat": "34.68", "popu": "1715000.0", "tempRate": "-20.5%", "co2Rate": null}, {"long": "113.16", "lat": "30.6501", "popu": "1708000.0", "tempRate": "-15.4%", "co2Rate": null}, {"long": "125.0", "lat": "46.58", "popu": "1693000.0", "tempRate": "-62.9%", "co2Rate": null}, {"long": "116.48", "lat": "31.7503", "popu": "1690000.0", "tempRate": "-21.0%", "co2Rate": null}, {"long": "108.4", "lat": "30.82", "popu": "1680000.0", "tempRate": "-11.8%", "co2Rate": null}, {"long": "120.62", "lat": "31.3005", "popu": "1650000.0", "tempRate": "-21.2%", "co2Rate": null}, {"long": "123.99", "lat": "47.345", "popu": "1641000.0", "tempRate": "-65.9%", "co2Rate": null}, {"long": "122.94", "lat": "41.115", "popu": "1639000.0", "tempRate": "-37.2%", "co2Rate": null}, {"long": "114.48", "lat": "36.58", "popu": "1631000.0", "tempRate": "-21.8%", "co2Rate": null}, {"long": "117.1201", "lat": "36.2", "popu": "1629000.0", "tempRate": "-28.5%", "co2Rate": null}, {"long": "116.67", "lat": "23.37", "popu": "1601000.0", "tempRate": "-8.7%", "co2Rate": null}, {"long": "110.38", "lat": "21.2", "popu": "1590000.0", "tempRate": "-6.7%", "co2Rate": null}, {"long": "113.44", "lat": "30.3704", "popu": "1556000.0", "tempRate": "-15.3%", "co2Rate": null}, {"long": "119.1001", "lat": "36.7204", "popu": "1553000.0", "tempRate": "-26.5%", "co2Rate": null}, {"long": "114.07", "lat": "32.1304", "popu": "1541000.0", "tempRate": "-19.3%", "co2Rate": null}, {"long": "105.38", "lat": "28.88", "popu": "1537000.0", "tempRate": "-11.4%", "co2Rate": null}, {"long": "114.95", "lat": "25.92", "popu": "1500000.0", "tempRate": "-13.2%", "co2Rate": null}, {"long": "109.25", "lat": "24.28", "popu": "1497000.0", "tempRate": "-9.3%", "co2Rate": null}, {"long": "123.87", "lat": "41.8654", "popu": "1470000.0", "tempRate": "-43.7%", "co2Rate": null}, {"long": "111.68", "lat": "29.03", "popu": "1469000.0", "tempRate": "-13.3%", "co2Rate": null}, {"long": "105.05", "lat": "29.5804", "popu": "1466000.0", "tempRate": "-13.7%", "co2Rate": null}, {"long": "118.58", "lat": "24.9", "popu": "1463000.0", "tempRate": "-10.2%", "co2Rate": null}, {"long": "116.98", "lat": "32.63", "popu": "1451000.0", "tempRate": "-21.8%", "co2Rate": null}, {"long": "105.5333", "lat": "30.5333", "popu": "1425000.0", "tempRate": "-12.8%", "co2Rate": null}, {"long": "104.77", "lat": "31.47", "popu": "1396000.0", "tempRate": "-15.1%", "co2Rate": null}, {"long": "118.48", "lat": "31.7304", "popu": "1366302.0", "tempRate": "-20.8%", "co2Rate": null}, {"long": "112.33", "lat": "28.6004", "popu": "1352000.0", "tempRate": "-13.9%", "co2Rate": null}, {"long": "115.45", "lat": "35.23", "popu": "1338000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "119.97", "lat": "31.78", "popu": "1327000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "118.95", "lat": "42.27", "popu": "1277000.0", "tempRate": "-41.6%", "co2Rate": null}, {"long": "119.03", "lat": "33.58", "popu": "1264000.0", "tempRate": "-22.6%", "co2Rate": null}, {"long": "129.59", "lat": "44.575", "popu": "1244000.0", "tempRate": "-67.5%", "co2Rate": null}, {"long": "120.1", "lat": "30.8704", "popu": "1231000.0", "tempRate": "-20.7%", "co2Rate": null}, {"long": "105.92", "lat": "34.6", "popu": "1225000.0", "tempRate": "-23.4%", "co2Rate": null}, {"long": "104.8333", "lat": "26.5944", "popu": "1221000.0", "tempRate": "-14.4%", "co2Rate": null}, {"long": "110.87", "lat": "21.9204", "popu": "1217715.0", "tempRate": "-5.6%", "co2Rate": null}, {"long": "116.55", "lat": "35.4004", "popu": "1186000.0", "tempRate": "-24.5%", "co2Rate": null}, {"long": "103.7333", "lat": "29.5671", "popu": "1157000.0", "tempRate": "-14.4%", "co2Rate": null}, {"long": "117.97", "lat": "28.4704", "popu": "1144577.0", "tempRate": "-16.7%", "co2Rate": null}, {"long": "110.15", "lat": "22.63", "popu": "1127000.0", "tempRate": "-5.8%", "co2Rate": null}, {"long": "108.7147", "lat": "34.3456", "popu": "1126000.0", "tempRate": "-16.7%", "co2Rate": null}, {"long": "115.48", "lat": "38.8704", "popu": "1107000.0", "tempRate": "-21.1%", "co2Rate": null}, {"long": "104.78", "lat": "29.4", "popu": "1105000.0", "tempRate": "-13.9%", "co2Rate": null}, {"long": "109.02", "lat": "32.68", "popu": "1100000.0", "tempRate": "-16.3%", "co2Rate": null}, {"long": "119.65", "lat": "29.12", "popu": "1092852.0", "tempRate": "-19.2%", "co2Rate": null}, {"long": "113.15", "lat": "27.83", "popu": "1080000.0", "tempRate": "-14.1%", "co2Rate": null}, {"long": "112.13", "lat": "32.02", "popu": "1069000.0", "tempRate": "-18.0%", "co2Rate": null}, {"long": "119.3801", "lat": "35.99", "popu": "1060000.0", "tempRate": "-26.6%", "co2Rate": null}, {"long": "101.77", "lat": "36.62", "popu": "1048000.0", "tempRate": "-44.6%", "co2Rate": null}, {"long": "114.93", "lat": "40.83", "popu": "1046000.0", "tempRate": "-49.6%", "co2Rate": null}, {"long": "113.5678", "lat": "22.2769", "popu": "1023000.0", "tempRate": "-6.9%", "co2Rate": null}, {"long": "130.35", "lat": "46.83", "popu": "1020000.0", "tempRate": "-70.9%", "co2Rate": null}, {"long": "112.59", "lat": "26.88", "popu": "1016000.0", "tempRate": "-14.5%", "co2Rate": null}, {"long": "123.75", "lat": "41.3304", "popu": "1012000.0", "tempRate": "-47.4%", "co2Rate": null}, {"long": "119.62", "lat": "39.9304", "popu": "1003000.0", "tempRate": "-29.8%", "co2Rate": null}, {"long": "111.62", "lat": "26.2304", "popu": "1000000.0", "tempRate": "-14.1%", "co2Rate": null}, {"long": "99.15", "lat": "25.12", "popu": "1000000.0", "tempRate": "-10.2%", "co2Rate": null}, {"long": "106.273", "lat": "38.468", "popu": "991000.0", "tempRate": "-28.9%", "co2Rate": null}, {"long": "120.75", "lat": "30.7704", "popu": "988000.0", "tempRate": "-20.5%", "co2Rate": null}, {"long": "110.28", "lat": "25.28", "popu": "987000.0", "tempRate": "-10.1%", "co2Rate": null}, {"long": "114.4", "lat": "27.8333", "popu": "982000.0", "tempRate": "-15.4%", "co2Rate": null}, {"long": "113.57", "lat": "37.87", "popu": "981448.0", "tempRate": "-28.8%", "co2Rate": null}, {"long": "130.97", "lat": "45.3", "popu": "965000.0", "tempRate": "-65.4%", "co2Rate": null}, {"long": "118.35", "lat": "34.38", "popu": "962656.0", "tempRate": "-23.3%", "co2Rate": null}, {"long": "113.85", "lat": "27.62", "popu": "961000.0", "tempRate": "-14.9%", "co2Rate": null}, {"long": "121.1", "lat": "41.1204", "popu": "956000.0", "tempRate": "-34.7%", "co2Rate": null}, {"long": "120.825", "lat": "32.0304", "popu": "947000.0", "tempRate": "-22.6%", "co2Rate": null}, {"long": "113.12", "lat": "23.0301", "popu": "943000.0", "tempRate": "-7.2%", "co2Rate": null}, {"long": "116.75", "lat": "33.9504", "popu": "913000.0", "tempRate": "-22.8%", "co2Rate": null}, {"long": "114.93", "lat": "27.8", "popu": "913000.0", "tempRate": "-15.9%", "co2Rate": null}, {"long": "113.87", "lat": "35.3204", "popu": "903000.0", "tempRate": "-21.2%", "co2Rate": null}, {"long": "104.57", "lat": "28.77", "popu": "902000.0", "tempRate": "-12.9%", "co2Rate": null}, {"long": "117.33", "lat": "32.95", "popu": "894000.0", "tempRate": "-21.9%", "co2Rate": null}, {"long": "114.35", "lat": "36.08", "popu": "887000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "122.27", "lat": "43.62", "popu": "884000.0", "tempRate": "-42.6%", "co2Rate": null}, {"long": "111.28", "lat": "30.7", "popu": "875000.0", "tempRate": "-13.6%", "co2Rate": null}, {"long": "111.97", "lat": "21.8504", "popu": "872363.0", "tempRate": "-6.2%", "co2Rate": null}, {"long": "114.35", "lat": "34.85", "popu": "872000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "124.3936", "lat": "40.1436", "popu": "870000.0", "tempRate": "-35.2%", "co2Rate": null}, {"long": "118.7553", "lat": "30.9525", "popu": "866000.0", "tempRate": "-21.7%", "co2Rate": null}, {"long": "119.45", "lat": "35.4304", "popu": "865000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "113.22", "lat": "35.25", "popu": "857000.0", "tempRate": "-23.5%", "co2Rate": null}, {"long": "119.43", "lat": "32.22", "popu": "854000.0", "tempRate": "-22.0%", "co2Rate": null}, {"long": "113.3", "lat": "33.7304", "popu": "849000.0", "tempRate": "-20.6%", "co2Rate": null}, {"long": "106.92", "lat": "27.7", "popu": "849000.0", "tempRate": "-14.3%", "co2Rate": null}, {"long": "105.93", "lat": "26.2504", "popu": "849000.0", "tempRate": "-12.7%", "co2Rate": null}, {"long": "112.73", "lat": "37.6804", "popu": "840000.0", "tempRate": "-31.1%", "co2Rate": null}, {"long": "120.1253", "lat": "33.3856", "popu": "839000.0", "tempRate": "-23.4%", "co2Rate": null}, {"long": "111.52", "lat": "36.0803", "popu": "834000.0", "tempRate": "-25.0%", "co2Rate": null}, {"long": "113.1", "lat": "29.3801", "popu": "826000.0", "tempRate": "-14.3%", "co2Rate": null}, {"long": "104.89", "lat": "25.0904", "popu": "816000.0", "tempRate": "-12.2%", "co2Rate": null}, {"long": "118.37", "lat": "31.3504", "popu": "810000.0", "tempRate": "-20.4%", "co2Rate": null}, {"long": "116.68", "lat": "39.5204", "popu": "810000.0", "tempRate": "-25.4%", "co2Rate": null}, {"long": "103.72", "lat": "27.3204", "popu": "809000.0", "tempRate": "-17.3%", "co2Rate": null}, {"long": "119.4011", "lat": "41.24", "popu": "806000.0", "tempRate": "-39.6%", "co2Rate": null}, {"long": "107.15", "lat": "34.38", "popu": "800000.0", "tempRate": "-21.3%", "co2Rate": null}, {"long": "122.28", "lat": "40.6703", "popu": "795000.0", "tempRate": "-34.8%", "co2Rate": null}, {"long": "123.18", "lat": "41.28", "popu": "794000.0", "tempRate": "-38.3%", "co2Rate": null}, {"long": "120.57", "lat": "30.0004", "popu": "777000.0", "tempRate": "-20.7%", "co2Rate": null}, {"long": "128.9", "lat": "47.6999", "popu": "777000.0", "tempRate": "-105.0%", "co2Rate": null}, {"long": "119.9519", "lat": "30.0533", "popu": "771000.0", "tempRate": "-21.5%", "co2Rate": null}, {"long": "121.66", "lat": "42.0105", "popu": "770000.0", "tempRate": "-42.5%", "co2Rate": null}, {"long": "110.78", "lat": "32.57", "popu": "770000.0", "tempRate": "-17.8%", "co2Rate": null}, {"long": "112.83", "lat": "35.5004", "popu": "760000.0", "tempRate": "-28.3%", "co2Rate": null}, {"long": "130.37", "lat": "47.4", "popu": "743307.0", "tempRate": "-78.7%", "co2Rate": null}, {"long": "109.1", "lat": "21.4804", "popu": "728978.0", "tempRate": "-7.1%", "co2Rate": null}, {"long": "113.58", "lat": "24.8", "popu": "720266.0", "tempRate": "-8.9%", "co2Rate": null}, {"long": "119.17", "lat": "34.6004", "popu": "715600.0", "tempRate": "-22.2%", "co2Rate": null}, {"long": "113.0301", "lat": "23.7004", "popu": "706717.0", "tempRate": "-7.6%", "co2Rate": null}, {"long": "113.1053", "lat": "36.1839", "popu": "706000.0", "tempRate": "-30.2%", "co2Rate": null}, {"long": "115.1", "lat": "30.22", "popu": "688090.0", "tempRate": "-15.7%", "co2Rate": null}, {"long": "114.98", "lat": "35.7004", "popu": "666322.0", "tempRate": "-20.7%", "co2Rate": null}, {"long": "103.8166", "lat": "25.6005", "popu": "652604.0", "tempRate": "-10.9%", "co2Rate": null}, {"long": "115.79", "lat": "39.5401", "popu": "628000.0", "tempRate": "-25.9%", "co2Rate": null}, {"long": "116.1944", "lat": "40.2248", "popu": "614821.0", "tempRate": "-32.5%", "co2Rate": null}, {"long": "119.9", "lat": "32.4904", "popu": "612356.0", "tempRate": "-22.6%", "co2Rate": null}, {"long": "114.5", "lat": "37.05", "popu": "611739.0", "tempRate": "-21.7%", "co2Rate": null}, {"long": "117.05", "lat": "30.5", "popu": "580497.0", "tempRate": "-18.3%", "co2Rate": null}, {"long": "86.0299", "lat": "44.3", "popu": "573182.0", "tempRate": "-48.7%", "co2Rate": null}, {"long": "112.42", "lat": "39.3004", "popu": "570000.0", "tempRate": "-47.8%", "co2Rate": null}, {"long": "117.78", "lat": "30.9504", "popu": "562832.0", "tempRate": "-19.5%", "co2Rate": null}, {"long": "122.1", "lat": "37.5", "popu": "560255.0", "tempRate": "-21.4%", "co2Rate": null}, {"long": "124.33", "lat": "43.17", "popu": "555609.0", "tempRate": "-48.8%", "co2Rate": null}, {"long": "115.98", "lat": "29.73", "popu": "545616.0", "tempRate": "-16.8%", "co2Rate": null}, {"long": "75.9699", "lat": "39.4763", "popu": "543914.0", "tempRate": "-22.7%", "co2Rate": null}, {"long": "119.43", "lat": "32.4", "popu": "539715.0", "tempRate": "-22.1%", "co2Rate": null}],
            tempGeoJson: [{"name": "Afghanistan", "code": "AFG", "tempRate": "-13.3%"}, {"name": "Albania", "code": "ALB", "tempRate": "-17.1%"}, {"name": "Algeria", "code": "DZA", "tempRate": "-14.7%"}, {"name": "American Samoa", "code": "ASM", "tempRate": "-2.0%"}, {"name": "Andorra", "code": "AND", "tempRate": "-45.0%"}, {"name": "Angola", "code": "AGO", "tempRate": "-3.0%"}, {"name": "Antigua And Barbuda", "code": "ATG", "tempRate": "-1.3%"}, {"name": "Argentina", "code": "ARG", "tempRate": "4.6%"}, {"name": "Armenia", "code": "ARM", "tempRate": "-23.9%"}, {"name": "Aruba", "code": "ABW", "tempRate": "-1.1%"}, {"name": "Australia", "code": "AUS", "tempRate": "4.3%"}, {"name": "Austria", "code": "AUT", "tempRate": "-34.5%"}, {"name": "Azerbaijan", "code": "AZE", "tempRate": "-14.7%"}, {"name": "Bahamas, The", "code": "BHS", "tempRate": "-4.1%"}, {"name": "Bahrain", "code": "BHR", "tempRate": "-4.2%"}, {"name": "Bangladesh", "code": "BGD", "tempRate": "-2.5%"}, {"name": "Barbados", "code": "BRB", "tempRate": "-1.4%"}, {"name": "Belarus", "code": "BLR", "tempRate": "-57.3%"}, {"name": "Belgium", "code": "BEL", "tempRate": "-29.6%"}, {"name": "Belize", "code": "BLZ", "tempRate": "-9.0%"}, {"name": "Benin", "code": "BEN", "tempRate": "-2.5%"}, {"name": "Bhutan", "code": "BTN", "tempRate": "-13.7%"}, {"name": "Bolivia", "code": "BOL", "tempRate": "-5.6%"}, {"name": "Bosnia And Herzegovina", "code": "BIH", "tempRate": "-34.1%"}, {"name": "Botswana", "code": "BWA", "tempRate": "0.7%"}, {"name": "Brazil", "code": "BRA", "tempRate": "-0.5%"}, {"name": "Brunei", "code": "BRN", "tempRate": "-4.4%"}, {"name": "Bulgaria", "code": "BGR", "tempRate": "-25.8%"}, {"name": "Burkina Faso", "code": "BFA", "tempRate": "-2.9%"}, {"name": "Burma", "code": "MMR", "tempRate": "-4.1%"}, {"name": "Burundi", "code": "BDI", "tempRate": "-5.8%"}, {"name": "Cabo Verde", "code": "CPV", "tempRate": "-0.8%"}, {"name": "Cambodia", "code": "KHM", "tempRate": "-4.1%"}, {"name": "Cameroon", "code": "CMR", "tempRate": "-5.8%"}, {"name": "Canada", "code": "CAN", "tempRate": "-38.2%"}, {"name": "Central African Republic", "code": "CAF", "tempRate": "-6.2%"}, {"name": "Chad", "code": "TCD", "tempRate": "-3.3%"}, {"name": "Chile", "code": "CHL", "tempRate": "3.5%"}, {"name": "China", "code": "CHN", "tempRate": "-24.1%"}, {"name": "Colombia", "code": "COL", "tempRate": "-3.6%"}, {"name": "Comoros", "code": "COM", "tempRate": "-2.1%"}, {"name": "Congo (Brazzaville)", "code": "COG", "tempRate": "-5.4%"}, {"name": "Congo (Kinshasa)", "code": "COD", "tempRate": "-4.5%"}, {"name": "Costa Rica", "code": "CRI", "tempRate": "-3.2%"}, {"name": "Croatia", "code": "HRV", "tempRate": "-29.7%"}, {"name": "Cuba", "code": "CUB", "tempRate": "-5.0%"}, {"name": "Cura\u00e7ao", "code": "CUW", "tempRate": "-1.1%"}, {"name": "Cyprus", "code": "CYP", "tempRate": "-12.0%"}, {"name": "Czechia", "code": "CZE", "tempRate": "-37.5%"}, {"name": "C\u00f4te D\u2019Ivoire", "code": "CIV", "tempRate": "-3.9%"}, {"name": "Denmark", "code": "DNK", "tempRate": "-35.5%"}, {"name": "Djibouti", "code": "DJI", "tempRate": "-3.3%"}, {"name": "Dominica", "code": "DMA", "tempRate": "-1.4%"}, {"name": "Dominican Republic", "code": "DOM", "tempRate": "-3.9%"}, {"name": "Ecuador", "code": "ECU", "tempRate": "-4.1%"}, {"name": "Egypt", "code": "EGY", "tempRate": "-8.1%"}, {"name": "El Salvador", "code": "SLV", "tempRate": "-4.1%"}, {"name": "Equatorial Guinea", "code": "GNQ", "tempRate": "-3.3%"}, {"name": "Eritrea", "code": "ERI", "tempRate": "-4.4%"}, {"name": "Estonia", "code": "EST", "tempRate": "-51.2%"}, {"name": "Ethiopia", "code": "ETH", "tempRate": "-9.1%"}, {"name": "Fiji", "code": "FJI", "tempRate": "-3.7%"}, {"name": "Finland", "code": "FIN", "tempRate": "-55.0%"}, {"name": "France", "code": "FRA", "tempRate": "-25.6%"}, {"name": "Gabon", "code": "GAB", "tempRate": "-4.9%"}, {"name": "Gambia, The", "code": "GMB", "tempRate": "-3.8%"}, {"name": "Georgia", "code": "GEO", "tempRate": "-25.9%"}, {"name": "Germany", "code": "DEU", "tempRate": "-32.9%"}, {"name": "Ghana", "code": "GHA", "tempRate": "-4.7%"}, {"name": "Greece", "code": "GRC", "tempRate": "-12.8%"}, {"name": "Grenada", "code": "GRD", "tempRate": "-2.0%"}, {"name": "Guam", "code": "GUM", "tempRate": "-1.9%"}, {"name": "Guatemala", "code": "GTM", "tempRate": "-8.3%"}, {"name": "Guinea", "code": "GIN", "tempRate": "-3.1%"}, {"name": "Guinea-Bissau", "code": "GNB", "tempRate": "-2.9%"}, {"name": "Guyana", "code": "GUY", "tempRate": "-2.7%"}, {"name": "Haiti", "code": "HTI", "tempRate": "-5.0%"}, {"name": "Honduras", "code": "HND", "tempRate": "-7.4%"}, {"name": "Hong Kong", "code": "HKG", "tempRate": "-6.9%"}, {"name": "Hungary", "code": "HUN", "tempRate": "-33.2%"}, {"name": "Iceland", "code": "ISL", "tempRate": "-21.5%"}, {"name": "India", "code": "IND", "tempRate": "-3.4%"}, {"name": "Indonesia", "code": "IDN", "tempRate": "-3.3%"}, {"name": "Iran", "code": "IRN", "tempRate": "-16.2%"}, {"name": "Iraq", "code": "IRQ", "tempRate": "-13.9%"}, {"name": "Ireland", "code": "IRL", "tempRate": "-12.6%"}, {"name": "Israel", "code": "ISR", "tempRate": "-8.0%"}, {"name": "Italy", "code": "ITA", "tempRate": "-19.8%"}, {"name": "Jamaica", "code": "JAM", "tempRate": "-4.9%"}, {"name": "Japan", "code": "JPN", "tempRate": "-18.7%"}, {"name": "Jordan", "code": "JOR", "tempRate": "-12.8%"}, {"name": "Kazakhstan", "code": "KAZ", "tempRate": "-48.1%"}, {"name": "Kenya", "code": "KEN", "tempRate": "-2.4%"}, {"name": "Kiribati", "code": "KIR", "tempRate": "-3.0%"}, {"name": "Korea, North", "code": "PRK", "tempRate": "-28.5%"}, {"name": "Korea, South", "code": "KOR", "tempRate": "-25.4%"}, {"name": "Kosovo", "code": "XKS", "tempRate": "-24.9%"}, {"name": "Kuwait", "code": "KWT", "tempRate": "-10.1%"}, {"name": "Kyrgyzstan", "code": "KGZ", "tempRate": "-23.2%"}, {"name": "Laos", "code": "LAO", "tempRate": "-6.3%"}, {"name": "Latvia", "code": "LVA", "tempRate": "-48.1%"}, {"name": "Lebanon", "code": "LBN", "tempRate": "-11.0%"}, {"name": "Lesotho", "code": "LSO", "tempRate": "9.9%"}, {"name": "Liberia", "code": "LBR", "tempRate": "-3.2%"}, {"name": "Libya", "code": "LBY", "tempRate": "-8.5%"}, {"name": "Liechtenstein", "code": "LIE", "tempRate": "-54.6%"}, {"name": "Lithuania", "code": "LTU", "tempRate": "-54.6%"}, {"name": "Luxembourg", "code": "LUX", "tempRate": "-34.7%"}, {"name": "Macau", "code": "MAC", "tempRate": "-6.8%"}, {"name": "Macedonia", "code": "MKD", "tempRate": "-24.9%"}, {"name": "Madagascar", "code": "MDG", "tempRate": "0.4%"}, {"name": "Malawi", "code": "MWI", "tempRate": "0.9%"}, {"name": "Malaysia", "code": "MYS", "tempRate": "-4.0%"}, {"name": "Maldives", "code": "MDV", "tempRate": "-3.4%"}, {"name": "Mali", "code": "MLI", "tempRate": "-2.7%"}, {"name": "Malta", "code": "MLT", "tempRate": "-9.2%"}, {"name": "Marshall Islands", "code": "MHL", "tempRate": "-2.1%"}, {"name": "Mauritania", "code": "MRT", "tempRate": "-5.0%"}, {"name": "Mauritius", "code": "MUS", "tempRate": "0.7%"}, {"name": "Mexico", "code": "MEX", "tempRate": "-8.6%"}, {"name": "Micronesia, Federated States Of", "code": "FSM", "tempRate": "-2.7%"}, {"name": "Moldova", "code": "MDA", "tempRate": "-41.9%"}, {"name": "Monaco", "code": "MCO", "tempRate": "-19.8%"}, {"name": "Mongolia", "code": "MNG", "tempRate": "-192.5%"}, {"name": "Montenegro", "code": "MNE", "tempRate": "-24.2%"}, {"name": "Morocco", "code": "MAR", "tempRate": "-10.1%"}, {"name": "Mozambique", "code": "MOZ", "tempRate": "0.3%"}, {"name": "Namibia", "code": "NAM", "tempRate": "-2.2%"}, {"name": "Nepal", "code": "NPL", "tempRate": "-3.8%"}, {"name": "Netherlands", "code": "NLD", "tempRate": "-25.6%"}, {"name": "New Zealand", "code": "NZL", "tempRate": "-4.8%"}, {"name": "Nicaragua", "code": "NIC", "tempRate": "-3.6%"}, {"name": "Niger", "code": "NER", "tempRate": "-2.9%"}, {"name": "Nigeria", "code": "NGA", "tempRate": "-3.3%"}, {"name": "Northern Mariana Islands", "code": "MNP", "tempRate": "-1.7%"}, {"name": "Norway", "code": "NOR", "tempRate": "-55.7%"}, {"name": "Oman", "code": "OMN", "tempRate": "-2.3%"}, {"name": "Pakistan", "code": "PAK", "tempRate": "-7.7%"}, {"name": "Palau", "code": "PLW", "tempRate": "-2.5%"}, {"name": "Panama", "code": "PAN", "tempRate": "-2.2%"}, {"name": "Papua New Guinea", "code": "PNG", "tempRate": "-2.5%"}, {"name": "Paraguay", "code": "PRY", "tempRate": "-2.1%"}, {"name": "Peru", "code": "PER", "tempRate": "-1.1%"}, {"name": "Philippines", "code": "PHL", "tempRate": "-4.0%"}, {"name": "Poland", "code": "POL", "tempRate": "-40.7%"}, {"name": "Portugal", "code": "PRT", "tempRate": "-13.1%"}, {"name": "Qatar", "code": "QAT", "tempRate": "-6.0%"}, {"name": "Romania", "code": "ROU", "tempRate": "-35.4%"}, {"name": "Russia", "code": "RUS", "tempRate": "-67.0%"}, {"name": "Rwanda", "code": "RWA", "tempRate": "-7.8%"}, {"name": "Saint Kitts And Nevis", "code": "KNA", "tempRate": "-1.3%"}, {"name": "Saint Lucia", "code": "LCA", "tempRate": "-2.4%"}, {"name": "Saint Vincent And The Grenadines", "code": "VCT", "tempRate": "-1.8%"}, {"name": "Samoa", "code": "WSM", "tempRate": "-1.9%"}, {"name": "San Marino", "code": "SMR", "tempRate": "-22.1%"}, {"name": "Sao Tome And Principe", "code": "STP", "tempRate": "-4.4%"}, {"name": "Saudi Arabia", "code": "SAU", "tempRate": "-7.8%"}, {"name": "Senegal", "code": "SEN", "tempRate": "-1.4%"}, {"name": "Serbia", "code": "SRB", "tempRate": "-28.1%"}, {"name": "Seychelles", "code": "SYC", "tempRate": "-2.9%"}, {"name": "Sierra Leone", "code": "SLE", "tempRate": "-3.3%"}, {"name": "Singapore", "code": "SGP", "tempRate": "-2.2%"}, {"name": "Sint Maarten", "code": "SXM", "tempRate": "-1.3%"}, {"name": "Slovakia", "code": "SVK", "tempRate": "-33.0%"}, {"name": "Slovenia", "code": "SVN", "tempRate": "-37.0%"}, {"name": "Solomon Islands", "code": "SLB", "tempRate": "-3.6%"}, {"name": "Somalia", "code": "SOM", "tempRate": "-2.7%"}, {"name": "South Africa", "code": "ZAF", "tempRate": "1.5%"}, {"name": "South Sudan", "code": "SSD", "tempRate": "-4.2%"}, {"name": "Spain", "code": "ESP", "tempRate": "-15.6%"}, {"name": "Sri Lanka", "code": "LKA", "tempRate": "-3.7%"}, {"name": "Sudan", "code": "SDN", "tempRate": "-1.7%"}, {"name": "Suriname", "code": "SUR", "tempRate": "-3.2%"}, {"name": "Swaziland", "code": "SWZ", "tempRate": "0.7%"}, {"name": "Sweden", "code": "SWE", "tempRate": "-40.6%"}, {"name": "Switzerland", "code": "CHE", "tempRate": "-36.4%"}, {"name": "Syria", "code": "SYR", "tempRate": "-15.5%"}, {"name": "Taiwan", "code": "TWN", "tempRate": "-7.2%"}, {"name": "Tajikistan", "code": "TJK", "tempRate": "-18.2%"}, {"name": "Tanzania", "code": "TZA", "tempRate": "-0.8%"}, {"name": "Thailand", "code": "THA", "tempRate": "-4.1%"}, {"name": "Timor-Leste", "code": "TLS", "tempRate": "-2.2%"}, {"name": "Togo", "code": "TGO", "tempRate": "-2.6%"}, {"name": "Tonga", "code": "TON", "tempRate": "-3.7%"}, {"name": "Trinidad And Tobago", "code": "TTO", "tempRate": "-2.6%"}, {"name": "Tunisia", "code": "TUN", "tempRate": "-13.3%"}, {"name": "Turkey", "code": "TUR", "tempRate": "-17.6%"}, {"name": "Turkmenistan", "code": "TKM", "tempRate": "-19.8%"}, {"name": "Tuvalu", "code": "TUV", "tempRate": "-1.4%"}, {"name": "Uganda", "code": "UGA", "tempRate": "-3.9%"}, {"name": "Ukraine", "code": "UKR", "tempRate": "-43.4%"}, {"name": "United Arab Emirates", "code": "ARE", "tempRate": "-6.3%"}, {"name": "United Kingdom", "code": "GBR", "tempRate": "-20.4%"}, {"name": "United States", "code": "USA", "tempRate": "-18.9%"}, {"name": "Uruguay", "code": "URY", "tempRate": "3.3%"}, {"name": "Uzbekistan", "code": "UZB", "tempRate": "-18.1%"}, {"name": "Vanuatu", "code": "VUT", "tempRate": "-2.7%"}, {"name": "Venezuela", "code": "VEN", "tempRate": "-3.9%"}, {"name": "Vietnam", "code": "VNM", "tempRate": "-5.6%"}, {"name": "West Bank", "code": "XWB", "tempRate": "-10.5%"}, {"name": "Yemen", "code": "YEM", "tempRate": "-3.0%"}, {"name": "Zambia", "code": "ZMB", "tempRate": "-0.2%"}, {"name": "Zimbabwe", "code": "ZWE", "tempRate": "-1.1%"}]
        }
    },
    mounted() {
        this.placeSelection = window.localStorage.getItem('placeSelection');
        this.scaleSelection = window.localStorage.getItem('scaleSelection');
        console.log(this.placeSelection);
        console.log(this.scaleSelection);
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
        // TODO: selectCountry
        showCity(countryCode){
            this.placeSelection = countryCode;
            this.scaleSelection = 1;
            window.localStorage.setItem('placeSelection', this.placeSelection);
            window.localStorage.setItem('scaleSelection', this.scaleSelection);

            this.info.update();
            if(this.cityMarkers!=null){
                console.log('222');
                this.cityMarkers.clearLayers();
            }


            if(countryCode != 'CHN'){
                console.log('111');
                return;
            }
            var layers = [];
            for (let i of this.cityInfo) {
                var city = {};
                city.lat = i.lat;
                city.lng = i.long;
                layers.push(L.circleMarker(city, {
                    color: 'green',
                    fillColor: 'green',
                    fillOpacity: 0.5,
                    radius: 5,
                    zIndexOffset: 9999
                }).bringToFront().addTo(this.map).bindPopup(`Population: ${i.popu}<br>Temperature increase rate: ${i.tempRate}`));
            }
            this.cityMarkers = L.layerGroup(layers);
            this.map.addLayer(this.cityMarkers);
        },
        zoomToFeature(e) {
            const layer = e.target;
            this.map.fitBounds(layer.getBounds());
            var countryCode = layer.feature.properties.code;
            console.log(countryCode);
            this.showCity(countryCode)
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
            L.control.layers(this.allOptions, null, {collapsed: false}).addTo(this.map);

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
