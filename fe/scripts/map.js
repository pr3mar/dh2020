const serverBaseUrl = 'http://localhost:5000/api/spills'

const spillMarkers = L.layerGroup();

const mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
  '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
  'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
const mbUrl = "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw";

const grayscale   = L.tileLayer(mbUrl, {id: 'mapbox/light-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr}),
  streets  = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});

const spillMap = L.map('oilMap', {
  center: [-21., 56.],
  zoom: 5,
  layers: [grayscale, spillMarkers]
});

(() => {
  axios.get(serverBaseUrl)
    .then(data => {
      for (record of data.data) {
        const coords = record.Coords.split(';');
        console.log(record);
        L.marker(coords).bindPopup( '<div tabs>' +

          '<div class="tab" id="tab-1">' +
          '<div class="content">' +
          '<b>Spill Info</b>' +
          '<table>' +
          '<tr><td>Spill</td><td>' + record.Spill + '</td></tr>' +
          '<tr><td>Date</td><td>' + record.Dates + '</td></tr>' +
          '<tr><td>Location</td><td>' + record.Location + '</td></tr>' +
          '<tr><td>Min tonnes</td><td>' + (record.MinTonnes ? record.MinTonnes : 'N/A') + '</td></tr>' +
          '<tr><td>Max tonnes</td><td>' + (record.MaxTonnes ? record.MinTonnes : 'N/A') + '</td></tr>' +
          '<tr><td>Owner</td><td>' + record.Owner + '</td></tr>' +
          '</table>' +
          '</div>' +
          '</div>' +

          '<div class="tab" id="tab-2">' +
          '<div class="content">' +
          '<b>History</b>' +
          '</div>' +
          '</div>' +

          '<div class="tab" id="tab-3">' +
          '<div class="content">' +
          '<b>Public reaction</b>' +
          '</div>' +
          '</div>' +

          '<ul class="tabs-link">' +
          '<li class="tab-link"> <a href="#tab-1"><span>Spill Info</span></a></li>' +
          '<li class="tab-link"> <a href="#tab-2"><span>History</span></a></li>' +
          '<li class="tab-link"> <a href="#tab-3"><span>Public Reaction</span></a></li>' +
          '</ul>' +
          '</div>').addTo(spillMarkers);
      }
    })
    .catch(err => console.log(err));
})();

const baseLayers = {
  "Streets": streets,
  "Grayscale": grayscale
};

const overlays = {
  "Cities": spillMarkers
};

L.control.layers(baseLayers, overlays).addTo(spillMap);
